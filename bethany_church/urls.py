from django.contrib import admin
from django.urls import path
from attendance import views
from ministry.views import MinisterCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_member/', views.add_member, name='add_member'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('member_added_success/', views.add_member_success, name='success_url'),
    path('ministry_list/', views.ministry_list, name='ministry_list'),
    path('assign_minister/', views.AssignMinisterView.as_view(), name='assign_minister'	),
    path('attendance_success/', views.home, name='attendance_success'),
        path('members/<int:member_id>/details/', views.get_member_details, name='member-details'),
        path ('ministry_list/', views.ministry_list, name='ministry_list'),
path('ministers/add/', MinisterCreateView.as_view(), name='add_minister'),
    path('', views.home, name='home'),  
]
