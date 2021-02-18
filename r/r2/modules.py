from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
import csv
from .document_similarity import *
from django.contrib.staticfiles import finders
from django.shortcuts import render
from .models import PostQ,Post
from django.views import View
from django.shortcuts import render
from .serchx import *
