from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.admin_home,name="admin_home"),
    path('addshow/',views.add_show,name="add_show"),
    path('<int:id>/',views.update_data,name="updatedata"),
    path('<int:id>/',views.update_data_inter,name="updatedatas"),
    path('delete/<int:id>/',views.delete_data,name="deletedata"),
    path('delete/<int:id>/',views.delete_data_inter,name="deletedatas"),
]