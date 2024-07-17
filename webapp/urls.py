from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from views.views import TokenRefreshView

from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings', views.bookings, name='bookings'),
    path('api/menu-items/', views.MenuItemViewSet.as_view({'get': 'list'})),
    path('api/menu-items/<int:pk>', views.MenuItemViewSet.as_view({'get': 'retrieve'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView, name='token_refresh'),
    path('api/cart/menu-items', views.cart, name='cart'),
    path('api/category', views.CategoriesView.as_view(), name='category'),
    path('api/featured', views.featured, name='featured'),
    path('api/delivery', views.assign_delivery, name='delivery'),
    path('api/groups/manager/users', views.managers),
    path('api/groups/manager/users/<str:id>', views.single_manager),
    path('api/groups/delivery-crew/users', views.delivery_crew),
    path('api/groups/delivery-crew/users/<str:id>', views.single_delivery_crew),
    path('api/orders', views.OrdersViewSet.as_view()),
    path('api/orders/<int:id>', views.single_order),
    path('api/register', views.register_user),
]