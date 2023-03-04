from django.urls import path
from . import views

urlpatterns = [

    # Sets the url path to the home page TheCasualGardener_home.html.
    path('', views.TheCasualGardener_home, name="TheCasualGardener_home"),
    path('create_Record/', views.createRecord, name="create_Record"),
    path('list_basket/', views.list, name="list_basket"),
    path('<int:pk>/basket_details/', views.details, name="basket_details"),
    path('<int:pk>/basket_edit/', views.edit, name="basket_edit"),
    path('<int:pk>/basket_delete/', views.delete, name="basket_delete"),
    path('api/', views.my_api, name="tcg_api"),
]