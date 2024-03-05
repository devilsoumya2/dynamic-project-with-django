"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.aboutUs,name="about"),
    path('blog/', views.blog,name="blog"),
    path('contact/', views.contact,name="contact"),
    path('menu/', views.menu,name="menu"),
    path('products/', views.products,name="products"),
    path('review/', views.review,name="review"),
    path('submitform/', views.submitform,name="submitform"),
    path('saveenquiry/', views.saveEnquiry,name="saveenquiry"),
    path('course/<courseid>', views.courseDetails),
    path('', views.homepage),
    path('userform/', views.userform),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd, name="evenodd"),
    path('marksheet/', views.marksheet),
    path('newsdetails/<slug>', views.newsDeatatils),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
