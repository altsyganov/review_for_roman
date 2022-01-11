from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
# from .views import ProductView, PriceView, TypeView
from . import api

router = DefaultRouter()
router.register('product', api.ProductViewSet)
router.register('price', api.PriceViewSet)
router.register('type', api.TypeViewSet)




app_name = "Shop"

urlpatterns = [
    path('', include(router.urls))
    # path('product/', views.ProductViewSet.as_view()),
    # path('price/', PriceView.as_view()),
    # path('type/', TypeView.as_view()),
    # path('product/<int:pk>', ProductView.as_view()),
    # path('price/<int:pk>', PriceView.as_view()),
    # path('type/<int:pk>', TypeView.as_view())
]