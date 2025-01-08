from django.shortcuts import render
#used when we have to return httpresponse
#from django.http import HttpResponse

# Create your views here.
#list of dictionaries
posts = [
    {
        'author': 'martand',
        'title': 'Blog Post 1',
        'content': 'This is first blog post and creating content for display',
        'date_posted':'January 8 2025'
    },
    {
        'author': 'aditya',
        'title': 'Blog Post 2',
        'content': 'This is second blog post and testing the looping over data in template',
        'date_posted':'January 9 2025'
    },
]
def home(request):
    context = {

        'posts':posts
    }
    #return HttpResponse('<h1>Blog home</h1>')
    #render inbuilt function which returns rendered html page
    #passing context as an argument for html html will have access to variable 'posts' directly
    return render(request, 'blog/home.html',context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    #return render(request,'blog/about.html')
    return render(request,'blog/about.html',{'title':'About'})