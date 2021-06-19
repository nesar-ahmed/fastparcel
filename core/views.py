from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import forms


def home(request):
    return render(request, "home.html", {})


def sign_up(request):
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email").lower()

            user = form.save(commit=False)
            user.username = email
            user.save()

            login(request, user)
            return redirect("/")

    context = {"form": form}
    return render(request, "sign-up.html", context)


@login_required()
def customer_page(request):
    return render(request, "home.html", {})


@login_required()
def courier_page(request):
    return render(request, "home.html", {})
