
from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Market
from django.contrib.auth import get_user_model

User = get_user_model()
