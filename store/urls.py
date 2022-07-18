from django.urls import path
from .views import RegisterView, LoginView, UserView,LogoutView
from django.conf.urls import include
from . import views



urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('items', views.ItemList.as_view(), name='item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('comments', views.CommentList.as_view(), name='comment_list' ),
    path('comment/<int:pk>', views.CommentDetail.as_view(), name='comment_detail'),
    path('cartItemList/<int:pk>', views.CartItemDetail.as_view(), name='cartItem_list'),
    path('carts', views.CartList.as_view(), name='cart_list'),
]
