from rest_framework import serializers
from .models import Package, Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['name', 'version']

class PackageSerializer(serializers.ModelSerializer):
    libraries = LibrarySerializer(many=True)
    dependencies = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = ['name', 'version', 'description', 'date_added', 'libraries', 'dependencies', 'file_url']

    def get_dependencies(self, obj):
        return PackageSerializer(obj.dependencies.all(), many=True, context=self.context).data

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None
