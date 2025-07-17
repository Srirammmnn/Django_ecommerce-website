from django.urls import path
from . import views

urlpatterns= [

    path('',views.index, name='index'),
    path('login/',views.user_login,name='login'),
    path('sign/',views.sign,name='sign'),
    path('contact/',views.contact,name='contact'),
    path('product/<int:pk>',views.product,name='product'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout_user,name='logout'),
    path('search/',views.search,name='search'),
    # path('cart/',views.cart_view,name='cart'),

]