from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializer import CarSerializer
from .models import Cars

# Create your views here.
class CarsView(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Cars.objects.all()

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        car = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(car)
        return Response(serializer.data)

    def get_category(self, request, category):
        queryset = Cars.objects.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list_ordered(self, request, order_by):
        queryset = Cars.objects.all()
        if order_by == "year_desc":
            queryset = queryset.order_by("-year")
        elif order_by == "year_asc":
            queryset = queryset.order_by("year")
        elif order_by == "price_desc":
            queryset = queryset.order_by("-price")
        elif order_by == "price_asc":
            queryset = queryset.order_by("price")
        else:
            queryset = queryset.order_by(order_by)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
