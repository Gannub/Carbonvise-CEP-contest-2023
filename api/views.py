from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from market.models import Market
from .serializers import UserSLZ
from rest_framework import viewsets
from django .contrib.auth import get_user_model
from profiles.models import Profile
User =get_user_model()

class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        qs_all = User.objects.filter(is_dealer=True)
        serializer = UserSLZ(qs_all, many=True)
        serializer_prof = UserSLZ(qs_all,many=True)
        return Response(serializer.data)


# class UserViewsets(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSLZ 
#     http_method_names = ['get']