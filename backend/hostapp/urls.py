from django.urls import path, include
from .views import BoxesView, CodeView, LinkView

urlpatterns = [
    path('links', BoxesView.as_view(), name='getBoxes'),
    path('create-code', CodeView.as_view(), name='newCode'),
    path('check-code', CodeView.as_view(), name='checkcode'),
    path('add-link', LinkView.as_view(), name='addLink')
]


# from django.urls import path, include
# from .views import BoxesView, CodeView, LinkView

# urlpatterns = [
#     path('links', BoxesView.get, name='getBoxes'),
#     path('create-code', CodeView.post, name='newCode'),
#     path('check-code', CodeView.get, name='checkcode'),
#     path('add-link', LinkView.post, name='addLink')
# ]
