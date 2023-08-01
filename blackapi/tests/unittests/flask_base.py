from unittest import TestCase
from blackapi import create_app
from flask import url_for


class TestFlaskBase(TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
    
    def test_payload_healthcheck(self):
        expected = {'status': 'green'}
        response = self.client.get(url_for('healthcheck.liveness'))
        self.assertEqual(response.json, expected)