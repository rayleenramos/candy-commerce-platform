"""
URLs for accounts app
"""

from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("account/", views.account_page, name="account"),
    path("account/add-card/", views.add_card, name="add_card"),
    path("account/remove-card/<int:card_id>/", views.remove_card, name="remove_card"),
    path("account/edit/", views.edit_profile, name="edit_profile"),
]
