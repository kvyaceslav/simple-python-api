from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Category
from .serislizers import CategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    categories = Category.objects.filter(owner_id=request.user.id)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request, id):
    try:
        category = Category.objects.get(owner_id=request.user.id, id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add(request):
    request.data['owner'] = request.user.id
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update(request, id):
    try:
        category = Category.objects.get(owner_id=request.user.id, id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, id):
    try:
        category = Category.objects.get(owner_id=request.user.id, id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    category.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
