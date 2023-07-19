from rest_framework import serializers
from django.contrib.auth import get_user_model
from market.models import Market
from profiles.models import Profile
from dealer.models import Dealer

User = get_user_model()


# class 

class DealerSLZ(serializers.ModelSerializer):
    deal_province = serializers.CharField(source='get_deal_province_display')
    class Meta:
        model = Dealer
        # fields = '__all__'
        exclude = ['id','shop_icon']


class UserProvinceSLZ(serializers.ModelSerializer):
    province = serializers.CharField(source='get_province_display')
    class Meta:
        model = Profile
        fields = ['province',]
        


class DealsSLZ(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['name',]


class UserSLZ(serializers.ModelSerializer):
    deal_created = DealsSLZ(many=True)
    profile = UserProvinceSLZ()
    dealer_data = DealerSLZ(many=False)
    class Meta:
        
        model = User
        fields = ['first_name','last_name','email','profile','dealer_data','deal_created']
        # fields = '__all__'
        # exclude = []


