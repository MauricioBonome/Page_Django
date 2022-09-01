from django.shortcuts import render
from .models import post
def render_posts(request):
    posts =post.objects.all()
    return render(request,'posts.html',{'posts':posts})