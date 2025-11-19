"""
Account views for user authentication
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()


def register(request):
    """User registration - username and password only (does not write to database)"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if not username or not password:
            messages.error(request, "Please provide both username and password.")
        elif password != password2:
            messages.error(request, "Passwords do not match.")
        else:
            # Registration form submitted but does not write to database
            messages.success(
                request,
                f"Registration form submitted for {username}! (Note: This is a template - registration does not write to database)",
            )
            return redirect("login")

    return render(request, "accounts/register.html")


def login_view(request):
    """Custom login view - only accepts admin/cps5301"""
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "cps5301":
            # Get or create admin user
            user, created = User.objects.get_or_create(username=username)
            if created or not user.check_password(password):
                # Set password correctly (handles both new and existing users)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.save()

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                next_url = request.POST.get("next") or request.GET.get("next", "/")
                return redirect(next_url)
            else:
                messages.error(request, "Failed to authenticate. Please try again.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "accounts/login.html")


def logout_view(request):
    """Custom logout view"""
    # Store logout message before clearing session
    messages.success(request, "You have been successfully logged out.")

    # Logout user (this clears auth-related session data)
    logout(request)

    return redirect("login")


@login_required
def account_page(request):
    """User account page"""
    context = {
        "user": request.user,
    }
    return render(request, "accounts/account.html", context)
