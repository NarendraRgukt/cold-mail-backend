from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate(self, data):
        if not data.get("first_name"):
            raise serializers.ValidationError({"first_name": "This field is required."})
        if not data.get("company_name"):
            raise serializers.ValidationError({"company_name": "This field is required."})
        if not data.get("role_name"):
            raise serializers.ValidationError({"role_name": "This field is required."})
        return data
