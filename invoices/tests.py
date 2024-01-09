from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Invoice

class InvoiceTests(APITestCase):
    def test_create_invoice(self):
        """
        Ensure we can create a new invoice.
        """
        url = reverse('invoice-list')
        data = {'date': '2022-01-01', 'customer_name': 'John Doe', 'details': [{'description': 'Service', 'quantity': 1, 'unit_price': 100, 'price': 100}]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'John Doe')
        
    # Add more test cases for update, retrieve, delete, etc.

