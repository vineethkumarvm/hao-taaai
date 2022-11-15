from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name = "home"),
    path('about/',views.about,name = "about"),
    path('job/',views.job, name = "job"),
    path('job/<int:id>',views.job, name = "jobi"),
    path('crptojob/<int:id>',views.crptojob, name = "crptojob"),
    # path('login/',views.login,name = "login"),
    # path('signup/',views.signup,name = "signup"),
]