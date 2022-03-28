from math import prod
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products
# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        'api/routes',
        'api/products',
        'api/product',

    ]
    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    return Response(products)


@api_view(["GET"])
def getProduct(request, pk):
    product = None
    for i in products:
        if pk == i["_id"]:
            product = i

    return Response(product)
