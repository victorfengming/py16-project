from django.conf.urls import url
from . views import IndexViews,LoginViews


urlpatterns = [
    # 首页
    url(r'^$',IndexViews.myhome_index,name="myhome_index"),
    # 列表
    url(r'^list/$',IndexViews.myhome_list,name="myhome_list"),
    # 详情
    url(r'^info/$', IndexViews.myhome_info, name="myhome_info"),
    # 登录
    url(r'^login/$', LoginViews.myhome_login, name="myhome_login"),
    url(r'^dologin/$', LoginViews.myhome_dologin, name="myhome_dologin"),

    # 注册
    url(r'^register/$', LoginViews.myhome_register, name="myhome_register"),

    url(r'^doregister/$', LoginViews.myhome_doregister, name="myhome_doregister"),

    # 购物车 ,一套: 增 删 改 查

    # 订单 确认订单 提交订单, 订单支付

    # 个人中心 我的订单 个人信息 个人资料修改 地址管理


]

