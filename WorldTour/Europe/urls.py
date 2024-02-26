# from django.urls import path
# from . import views

# urlpatterns = [
#     path(" ", views.index)
    
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello)  # Use an empty string instead of " "
]
