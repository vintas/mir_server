from rest_framework import serializers
from .models import Package, Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['name', 'version']

class DependencySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    version = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=10)

class PackageSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Package
        fields = ['name', 'version', 'description', 'dependencies', 'type', 'file_url']

    def get_dependencies(self, obj):
        dependencies = []
        # Add library dependencies
        for library in obj.libraries.all():
            item_type = 'library'
            if 'conf' in library.name or 'pem' in library.name:
                item_type = 'config'
            else:
                item_type = 'library'
            dependencies.append({
                'name': library.name,
                'version': library.version,
                'type': item_type
            })
        # Add package dependencies
        for dependency in obj.dependencies.all():
            dependencies.append({
                'name': dependency.name,
                'version': dependency.version,
                'type': 'package'
            })
        return dependencies

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None

    def get_type(self, obj):
        return 'package'

class LibraryWithDependenciesSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = ['name', 'version', 'dependencies', 'type', 'file_url']

    def get_dependencies(self, obj):
        dependencies = []
        # Add library dependencies
        for library in obj.dependencies.all():
            item_type = 'library'
            if 'conf' in library.name or 'pem' in library.name:
                item_type = 'config'
            else:
                item_type = 'library'
            dependencies.append({
                'name': library.name,
                'version': library.version,
                'type': item_type
            })
        return dependencies

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None

    def get_type(self, obj):
        print(obj)
        if 'conf' in obj.name or 'pem' in obj.name:
            return 'config'
        return 'library'
