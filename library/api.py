from rest_framework import routers
from api import views
from django.urls import path

# router = routers.DefaultRouter()
# routers.register(r'books', views.BookViewSet)
# routers.register(r'lib-users', views.LibUserViewSet)
# routers.register(r'render-books', views.RentBookViewSet)

from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'books', views.BookViewSet)

