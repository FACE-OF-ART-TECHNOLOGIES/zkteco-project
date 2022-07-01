from django.urls import path 
from . import views

urlpatterns = [
    path('goto/<str:id>/', views.goto, name="goto"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('statistics/', views.statistics, name='statistics'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/summary/', views.atsummary, name='attendance-summary'),
    path('salary/', views.salary, name='salary'),
    path('salaryreports/', views.salaryreports, name='salaryreports'),
    path('payments/', views.payments, name="payments"),
    path('payapi/', views.payApi, name="payapi"),
    path('pay/', views.pay, name="pay"),
    path('api/marksalarypaid/', views.api_marka_salary_as_paid, name='marksalaryaspaid'),
    path('advancepayments/', views.advancepayments, name="advancepayments"), 
    path('advancereports/', views.advancereports, name="advancereports"),
    path('api/totalworkinghour/', views.totalapiworkinghour, name="apitotalworkinghour"),
    path('api/totalapiovertimehour/', views.totalapiovertimehour, name="totalapiovertimehour"),
    path('api/totalapimonthlyEarnings/', views.totalapimonthlyEarnings, name="totalapimonthlyEarnings")
]