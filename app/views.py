from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response

class ProductCrudVS(ViewSet):
    def list(self,request):
        SPO=Product.objects.all()
        SPD=ProductSerializer(SPO,many=True)
        return Response(SPD.data)

    def create(self,request):
        SD=ProductSerializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'Success':'Product Is Created'})
        return Response({'Failure':'Product is Not Created'})

    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO)
        return Response(SPD.data)
    
    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'Product Is Updated'})
        return Response({'Failure':'Product Is Not updated'})
    
    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'Product Is Updated'})
        return Response({'Failure':'Product Is Not updated'})
        
    def destroy(self,request,pk):
        SPO=Product.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product Is Deleted'})