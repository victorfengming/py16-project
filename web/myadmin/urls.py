from django.conf.urls import url
from . views import IndexViews,UsersViews

urlpatterns = [
    url(r'^$',IndexViews.index,name="myadmin_index"),

    url(r'^user/add/$',UsersViews.user_add,name="myadmin_user_add"),
    url(r'^user/insert/$',UsersViews.user_insert,name="myadmin_user_insert"),
    url(r'^user/index/$',UsersViews.user_index,name="myadmin_user_index"),
    url(r'^user/edit/$',UsersViews.user_edit,name="myadmin_user_edit"),
    url(r'^user/setstatus/$',UsersViews.user_set_status,name="myadmin_user_set_status"),

]
