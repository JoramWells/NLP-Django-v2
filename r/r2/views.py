from django.shortcuts import render,get_object_or_404
from .models import PostQ,Post
from django.views.generic import ListView,DetailView,CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import QuoteForm
from django.contrib.auth.models import User

from .modules import *

queryset = PostQ.objects.all()


class QuoteView(ListView):
    model = PostQ
    template_name= 'index.html'



def QuoteCategoryView(request,cats):
    quote_category_posts=PostQ.objects.filter(category=cats)
    return render(request,'category.html',{'cats':cats,'quote_category_posts':quote_category_posts})


def Auth(request,auth):
    obj=PostQ.objects.filter(author=auth)
    auth_posts=PostQ.objects.filter(author__exact=obj.id)

    return render(request,'author.html',{'auth':auth,'auth_posts':auth_posts})


class AddQuoteView(CreateView):
    model=PostQ
    template_name='upload.html'
    form_class = QuoteForm
    ##fields='__all__'



def query_to_csv(queryset, filename='items.csv', **override):
    field_names = [field.name for field in queryset.model._meta.fields]
    def field_value(row, field_name):
        if field_name in override.keys():
            return override[field_name]
        else:
            return row[field_name]
    with open(filename, 'w+', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')
        writer.writerow(field_names) 
        for row in queryset.values(*field_names):
            writer.writerow([field_value(row, field) for field in field_names])


query_to_csv(queryset, filename='data.csv', user=1, group=1)



def display(request):
    if request.method == 'POST':
        if request.POST.get('keyword'):#if request.POST.get('keyword') and request.POST.get('videos'):
            post=Post()
            post.keyword = request.POST.get('keyword')
            post.min_videos = 10 #request.POST.get('videos')
            post.save()
            q= Post.objects.all().order_by('-created_on')[:1]
            
            query_to_csv(q, filename='serchin.csv', user=1, group=1)
            d = read_data('serchin.csv')
            key = d['keyword']
            key = key[0]
            url = d['min_videos']
            url =url[0]
            sl = SearchView( key,url)
            s2 = sl.postl()
            
            if len(s2) == 0:
                return HttpResponse('Not Found')
            url=[]
            for i in s2:
                c=PostQ.objects.get(id=i)
                url.append(c)
                context={
                    'url':url
                    }
                
            return render(request,'create.html',context)
    else:
        return render(request,'index.html')