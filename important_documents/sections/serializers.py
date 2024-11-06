from rest_framework import serializers
from .models import Section, File

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'section', 'file', 'file_name', 'file_type', 'file_size', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
