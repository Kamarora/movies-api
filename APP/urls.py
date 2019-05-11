from django.conf.urls import url
from django.urls import path  
from django.contrib import admin  
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
	# url('mvi', views.mvi),  
	# url('show',views.show),  
	# url('edit/<int:id>', views.edit),  
	# url('update/<int:id>', views.update),  
	# url('delete/<int:id>', views.destroy),  
    path('admin/', admin.site.urls),  
    path('mvi', views.mvi),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy), 
    path('search', views.search),
    path('login', views.login),
    path('logout', views.logout),
]
