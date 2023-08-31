from django.urls import path
from .views import ApplicationFormListCreateView, ApplicationFormRetrieveUpdateView,ApplicationNoView,DataExcelView

urlpatterns = [
    path('application-forms/no-of-student/',ApplicationNoView.as_view(),name='application-no-list'),
    path('application-forms/', ApplicationFormListCreateView.as_view(), name='application-form-list-create'),
    path('application-forms/<int:ar_number>', ApplicationFormRetrieveUpdateView.as_view(), name='application-form-retrieve-update'),
    path('application-forms/excel/',DataExcelView.as_view({'get':'export_to_excel'}),name = 'export_to_excel'),
]
# urlpatterns = [
#     path('application-forms/', PostView.as_view(), name='application-form-list-create'),
#     path('application-forms/<int:pk>/', ApplicationFormRetrieveUpdateView.as_view(), name='application-form-retrieve-update'),
# ]

