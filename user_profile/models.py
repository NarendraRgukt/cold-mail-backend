from django.db import models

from user_accounts.models import User
# from django_cryptography.fields import encrypt
from django.core import signing

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    linkedin_url = models.URLField(max_length=255, null=True, blank=True)
    github_url = models.URLField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    # gmail_app_password = encrypt(models.CharField(max_length=255, null=True, blank=True))
    gmail_app_password_encrypted = models.TextField(null=True, blank=True)

    def set_gmail_app_password(self, raw_password):
        """Encrypt and store Gmail app password"""
        self.gmail_app_password_encrypted = signing.dumps(raw_password)
        self.save(update_fields=['gmail_app_password_encrypted'])

    def get_gmail_app_password(self):
        """Decrypt Gmail app password"""
        if not self.gmail_app_password_encrypted:
            return None
        try:
            return signing.loads(self.gmail_app_password_encrypted)
        except signing.BadSignature:
            return None
    

    def __str__(self):
        return f"{self.user.username}'s Profile"
