
from django.contrib import admin
from django.urls import path
from smsapp.views import home,create,delete,edit,update

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name="home"),
    path("create/",create,name="create"),
    path("delete/<int:id>",delete,name='delete'),
    path("edit/<int:id>",edit,name='edit'),
    path("update",update,name='update'),
]
