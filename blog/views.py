# views.py
from django.shortcuts import render, redirect
from .models import SkewStarh1, SkewStarP, PersonalInfo, Skill, AboutMe, Service, Work, Partfolio, PortfolioTitle, BlogTitle, Blog, Contact, BlogSingle


# def HomePage(request) :
#     return render(request, 'index.html')

def menu_view(request):
    menu_items = [
        {"name": "Home", "url": "index.html"},
        {"name": "About", "url": "#about"},
        {"name": "Services", "url": "#services"},
        {"name": "Work", "url": "#work"},
        {"name": "Contact", "url": "#contact"},
    ]
    personal_info = PersonalInfo.objects.all()
    skills = Skill.objects.all()
    about_me = AboutMe.objects.first()
    title = SkewStarh1.objects.all()
    subtitle = SkewStarP.objects.all()
    service = Service.objects.all()
    work = Work.objects.all()
    partfolio = Partfolio.objects.all()
    portfolio_title = PortfolioTitle.objects.all()
    blog_title = BlogTitle.objects.all()
    blog = Blog.objects.all()
    contact = Contact.objects.all()
    context = {
        'personal_info': personal_info,
        'skills': skills,
        'about_me': about_me,
        "menu_items": menu_items,
        "title": title,
        "subtitle": subtitle,
        "service":service,
        "work" : work,
        "partfolio" : partfolio,
        "portfolio_title" : portfolio_title,
        "blog_title" : blog_title,
        "blog" : blog,
        "contact" : contact 
    }
    return render(request, 'index.html', context)

def blog_single(request):
    blog = {"name": "Blog", "url": "#blog"}
    blog_entries = BlogSingle.objects.all()
    context = {
        "blog": blog,
        "blog_entries": blog_entries,
    }
    # Render the template with the context
    return render(request, 'blogsingle.html', context)
