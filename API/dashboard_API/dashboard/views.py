from .models import Team, CustomerContact, Invoice, Transactions, BarData, PieData, LineData
from .serializers import TeamSerializer, InvoiceSerializer, ContactsSerializer, TransactionSerializer, BarDataSerializer, PieDataSerializer, LineDataSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status


# Use the @api_view decorator to specify the accepted HTTP methods
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Invoice views
@api_view(['GET', 'POST'])
def invoice_list(request):
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# Customer Contact views
@api_view(['GET', 'POST'])
def customer_contacts_list(request):
    if request.method == 'GET':
        customer_contacts = CustomerContact.objects.all()
        serializer = ContactsSerializer(customer_contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def customer_contacts_detail(request, pk):
    try:
        customer_contacts = CustomerContact.objects.get(pk=pk)
    except CustomerContact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactsSerializer(customer_contacts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactsSerializer(customer_contacts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer_contacts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def transaction_list(request):
    if request.method == 'GET':
        transactions = Transactions.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction_detail(request, pk):
    try:
        transaction = Transactions.objects.get(pk=pk)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def bar_data_list(request):
    if request.method == 'GET':
        bar_data = BarData.objects.all()
        serializer = BarDataSerializer(bar_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BarDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bar_data_detail(request, pk):
    try:
        bar_data = BarData.objects.get(pk=pk)
    except BarData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BarDataSerializer(bar_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BarDataSerializer(bar_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bar_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def pie_data_list(request):
    if request.method == 'GET':
        pie_data = PieData.objects.all()
        serializer = PieDataSerializer(pie_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PieDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def pie_data_detail(request, pk):
    try:
        pie_data = PieData.objects.get(pk=pk)
    except PieData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PieDataSerializer(pie_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PieDataSerializer(pie_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pie_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def line_data_list(request):
    if request.method == 'GET':
        line_data = LineData.objects.all()
        serializer = LineDataSerializer(line_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LineDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def line_data_detail(request, pk):
    try:
        line_data = LineData.objects.get(pk=pk)
    except LineData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LineDataSerializer(line_data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LineDataSerializer(line_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        line_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

