from django.shortcuts import render, redirect
from .models import Article
from .models import Project
from .models import Content
from .forms import ContentForm

# Create your views here.


def home(request):
    return render(request, 'business_app/home.html')


def blog(request):
    articles = Article.objects.all().order_by('-id')[:4]
    contents = Content.objects.filter(content_type='B').order_by('-id') 
    context = {'articles': articles, 'contents': contents}
    return render(request, 'business_app/blog.html', context)


def portfolio(request):
    projects = Project.objects.all().order_by('-id')
    contents = Content.objects.filter(content_type='P').order_by('-id') 
    context = {'projects': projects, 'contents': contents} 
    return render(request, 'business_app/portfolio.html', context)

def create_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save()
            if content.content_type == 'B':
                return redirect('blog')
            else: 
                return redirect('portfolio')
    else:
        form = ContentForm()

    articles = Article.objects.all()
    projects = Project.objects.all()
    contents = Content.objects.all()

    context = {'form': form, 'articles': articles, 'projects': projects, 'contents': contents}

    return render(request, 'business_app/create_content.html', context)



def contact(request):
    return render(request, 'business_app/contact.html')


