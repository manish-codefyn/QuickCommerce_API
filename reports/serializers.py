from rest_framework import serializers
from .models import Report, Dashboard


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'id', 'name', 'type', 'parameters',
            'file', 'is_ready', 'created_at'
        ]
        read_only_fields = ['id', 'file', 'is_ready', 'created_at']


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = ['id', 'name', 'configuration', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']