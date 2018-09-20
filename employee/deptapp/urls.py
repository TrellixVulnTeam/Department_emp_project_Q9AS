from django.conf.urls import url
from . import views

app_name='deptapp'

urlpatterns = [
     url(r'^$', views.login, name='login'),
     url(r'^home/', views.home, name='home'),
     url(r'^logout/', views.logout, name='logout'),
     url(r'^add/', views.adddept, name='adddept'),
     url(r'^detail/(?P<dept_id>[0-9]+)/addemp/', views.add_emp, name='add_emp'),
     url(r'^detail/(?P<dept_id>[0-9]+)/deleteemp/(?P<emp_id>[0-9]+)/', views.delete_emp, name='delete_emp'),
     url(r'^detail/(?P<dept_id>[0-9]+)/', views.detail_dept, name='detail_dept'),
     url(r'^update/(?P<dept_id>[0-9]+)/', views.edit_dept, name='edit_dept'),
     url(r'^delete/(?P<dept_id>[0-9]+)/', views.delete_dept, name='delete_dept'),

]
