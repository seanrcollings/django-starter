from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect

from .models import User
from .forms import LoginForm


class UsersList(ListView):
    model = User
    template_name = "users/index.html"


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
    return redirect("users_index")
