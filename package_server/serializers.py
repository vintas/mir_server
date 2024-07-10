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

    class Meta:
        model = Package
        fields = ['name', 'version', 'description', 'date_added', 'dependencies', 'file_url']

    def get_dependencies(self, obj):
        dependencies = []
        # Add library dependencies
        for library in obj.libraries.all():
            dependencies.append({
                'name': library.name,
                'version': library.version,
                'type': 'library'
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

class LibraryWithDependenciesSerializer(serializers.ModelSerializer):
    dependencies = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = ['name', 'version', 'dependencies', 'file_url']

    def get_dependencies(self, obj):
        dependencies = []
        # Add library dependencies
        for library in obj.dependencies.all():
            dependencies.append({
                'name': library.name,
                'version': library.version,
                'type': 'library'
            })
        return dependencies

    def get_file_url(self, obj):
        request = self.context.get('request')
        if obj.file:
            return request.build_absolute_uri(obj.file.url)
        return None
