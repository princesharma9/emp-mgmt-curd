from django.urls import path
from . import views

urlpatterns = [
    path('empList', views.empList, name='empList'),
    # path('empAdd', views.empAdd, name='empAdd'),
    path('empRemove/<int:remove_id>/', views.empRemove, name='empRemove'),
    path('empEdit/<int:edit_id>/', views.empEdit, name='empEdit'),
]
