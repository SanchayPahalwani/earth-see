from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Building, Position

User = get_user_model()

class BuildingSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = Building
        fields = ('id', 'name', 'description', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('building-detail', kwargs={'pk': obj.pk}, request = request),
       }

class PositionSerializer(serializers.ModelSerializer):
    
    links = serializers.SerializerMethodField()

    class Meta:
        model = Position
        fields = ('building', 'coords', 'player', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('position-detail', kwargs={'pk': obj.pk}, request = request),
            'building': reverse('building-detail', kwargs={'pk': obj.building}, request=request),
            'player': reverse('user-detail', kwargs={User.USERNAME_FIELD: obj.player}, request=request)
        }

class UserSerializer(serializers.ModelSerializer):
    
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    links = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        username = obj.get_username()
        return {
            'self': reverse('user-detail', kwargs={User.USERNAME_FIELD: username}, request=request),
        }