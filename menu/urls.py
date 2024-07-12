from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet
from .views import menu_view

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'menu-items', MenuItemViewSet)

urlpatterns = [
    path('', menu_view, name='menu'),
    path('api/', include(router.urls)),
]
