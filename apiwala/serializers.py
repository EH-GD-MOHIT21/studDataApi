from django.db.models import fields
from rest_framework import serializers
from .models import UserData

class FreePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["name_of_student","age","year_of_study"]

class SilverPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["name_of_student","age","year_of_study","father_name","course_enrolled"]

class GoldPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ["id"]

class GeneralSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = "__all__"