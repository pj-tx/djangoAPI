from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import JD
from .serializers import ItemSerializer
from rest_framework import serializers, status
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_jds': '/',
        'Search by title': '/?title=title_name',
        'Search by location': '/?location=location_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/jd/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_jds(request):
    jd = ItemSerializer(data=request.data)
 
    # validating for already existing data
    if JD.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    print("running this data validation")
    print(jd)
    if jd.is_valid():
        jd.save()
        return Response(jd.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def view_items(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = JD.objects.filter(**request.query_params.dict())
    else:
        items = JD.objects.all()
 
    # if there is something in items else raise error
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)