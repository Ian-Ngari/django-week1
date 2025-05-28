from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myapp'

urlpatterns = [
    # Main app URLs
    path('', views.food_list, name='food_list'),
    path('add/', views.add_food, name='add_food'),
    path('delete/<int:pk>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_calories, name='reset_calories'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='myapp:login'), name='logout'),  # Only this line changed
    path('signup/', views.signup, name='signup'),
]