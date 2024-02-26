from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Europe.urls')),  # Make sure Europe app's URLs are included correctly
]
