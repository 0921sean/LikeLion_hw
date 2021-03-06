"""BookSurfing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    path('detail/<int:blog_id>/', views.detail, name='detail'),

    path('new_comment/<int:blog_id>/', views.new_comment, name='new_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),

    path('accounts/', include('accounts.urls')),

    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('edit/<str:blog_id>/', views.edit, name='edit'),
    path('delete_comment/<str:comment_id>/', views.delete_comment, name='delete_comment')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'myapp.views.page_not_found'