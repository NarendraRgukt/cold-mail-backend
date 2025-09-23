from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "resume", "linkedin_url", "github_url", "phone_number","gmail_app_password_encrypted"]
