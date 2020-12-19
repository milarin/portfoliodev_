from django.contrib import admin
from django.urls import path
from .views import WorkList, WorkDetail

urlpatterns = [
  path('admin/', admin.site.urls),
  path('list/', WorkList.as_view(), name='list'),
  path('detail/<int:pk>/', WorkDetail.as_view(), name='detail'),
]