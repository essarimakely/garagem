from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet,CorViewSet,AcessorioViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"acessorios", AcessorioViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

