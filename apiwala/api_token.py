from random import choice,randint
from django.contrib.auth.models import User
from .models import CustomUserModel as cum,SubscriptionType as stype
token_choices = ["-","_"] + [chr(j) for j in range(97,123)] + [chr(i) for i in range(65,91)]

def generate_random_unique_token(username):
    size = 60
    breakpoint = randint(1,size-3)
    Generated_key = ""
    for i in range(size):
        if i == breakpoint:
            Generated_key += username
        else:
            Generated_key += choice(token_choices)
    return Generated_key

def validate_token(token):
    try:
        objects =  cum.objects.get(api_key=token)
        return True
    except:
        return False

def GetUserNameByToken(token):
    # this function is only calls when user exists so not using try/except.
    objects =  cum.objects.filter(api_key=token)
    for obj in objects:
        return obj.index

def is_limit_Excced(token):
    object = cum.objects.filter(api_key=token)
    for obj in object:
        if int(obj.limit) >= 1:
            obj.limit = str(int(obj.limit) - 1)
            obj.save()
            return False
        else:
            return True

def post_limit_check(token):
    object = cum.objects.filter(api_key=token)
    for obj in object:
        if int(obj.limit) >= 3:
            obj.limit = str(int(obj.limit) - 3)
            obj.save()
            return False
        else:
            return True

def GetQueryLimitsByToken(token):
    object = cum.objects.filter(api_key=token)
    for obj in object:
        return obj.limit

def GetPlanInfo(username):
    # returns a dict object of bool value
    sinfo = stype.objects.get(index=username)
    d = {}
    d['free'] = sinfo.free_plan
    d['silver'] = sinfo.silver_plan
    d['gold'] = sinfo.gold_plan
    d['diamond'] = sinfo.diamond_plan

    return d

def is_Diamond(apitoken):
    user = GetUserNameByToken(apitoken)
    obj = stype.objects.get(index=user)
    return obj.diamond_plan