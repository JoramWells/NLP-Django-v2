from django.urls import path
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static 
from .views import  QuoteView,AddQuoteView,QuoteCategoryView, Auth, display


  
urlpatterns = [ 
    
    url(r'^$',QuoteView.as_view(),name='quote-detail'),
    path('add_quote/',AddQuoteView.as_view(),name='add_quote'),
    path('quote_category/<str:cats>', QuoteCategoryView,name='quote_category'),
    path('meme_lord/<str:auth>',Auth ,name='meme_lord'),
    url(r'^results/$', display, name="disp"),
 
] 

