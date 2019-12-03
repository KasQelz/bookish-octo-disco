from django.conf.urls import url
from . import views
app_name = 'Smash'

urlpatterns = [
    url('registrar', views.registrar, name='registrar'),
    url('login', views.login_usuario, name='login'),
    url('logout', views.logout_usuario, name='logout'),
    url('galeria', views.galeria, name='galeria'),
    url('contacto', views.contacto, name='contacto'),
    url('subir', views.subir, name='subir'),
    url('', views.index , name='index' ),
]
