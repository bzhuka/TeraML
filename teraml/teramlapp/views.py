from django.shortcuts import render_to_response
from django.template import RequestContext
from teramlapp.models import Post
import datetime

def index(request):
    if request.method == 'POST':
       # save new post
        print("STEP 1")
        title = request.POST['title']
        content = request.POST['content']

        post = Post(title=title)
        post.last_update = datetime.datetime.now() 
        post.content = content
        post.save()
    elif request.method == 'GET':
        print("Hello")

    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))

def query(request):
    print("ASFD")
    if request.method == 'POST':
       # save new post
        print("STEP 1")
        title = request.POST['title']
        content = request.POST['content']

        post = Post(title=title)
        post.last_update = datetime.datetime.now() 
        post.content = content
        post.save()
    elif request.method == 'GET':
        print("Hello")

    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))

