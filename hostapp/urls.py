from django.urls import path, include
from .views import GET, POST


urlpatterns = [
    path('links/<str:code>', GET.boxes, name='getBoxes'),
    path('create-code', POST.create_code, name='newCode'),
    path('add-link', POST.add_link, name='addLink')
]