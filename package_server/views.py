from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Package, Library
from .forms import PackageForm, LibraryForm

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PackageSerializer
from packaging.version import Version, InvalidVersion

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@login_required
def home_view(request):
    packages = Package.objects.filter(user=request.user)
    return render(request, 'home.html', {'packages': packages})

@login_required
def add_package_view(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.user = request.user
            package.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('home')
    else:
        form = PackageForm()
    return render(request, 'add_package.html', {'form': form})

def add_library_view(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_package')  # Redirect to add package page after adding a library
    else:
        form = LibraryForm()
    return render(request, 'add_library.html', {'form': form})

@api_view(['GET'])
def package_detail_view(request, name, version=None):
    try:
        if version:
            package = Package.objects.get(name=name, version=version)
        else:
            packages = Package.objects.filter(name=name)
            if not packages:
                raise Package.DoesNotExist
            package = max(packages, key=lambda p: Version(p.version))
    except Package.DoesNotExist:
        return Response({'error': 'Package not found'}, status=404)
    except InvalidVersion:
        return Response({'error': 'Invalid version format'}, status=400)

    serializer = PackageSerializer(package, context={'request': request})
    return Response(serializer.data)
