from django.contrib.auth import get_user_model

from rest_framework import viewsets, authentication, permissions, filters

from .models import Building, Position
from .serializers import BuildingSerializer, PositionSerializer, UserSerializer

User = get_user_model()

class DefaultsMixin(object):
    authentication_classes = (
        #authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )

class BuildingViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Building.objects.order_by('name')
    serializer_class = BuildingSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

class PositionViewSet(DefaultsMixin, viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    search_fields = ('coords',)
    ordering_fields = ('player',)

class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )