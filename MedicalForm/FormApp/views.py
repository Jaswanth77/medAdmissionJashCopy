from rest_framework import generics,viewsets
from .models import ApplicationFormModel
from .serializers import ApplicationModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


# #imports for the excel view
# from rest_framework.viewsets import ReadOnlyModelViewSet
# from drf_excel.mixins import XLSXFileMixin
# from drf_excel.renderers import XLSXRenderer

#imports for export to excel
import pandas as pd
from io import BytesIO
from django.http import HttpResponse

#creating application view
class ApplicationFormListCreateView(generics.ListCreateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            None
        print(serializer.errors)  # Print the errors to the console
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(list(ApplicationFormModel.objects.all())[-1].ar_number)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
#application details fetching and updation view
class ApplicationFormRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer
    lookup_field = "ar_number"

    def update(self, request, *args, **kwargs):
        print("yess")
        try:
            instance = ApplicationFormModel.objects.get(ar_number=kwargs['ar_number'])
            serializer = ApplicationModelSerializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            print(instance.ar_number)
            print(serializer.errors)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        

#fetching the last application number view
class ApplicationNoView(generics.RetrieveAPIView):
    def get(self,request,*args,**kwargs):
        data = list(ApplicationFormModel.objects.all())
        if (len(data)==0):
            print("ar no:0")
            return Response(0,status.HTTP_200_OK)
        else:
            ar_no = data[-1].ar_number
            print("the no. of student data inside the db is:"+str(ar_no))
            return Response(ar_no,status=status.HTTP_200_OK)

class DataExcelView(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicationFormModel.objects.all()
    serializer_class = ApplicationModelSerializer
    

    def export_to_excel(self,request):

        # fetch data and store in pandas data frame
        queryset = self.get_queryset()
        serializer = ApplicationModelSerializer(queryset,many=True)
        df = pd.DataFrame(serializer.data)

        #create an excel file from data frame
        excel_file  = BytesIO()
        df.to_excel(excel_file,index=False,engine='xlsxwriter')
        excel_file.seek(0)

        #prepare the response with the excel file
        response = HttpResponse(excel_file.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=application_data.xlsx'
        print("request done")
        return response

# class ExcelView(XLSXFileMixin,ReadOnlyModelViewSet):
#     queryset = ApplicationFormModel.objects.all()
#     serializer_class = ApplicationModelSerializer
#     renderer_classes = (XLSXRenderer,)
#     filename = 'ApplicationData.xlsx'


# class PostView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         posts = ApplicationFormModel.objects.all()
#         serializer = ApplicationModelSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
        
#         posts_serializer = ApplicationModelSerializer(data=request.data)
#         print("asdfasdf")
#         if posts_serializer.is_valid():
#             print(posts_serializer.errors)
#             posts_serializer.save()
            
#             return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', posts_serializer.errors)
#             return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)