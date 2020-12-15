from django.shortcuts import render
from models import Profile
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib import auth
from Bot.views import joinclass
import sqlite3

# Create your views here.

