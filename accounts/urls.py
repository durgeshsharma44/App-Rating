from django.urls import path
from .views import home, user_login, admin_login, register, dashboard, admin_dashboard, logout_user, upload_screenshot

urlpatterns = [
    path('user/login/', user_login, name='user_login'),
    path('admin/login/', admin_login, name='admin_login'),
    path('', home, name="home"),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('logout/', logout_user, name='logout'),
    path('upload_screenshot/<int:app_id>/', upload_screenshot, name='upload_screenshot'),
]
