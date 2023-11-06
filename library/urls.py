from django.contrib import admin
from django.urls import path
from .api import router
from api.views import cat



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cat', cat )
]