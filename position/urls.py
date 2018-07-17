from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'buildings', views.BuildingViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'users', views.UserViewSet)