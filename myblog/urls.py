from django.urls import path
from myblog.views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="post_index"),
    path('myblog/<int:post_id>/', detail_view, name="post_detail"),
]