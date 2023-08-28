from django.urls import path, include
from products.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('brands', BrandViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', LinksView.as_view()),
    # path('categories/', CategoryView.as_view()),
    # path('brands/', BrandView.as_view()),
    # path('categories/<int:id>/', CategoryItemView.as_view()),
    # path('brands/<int:id>/', BrandItemView.as_view()),
]


