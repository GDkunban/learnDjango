from django.conf.urls import url
from . import views

urlpatterns = [
    # 实现查看
    url(r'^$', views.list_books),
    # 实现增加
    url(r'^add', views.new_book),
    # 实现修改
    url(r'^update/(\d+)', views.update),
    # 实现删除
    url(r'^del/(\d+)', views.delete),
]