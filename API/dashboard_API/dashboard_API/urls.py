"""
URL configuration for dashboard_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import team_list, team_detail, invoice_list, invoice_detail, customer_contacts_list, customer_contacts_detail, transaction_list, transaction_detail, bar_data_list, bar_data_detail, pie_data_list, pie_data_detail, line_data_list, line_data_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # URL pattern for listing and creating a team member
    path('teams/', team_list, name='team-list'),
    # URL pattern for retrieving, updating, and deleting a team member
    path('teams/<int:pk>/', team_detail, name='team-detail'),
    # URL pattern for listing and creating Invoices
    path('invoices/', invoice_list, name='invoice-list'),
    # URL pattern for retrieving, updating, and deleting an Invoice
    path('invoices/<int:pk>/', invoice_detail, name='invoice-detail'),
    # URL pattern for listing and creating Customer Contacts
    path('customer-contacts/', customer_contacts_list, name='customer-contacts-list'),
    # URL pattern for retrieving, updating, and deleting a Customer Contact
    path('customer-contacts/<int:pk>/', customer_contacts_detail, name='customer-contacts-detail'),
    # URL pattern for listing and creating a transaction
    path('transactions/', transaction_list, name='transaction-list'),
    # URL pattern for retrieving, updating, and deleting a transaction
    path('transactions/<int:pk>/', transaction_detail, name='transaction-detail'),
    # URL pattern for listing and creating a barchart
    path('BarData/', bar_data_list, name='BarData'),
    # URL pattern for retrieving, updating, and deleting a barchart data
    path('BarData/<int:pk>/', bar_data_detail, name='BarData-detail'),
    # URL pattern for listing and creating a piechart data
    path('PieData/', pie_data_list, name='PieData'),
    # URL pattern for retrieving, updating, and deleting a piechart data
    path('PieData/<int:pk>/', pie_data_detail, name='PieData-detail'),
    # URL pattern for listing and creating a line chart data
    path('LineData/', line_data_list, name='LineData'),
    # URL pattern for retrieving, updating, and deleting a line chart data
    path('LineData/<int:pk>/', line_data_detail, name='LineData-detail'),
]
