from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user-list', views.MyListMemberView.as_view(), name='administration_user_list'),
    path('user-detail', view.MyEditMemberDetailView.as_view(), name='administration_edit_user'),
    path('user_group', view.MyModifyTeamView.as_view(), name='administration_modify_group')
]