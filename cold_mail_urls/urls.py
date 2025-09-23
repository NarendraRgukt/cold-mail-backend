from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from employees.views import EmployeeView,BulkEmployeeUploadView,EmployeeListView,EmployeeCountView
from user_profile.views import ProfileCreateAPIView,ProfileUpdateAPIView
from user_accounts.views import LoginAPIView

urlpatterns = [
    path("employees/", EmployeeView.as_view()),             # POST
    path("employees/<uuid:pk>/", EmployeeView.as_view()), 
     path("employees/bulk-upload/", BulkEmployeeUploadView.as_view()), 
      path("get/employees/", EmployeeListView.as_view(), name="employee-list"),
      path("employees/count/", EmployeeCountView.as_view(), name="employee-count"),
        path("profile/create/", ProfileCreateAPIView.as_view(), name="profile-create"),
    path("profile/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
     path("login/", LoginAPIView.as_view(), name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)