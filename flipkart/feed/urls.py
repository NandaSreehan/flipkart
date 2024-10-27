from django.urls import path
from feed import views
urlpatterns=[
    path('',views.home,name='homePage'),
    path('about',views.home,name='aboutPage'),
    path('contact',views.home,name='contactPage'),
    path('post',views.home,name='postPage'),

]