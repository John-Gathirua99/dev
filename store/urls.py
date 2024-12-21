from django.urls import path
from . import views
from .views import ProductDetail
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('product/<int:pk>/',ProductDetail.as_view(),name='product'),
    path('product/<str:foo>/',views.category,name='category')
]