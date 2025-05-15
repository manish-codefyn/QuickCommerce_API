from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id', 'type', 'title', 'message', 
            'is_read', 'related_id', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class NotificationMarkReadSerializer(serializers.Serializer):
    is_read = serializers.BooleanField()
    
    def update(self, instance, validated_data):
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.save()
        return instance