from django.contrib import admin
from django.urls import path, include
from helloapp import views
from bioinformaticsapp import views as bioviews

# set urls
urlpatterns = [
    path('bio/', include('bioinformaticsapp.urls')) ,
    path('test/',views.hello),
    path('', bioviews.homeroot)

]
