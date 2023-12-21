from django.urls import path, include
from .views import BoxesView, CodeView, LinkView

urlpatterns = [
    path('links/<str:code>', BoxesView.as_view(), name='getBoxes'),
    path('create-code', CodeView.as_view(), name='newCode'),
    path('add-link', LinkView.as_view(), name='addLink')
]
