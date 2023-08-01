from flask_base import TestFlaskBase
from flask import url_for

class TestHealthCheck(TestFlaskBase):
    def test_payload_healthcheck(self):
        expected = {'status': 'green'}
        response = self.client.get(url_for('healthcheck.liveness'))
        self.assertEqual(response.json, expected)