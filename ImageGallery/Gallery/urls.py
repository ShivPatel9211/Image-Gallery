from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.gallery, name='gallery'),
    path('upload',views.uploadPhoto, name='upload'),
    path('category/<int:id>',views.category,name='category'),
    path('viewPhoto/<int:id>',views.viewPhoto,name='viewPhoto' ),
    path('rotateleft/<int:id>',views.rotateleft,name='rotateleft' ),
    path('rotateright/<int:id>',views.rotateright,name='rotateright' ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)