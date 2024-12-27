from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm 
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request,"tweetapp/index.html")
