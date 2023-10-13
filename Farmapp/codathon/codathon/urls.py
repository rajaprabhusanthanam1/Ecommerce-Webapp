"""
URL configuration for codathon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from farmapp import views
from farmapp.models import Product1, Order, OrderItem
from django.conf.urls.static import static
from django.conf import settings
#from farmapp.views import UserProfile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signuppage,name='signup'),
    path('login/',views.loginpage,name='login'),
    path('f1/',views.f1y,name='f1'),
    path('f2/',views.f2w,name='f2'),
    path('f3/',views.f3s,name='f3'),
    path('logout/',views.LogoutPage,name='logout'),
    path('f4/',views.f4c,name='f4'),
    path('orders/', views.order_list, name = 'order_list'),
    path('orders/<int:order_id/', views.order_detail, name = 'order_detail'),   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)