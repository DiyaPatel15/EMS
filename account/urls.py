from django.urls import path, include
from .views import EmployeeViewSet,EmployeeRegistrationView,EmployeeLoginView,TokenRefreshView,EmployeeLogoutView,EmployeeProfileView,EmployeeChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register(r"emp-list", EmployeeViewSet, basename="Employee List")

urlpatterns = [
    path('', include(router.urls)),
    path('register/',EmployeeRegistrationView.as_view(),name="register"),
    path('login/',EmployeeLoginView.as_view(),name="login"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="refreshtoken"),
    path('logout/',EmployeeLogoutView.as_view(),name="logout"),
    path("profile/", EmployeeProfileView.as_view(), name="profile"),
    path("changepassword/", EmployeeChangePasswordView.as_view(), name="changepassword"),
    path('send-password-reset-email/', SendPasswordResetEmailView.as_view(), name="SendPasswordResetEmail"),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name="reset_password"),
    # path('scan/', scan_qr_code, name='scan_qr_code'),
    # path('generate-qr/', generate_qr_code, name='generate_qr_code'),
# scan_qr_code,generate_qr_code




]