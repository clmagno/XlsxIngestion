import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpreadsheetSerializer
from .models import create_dynamic_model

from django.core.management import call_command

class SpreadsheetUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SpreadsheetSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            table_name = serializer.validated_data['table_name']
            
            # Read the spreadsheet and get the column names
            df = pd.read_excel(file)
            columns = df.columns.tolist()
            
            # Create the dynamic model
            DynamicModel = create_dynamic_model(table_name, columns)
            
            # Create the table in the database
            call_command('makemigrations', 'myapp')
            call_command('migrate', 'myapp')
            
            # Insert the data into the database
            for index, row in df.iterrows():
                instance = DynamicModel(**{col: str(val) for col, val in row.items()})
                instance.save()
            
            return Response({"message": f"Data uploaded successfully to {table_name}"})
        else:
            return Response(serializer.errors, status=400)



        