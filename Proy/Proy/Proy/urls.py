"""
Definition of urls for Proy.
"""

from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from cuentas.views import SetPasswordView, ConsultaUltimosMovView, ConsultaDeudasView, UserDeleteView, CtaCteDeleteView, CtaCteDetailsView, CtaCteUpdateView, CtaCteMenuView, UserMenuView, UserUpdateView, UserRegistrationView, HomeView, TemplateView, NewCuentaCorrienteView
from cuentas import views

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='base.html'),name='home'),
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^menu-user/$', UserMenuView.as_view(), name='menu_usr'),
    url(r'^menu-ctacte/$', CtaCteMenuView.as_view(), name='menu_ctacte'),
    url(r'^new-user/$', UserRegistrationView.as_view(), name='user_registration' ),
    url(r'^update-user/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='user_update'),
    url(r'password/$', SetPasswordView.as_view(), name='change_password'),
    url(r'^eliminar-usr/(?P<pk>\d+)/$', UserDeleteView.as_view(), name='user_delete'),
    url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name= 'logout'),
    url(r'^nuevo-mov/$', NewCuentaCorrienteView.as_view(), name='nuevo_movimiento' ),
    url(r'^update-ctacte/(?P<pk>\d+)/$', CtaCteUpdateView.as_view(), name='ctacte_update'),
    url(r'^(?P<pk>\d+)/$', CtaCteDetailsView.as_view(),name='ctacte_detalle'),
    url(r'^eliminar-ctacte/(?P<pk>\d+)/$', CtaCteDeleteView.as_view(), name='ctacte_delete'),
    url(r'^consulta-deudas/$', ConsultaDeudasView.as_view(), name='consulta_deuda' ),
    url(r'^ultimos_movimientos/$', ConsultaUltimosMovView.as_view(), name='consulta_ultimos'),
    url(r'^admin/', include(admin.site.urls)),
]
