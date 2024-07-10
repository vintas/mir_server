from rest_framework import serializers
from .models import Package, Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['name', 'version']

class PackageSerializer(serializers.ModelSerializer):
    libraries = LibrarySerializer(many=True)
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = ['name', 'description', 'date_added', 'libraries', 'file_url']

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None
