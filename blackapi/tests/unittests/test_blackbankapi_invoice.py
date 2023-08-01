from flask_base import TestFlaskBase
from flask import url_for

class TestInvoice(TestFlaskBase):
    def test_create_invoices_without_required_fields(self):
        file = "blackapi/csv_sample/wrong_csv_example.csv"
        data = {
            'file': (open(file, 'rb'), file)
        }
        expected = {'status': 'Fields not found'}
        response = self.client.post(url_for('invoice.create'), data=data)
        self.assertEqual(response.json, expected)

    def test_create_invoices_without_csv_file(self):
        expected = {'status': 'File not found in this request'}
        response = self.client.post(url_for('invoice.create'))
        self.assertEqual(response.json, expected)

    def test_create_invoices_with_required_fields(self):
        file = "blackapi/csv_sample/csv_example.csv"
        data = {
            'file': (open(file, 'rb'), file)
        }
        expected = {"status": "processed"}
        response = self.client.post(url_for('invoice.create'), data=data)
        self.assertEqual(response.json, expected)