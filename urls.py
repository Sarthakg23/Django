from django.conf.urls import url
from main import views

urlpatterns = [

     url('signup/', views.signup),
     url('dashboard/', views.dashboard),
     url('login/', views.login),
     url('debit/',views.debit),
     url('credit/',views.credit),
     url('acc_state/',views.acc_state),
     url('transfer/',views.transfer),
    # url('b_login/',views.b_login),
     url('', views.Homepageview),

    ]