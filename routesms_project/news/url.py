from django.conf.urls import url

from . import views
################NON GENERIC #############
# 
# urlpatterns = [
#      
#      url(r'^$', views.index, name='index'),
# #     url(r'^vote/$', views.vote, name='vote'),
#  #    url(r'^details/$', views.details, name='details'),
#  ]




################GENERIC #############

urlpatterns = [
    url(r'^signin/$', views.SignIn.as_view(), name='signin'),
    url(r'^register/$', views.SignUp.as_view(), name='signup'),
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^webkit_xls/$', views.WebkitXlsView.as_view(), name='webkitxls'),
    url(r'^webkit_xls/$', views.BankAccountView.as_view(), name='bankaccount'),
    url(r'^details/$', views.DetailView.as_view(), name='detail'),
    url(r'^result/$', views.ResultsView.as_view(), name='results'),
    url(r'^vote/$', views.vote, name='vote'),
]