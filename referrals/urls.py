from django.urls import path
from . import views

app_name = 'referrals'

urlpatterns = [
    path('create/<int:patient_id>/', views.create_referral, name='create_referral'),
    path('<int:pk>/', views.referral_detail, name='referral_detail'),
    path('access/<str:access_code>/', views.referral_access, name='referral_access'),
    path('access/', views.referral_access_page, name='referral_access_page'),
    path('all_referrals/<int:patient_id>/', views.patient_referrals, name='patient_referrals'),
]
