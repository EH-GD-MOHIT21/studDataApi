from django.contrib.auth import authenticate,login,logout
import smtplib
from email.message import EmailMessage
from django.contrib.auth.models import User
from .models import *
from .api_token import generate_random_unique_token as gru_token


def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is None:
        return (False,"Invalid Credentials")
    else:
        login(request,user)
        return (True,"Valid Credentials")

def validateuser(request):
    username = request.POST['username']
    password = request.POST['password']
    email_id = request.POST['mailid']
    if len(username)<=4 or len(username)>=20 or not username.isalnum():
        return (False,"Username should be alphanumeric and length between 5 to 19")
    elif len(password) <8 or password.isnumeric() or password.isalpha():
        return (False,"Password length should be 8 and not only numeric or alphabetical")
    else:
        uobj = User.objects.filter(username=username)
        for obj in uobj:
            return (False,"Username not available.")
        context = createNewInstances(request)
        if context:
            return (True,None)
        else:
            return (False,"Something went wrong")

def createNewInstances(request):
    try:
        new_obj = User(username=request.POST['username'])
        new_obj.set_password(request.POST['password'])
        new_obj.email = request.POST['mailid']
        new_obj.save()
        apikey = gru_token(request.POST['username'])
        ncm = CustomUserModel(index=new_obj,api_key=apikey)
        ncm.save()
        nsm = SubscriptionType(index=new_obj)
        nsm.save()
        api_permission = ApiPermissions(index=new_obj,get_api_permission=True)
        api_permission.save()
        if mailCredentials(to=request.POST['mailid'],api_token=apikey):
            return True
        else:
            # delete the credentials since mail not delivered.
            return False
    except:
        return False

def logoutuser(request):
    logout(request)
    return True

def mailCredentials(to,subject=None,message=None,api_token=None):
    sender_mail = "no.reply.python.py@gmail.com"   
    password_sender = "qwerty@123"

    message = EmailMessage()
    message['To'] = to
    message['From'] = sender_mail
    message['Subject'] = "Welcome User to APIWALA.com"
    message.set_content(f"Hello User welcome to APIWALA.com Your API LINK TOKEN is\n\n\n https://smvduapi.herokuapp.com/api/checkuser/{api_token} \n\n\n with free 50 query credits You Can Use it via Get Request Only If You are interested and love our service you can upgrade to higher plans for more benefits. \n Regards\n APIWALA.com")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_mail, password_sender)
        server.send_message(message)
        # print(to,api_token)
        return True
    except:
        return False

def main_checknupdate(request):
    username = request.POST['username']
    api_key = request.POST['api']
    passwd = request.POST['pass']
    cpasswd = request.POST['cpass']
    try:
        c = User.objects.get(username=username)
    except:
        return (False,"User Not Found")
    try:
        d = CustomUserModel.objects.get(index=c,api_key=api_key)
    except:
        return (False,"User Not Found")
    if passwd != cpasswd:
        return (False,"Both Password does not match")
            
    c.set_password(passwd)
    c.save()

    return (True,"Updated")

def DisplayApiRequestByWeb(request):
    if request.user.is_authenticated:
        cum = CustomUserModel.objects.get(index=request.user)
        api_key = cum.api_key
        limit_remain = cum.limit
        username = request.user.username
        stype = SubscriptionType.objects.get(index=request.user)
        api_p = ApiPermissions.objects.get(index=request.user)
        data = {
            'api_key':api_key,
            'limit':limit_remain,
            'username':username,
            'stype_obj':stype,
            'api_permission_obj':api_p
        }
        return data
    else:
        return None