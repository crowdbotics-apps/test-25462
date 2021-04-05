from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ItemViewSet, ListViewSet, RunViewSet

router = DefaultRouter()
router.register("item", ItemViewSet)
router.register("run", RunViewSet)
router.register("list", ListViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
