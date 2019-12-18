from django.urls import path
from details import views
urlpatterns = [
    path('', views.home, name='home'),
    # LOAN REQUEST
    path('loan_request/', views.loan_request, name='loan_request'),
    # user wise detail
    path('user_detail/', views.user_detail, name='user_detail'),
    # full details for admin
    path('full_details/', views.full_details, name='full_details'),
    # approve loan
    path('approve/<id>', views.approve, name='approve'),
]
