from django.urls import path
from employees.views import EmployeeView,BulkEmployeeUploadView,EmployeeListView

urlpatterns = [
    path("employees/", EmployeeView.as_view()),             # POST
    path("employees/<uuid:pk>/", EmployeeView.as_view()), 
     path("employees/bulk-upload/", BulkEmployeeUploadView.as_view()), 
      path("get/employees/", EmployeeListView.as_view(), name="employee-list"),
]
