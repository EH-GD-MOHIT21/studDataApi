from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserData,ApiPermissions as apm
from .serializers import *
from .api_token import *
from .loginmanager import *
from django.contrib import messages
from .post_data_verifier import postverifier
# Create your views here.

class APIWALA(APIView):
    def get(self,request,apikey):
        if validate_token(apikey):
            if apm.objects.get(index=GetUserNameByToken(apikey)).get_api_permission:
                username = GetUserNameByToken(apikey)
                # managing query limits
                if is_limit_Excced(apikey):
                    return Response({'status':409,'message':'Your query limit excceds please purchase some credits.'})
                # check for plan here
                plans = GetPlanInfo(username)

                if plans['gold'] or plans['diamond']:
                    studobj = UserData.objects.all()
                    studSerial = GoldPlanSerializer(studobj,many=True)
                    limit_remains = GetQueryLimitsByToken(apikey)
                    if plans['diamond']:
                        ans = 'Diamond'
                    else:
                        ans = 'Gold'
                    return Response({'status':200,'payload':studSerial.data,'user':str(username),'limit_remaining':limit_remains,'plan':ans})

                if plans['silver']:
                    studobj = UserData.objects.all()[:25]
                    studSerial = SilverPlanSerializer(studobj,many=True)
                    limit_remains = GetQueryLimitsByToken(apikey)
                    return Response({'status':200,'payload':studSerial.data,'user':str(username),'limit_remaining':limit_remains,'plan':'Silver'})

                if plans['free']:
                    studobj = UserData.objects.all()[:10]
                    studSerial = FreePlanSerializer(studobj,many=True)
                    limit_remains = GetQueryLimitsByToken(apikey)
                    return Response({'status':200,'payload':studSerial.data,'user':str(username),'limit_remaining':limit_remains,'plan':'free'})
                else:
                    return Response({'status':404,'message':'Couldnot find your plan please try again.'})
            else:
                return Response({'status':404,'message':'You need Permissions.'})
        else:
            return Response({'status':404,'message':'Invalid API TOKEN.'})
    def post(self,request,apikey):
        if validate_token(apikey):
            if is_Diamond(apikey):
                if postverifier().DataisNull(request.data):
                    return Response({'status':404,'message':'Please Provide All Data.','fields':postverifier().fields})
                if not postverifier().verify_name(request.data['name_of_student']):
                    return Response({'status':309,'message':'Invalid Name'})
                if not postverifier().verify_name(request.data['father_name']):
                    return Response({'status':309,'message':'Invalid Fathers Name'})
                if not postverifier().verify_name(request.data['course_enrolled']):
                    return Response({'status':309,'message':'Invalid Course Name'})
                if not postverifier().verify_name(request.data['college_name']):
                    return Response({'status':309,'message':'Invalid College Name.'})
                if not postverifier().verifyphone(request.data['phone_no']):
                    return Response({'status':309,'message':'Invalid Phone Number'})
                if not postverifier().verify_mail(request.data['email']):
                    return Response({'status':309,'message':'Invalid Email.'})
                if not postverifier().verify_age(request.data['age']):
                    return Response({'status':309,'message':'Invalid Age.'})
                if not postverifier().verify_year(request.data['year_of_study']):
                    return Response({'status':309,'message':'Invalid Year of study mantian between 1 to 4.'})

                # save the data

                serial = GeneralSerializers(data=request.data)
                if serial.is_valid():
                    if not post_limit_check(apikey):
                        serial.save()
                        return Response({'status':200,'message':'Approved Your Request','limit_remaining':GetQueryLimitsByToken(apikey),'payload':request.data})
                    else:
                        return Response({'status':420,'message':'Data Verified But You have not enough credits to save please purchase some to continue.','limit_remaining':GetQueryLimitsByToken(apikey)})
                else:
                    return Response({'status':404,'message':'Something Went Wrong.'})
            else:
                return Response({'status':300,'message':'Please Purchase Diamond pack for this Request'})
        else:
            return Response({'status':404,'message':'Invalid Api token.'})

    def put(self,request,apikey):
        if validate_token(apikey):
            if is_Diamond(apikey):
                return Response({'status':200,'message':'Approved Your Request'})
            else:
                return Response({'status':300,'message':'Please Purchase Diamond pack for this Request'})
        else:
            return Response({'status':404,'message':'Invalid Api token.'})
    def patch(self,request,apikey):
        if validate_token(apikey):
            if is_Diamond(apikey):
                return Response({'status':200,'message':'Approved Your Request'})
            else:
                return Response({'status':300,'message':'Please Purchase Diamond pack for this Request'})
        else:
            return Response({'status':404,'message':'Invalid Api token.'})
    def delete(self,request,apikey):
        return Response({'status':404,'message':'Only ADMIN has access to Delete Data.'})


def home(request):
    return render(request,'index.html')

def mainRegister(request):
    if request.method == 'POST':
        new_ = validateuser(request)
        if new_[0]:
            messages.success(request,f"Your Api link is mailed on {request.POST['mailid']}")
            return redirect('/')
        else:
            return render(request,'index.html',{'message':new_[1]})
    else:
        return redirect('/')

def mainLogin(request):
    if request.method == 'POST':
        tuple_obj = loginuser(request)
        if tuple_obj[0]:
            return redirect('/')
        else:
            return render(request,'index.html',{'message':tuple_obj[1]})
    else:
        return redirect('/')

def mainLogout(request):
    if logoutuser(request):
        return redirect('/')

def resetpass(request):
    return render(request,'fpass.html')

def checknupdate(request):
    status,message = main_checknupdate(request)
    if status:
        messages.info(request,'Password Reset Successfully.')
        return redirect('/')
    else:
        messages.info(request,message)
        return redirect('/')

def showapi(request):
    data = DisplayApiRequestByWeb(request)
    if data is None:
        return render(request,'index.html',{'message':'Please Login to access this feature.'})
    else:
        return render(request,'personalDetails.html',{'data':data})

