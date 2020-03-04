from django.contrib import admin
from django.urls import path, include
from helloapp import views

# set urls
urlpatterns = [
    path('index2/', include('bioinformaticsapp.urls')) ,
    path('index1/',views.hello),
    path('admin/', admin.site.urls),
]
