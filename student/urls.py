from django.urls import path
from .views import home,create_student,update_student,delete_student

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('',home , name= 'home'),
    path('create/',create_student,name='create'),
    path('update/<int:id>/',update_student,name='update'),
    path('delete/<int:id>/',delete_student,name='delete'),
   
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
