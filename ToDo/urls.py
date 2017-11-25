from django.conf.urls import url,include
from . import views

urlpatterns = [
url(r'^$',views.start),   
url(r'action',views.action,name="ToDoAction"),
url(r'delete/(?P<task_id>[0-9]+)',views.delete,name="DeleteTask")

]
