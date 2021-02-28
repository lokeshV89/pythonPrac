
from django.urls import path, include
from . import views

urlpatterns = [
    path('/',views.index,name='uploadIndex'),
    path('/saveImage',views.saveImage,name='saveImage'),
    
]
