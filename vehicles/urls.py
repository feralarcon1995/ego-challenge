from django.urls import path, include
from rest_framework import routers
from vehicles import views

router = routers.DefaultRouter()
router.register(r'cars', views.CarsView, 'cars')

urlpatterns = [
    path('', include(router.urls)),
    path('cars/category/<str:category>/', views.CarsView.as_view({'get': 'get_category'}), name='category-detail'),
    path('cars/ordered-by/<str:order_by>/', views.CarsView.as_view({'get': 'list_ordered'}), name='list-ordered'),
]
