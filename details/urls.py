from django.urls import path
from details import views
urlpatterns = [
    path('', views.home, name='home'),
    # LOAN REQUEST
    path('loan_request/', views.loan_request, name='loan_request'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('full_details/', views.full_details, name='full_details'),
    # path('approve/', vie,ws.approve, name='approve'),
    path('approve/<id>', views.approve, name='approve'),
    # path('approve/', views.approve, name='approve'),
]
