from django.urls import path, include
from .views import ArticleViewSet,UserViewSet
from rest_framework import routers

app_name = 'api'

router= routers.SimpleRouter()
router.register('articles',ArticleViewSet, basename="articles55")
router.register('users',UserViewSet, basename="users")

urlpatterns = [
path('', include(router.urls)),
]