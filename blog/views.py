from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CSPReportSerializer

def index(request):
    return render(request, "index.html")



class CSPReportView(APIView):
    def post(self, request):
        print("Request Headers:", request.headers)
        report_data = request.data.get('csp-report')
        if not report_data:
            return Response({"error": "No report data"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CSPReportSerializer(data=report_data)
        if serializer.is_valid():
            print("CSP Violation:", serializer.validated_data)
            return Response({"status": "Report received"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
