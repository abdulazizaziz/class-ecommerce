from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from .serializers import *
from .models import *


class LinksView(APIView):
    def get(self, request):
        data = {
            "Categories": "http://localhost:8000/api/categories/",
            "Brands": "http://localhost:8000/api/brands/",
        }
        return Response(data)

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryItemView(APIView):
    def get(self, request, id):
        category = Category.objects.filter(id=id).first()
        if category:
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        return Response({"detail": 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        category = Category.objects.filter(id=id).first()
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def delete(self, request, id):
        category = Category.objects.filter(id=id).first()
        if category:
            category.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response({"detail": 'Not found'}, status=status.HTTP_404_NOT_FOUND)




class BrandView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=400)

        return Response(serializer.data, status=201)
    
    
    

class BrandItemView(APIView):
    def get(self, request, id):
        brand = Brand.objects.filter(id=id).first()
        if brand:
            serializer = BrandSerializer(brand)
            return Response(serializer.data)
        return Response({"detail": 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        brand = Brand.objects.filter(id=id).first()
        if "name" in request.data:
            brand.name = request.data['name']
        if "country" in request.data:
            brand.country = request.data['country']
        brand.save()
        serializer = BrandSerializer(instance=brand)
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id):
        brand = Brand.objects.filter(id=id).first()
        if brand:
            brand.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response({"detail": 'Not found'}, status=status.HTTP_404_NOT_FOUND)

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class BrandViewSet(ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


# class ProductViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
class ProductViewSet(ModelViewSet):
    # serializer_class = ProductSerializer
    queryset = Product.objects.select_related('brand', 'category').prefetch_related('variants').all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductPostSerializer