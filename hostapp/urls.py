from django.urls import path, include
from .views import GET, POST


urlpatterns = [
    path('links/<str:code>', GET.boxes, name='getBoxes'),
    path('new', POST.newCode, name='newCode'),
    path('add/<str:code>', POST.newLink, name='addLink')
]