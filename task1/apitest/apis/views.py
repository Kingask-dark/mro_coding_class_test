from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from apitest.apis.serilaizers import LessionLearnSerilizer
from apitest.models import LessionList
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

class CustomePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10
    

class LessionListViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    pagination_class = CustomePagination
    
    @swagger_auto_schema(
        tags=['LessionListApi'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title'],
            properties={
                'title':openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    @action(detail=False,methods=["POST"])
    def get_lession(self,request):
        title = request.data.get('title')
        if not (title):
            return Response(
                {'detail': 'title is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            response = LessionList.objects.filter(title=title).first()
        
        except LessionList.DoesNotExist:
            return Response({'detail': 'Record not found.'}, status=status.HTTP_404_NOT_FOUND)

        serilizer = LessionLearnSerilizer(response)
        return Response(data=serilizer.data, status=status.HTTP_200_OK)