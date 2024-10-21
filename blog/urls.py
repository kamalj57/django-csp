from django.urls import path
from .views import CSPReportView,index
urlpatterns = [
    path('',index),
    path('csp-violation/', CSPReportView.as_view(), name='csp_report'),
]