from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('preeclampsia1', views.preeclampsia, name='preeclampsia1'),
    path('base/', views.base, name='base'),
    # path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('news/', views.news, name='news'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('logout/', views.logout_view, name='logout'),
    path('add_edit_patient', views.add_edit_patient, name='add_edit_patient'),
    # path('login/', views.login, name='login'),

    path('login/', views.blog_view, name='blog'),
    path('generate/', views.generate_objects, name='generate'),

    path('database/', views.database, name='database'),
    path('users/register/', views.register, name='register'),
    path('users/login/', views.login_view, name='login'),
    path('users/correlation', views.correlation, name='correlation'),
    path('proba/', views.proba, name='proba'),
    # path('proba1/', views.simple_upload, name='proba1'),
    path('proba1/', views.proba1, name='proba1'),
    # path('proba2/', views.proba1, name='proba2')

    # path('users/correlation/', views.correlation, name='correlation'),

]