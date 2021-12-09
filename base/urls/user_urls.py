from django.urls import path
from base.views import user_views as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.register_user, name="register_user"),
    path('profile/', views.getUserProfile, name="users_profile"),
    path('profile/update/', views.updateUserProfile, name="user_profile_update"),
    path('', views.getUsers, name="get_users"),
]