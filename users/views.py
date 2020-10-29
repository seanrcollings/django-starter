from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from rest_framework import viewsets, permissions, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerialzer

from .models import User
from .forms import LoginForm, RegistrationForm


class UserIndex(ListView):
    model = User
    template_name = "users/index.html"


class UserShow(DetailView):
    model = User
    template_name = "users/show.html"


class RegisterView(View):
    form = RegistrationForm
    template_name = "users/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            user = User(
                username=request.POST.get("username"),
                password=request.POST.get("password"),
                first_name=request.POST.get("first_name"),
                last_name=request.POST.get("last_name"),
            )
            user.save()
            messages.success(request, "Registered")
            return redirect("users_index")

        return render(request, self.template_name, {"form": form})


class LoginView(View):
    form = LoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST["username"],
                password=request.POST["password"],
            )
            if user is not None:
                login(request, user)
                messages.error(request, "Logged in")
                return redirect("users_index")

            messages.error(request, "Invalid Username of Password")
            return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("users:index")


### API ###
class UserViewSet(viewsets.ModelViewSet):
    """API Endpoint to view or edit users"""

    queryset = User.objects.all().order_by("date_joined")
    serializer_class = UserSerialzer
    # permission_classes = [permissions.IsAuthenticated]


# class ListUsers(views.APIView):
#     def get(self, request, format=None):
#         breakpoint()


# @api_view(["GET"])
# def test_view(request):
#     print("hi there")
#     breakpoint()
#     return Response({"message": "hello there"})
