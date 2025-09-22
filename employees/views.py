from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer
import json

class EmployeeView(APIView):

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response({"message": "Employee deleted"}, status=status.HTTP_204_NO_CONTENT)






class BulkEmployeeUploadView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.lower().endswith(".json"):
            return Response({"error": "Only .json files are supported"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            employees = json.load(file)
            if not isinstance(employees, list):
                return Response({"error": "JSON file must contain an array of objects"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Failed to parse JSON: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        success_count = 0
        failed_count = 0
        failed_records = []

        for obj in employees:
            serializer = EmployeeSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
                success_count += 1
            else:
                failed_count += 1
                failed_records.append({
                    "input": obj,
                    "errors": serializer.errors
                })

        report = {
            "success_count": success_count,
            "failed_count": failed_count,
            "failed_records": failed_records
        }
        return Response(report, status=status.HTTP_200_OK)

