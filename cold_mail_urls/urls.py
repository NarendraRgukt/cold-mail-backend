from django.urls import path
from employees.views import EmployeeView

urlpatterns = [
    path("employees/", EmployeeView.as_view()),             # POST
    path("employees/<uuid:pk>/", EmployeeView.as_view()),   # PUT, DELETE
]
