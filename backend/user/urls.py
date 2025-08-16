from django.urls import path
from .controllers import auth_controller

urlpatterns = [
    path('signup/', auth_controller.SignupAPIView.as_view(), name='signup'),
    path('login/',auth_controller.LoginAPIView.as_view(),name='login'),
    path('publicApi/',auth_controller.PublicAPIView.as_view(),name='publicapi'),
    path('protectedApi/',auth_controller.ProtectedAPIView.as_view(),name='protectedapi'),
]
