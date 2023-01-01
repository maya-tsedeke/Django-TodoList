from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from authorization.views import ( RegisterView, ChangePasswordView, UserLoginView)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='auth_register'),
    path('signin/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('changePassword/<key>/',ChangePasswordView.as_view(), name='auth_change_password'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
