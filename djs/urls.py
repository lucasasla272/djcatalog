from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'djs'

urlpatterns = [
    path('', views.dj_list, name='dj_list'),          # listado
    path('<int:pk>/', views.dj_detail, name='dj_detail'),  # detalle (pk = id del DJ)
    path('nuevo/', views.dj_create, name='dj_create'),
path('<int:pk>/editar/', views.dj_update, name='dj_update'),
path('<int:pk>/eliminar/', views.dj_delete, name='dj_delete'),
path('login/', auth_views.LoginView.as_view(template_name='djs/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]