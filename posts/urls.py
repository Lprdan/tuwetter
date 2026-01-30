from django.urls import path
from .views import home, delete_post, toggle_like, notifications

urlpatterns = [
    path('home/', home, name='home'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
    path('notifications/', notifications, name='notifications'),
]
