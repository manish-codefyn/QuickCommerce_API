from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.models import SocialAccount
from django.http import HttpResponse
from django.shortcuts import redirect
import json


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed.
        """
        # Check if the email is already registered
        email = sociallogin.user.email
        if email and self.email_exists(email):
            # If email exists, link accounts
            existing_user = self.get_user_by_email(email)
            sociallogin.connect(request, existing_user)
            raise ImmediateHttpResponse(redirect('/'))
    
    def email_exists(self, email):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.filter(email=email).exists()
    
    def get_user_by_email(self, email):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        return User.objects.get(email=email)