import unittest
import json
from app import app

class MCPServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_mcp_store(self):
        data = {
            'key': 'value'
        }
        response = self.app.post('/mcp/store', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json['status'])

    def test_mcp_retrieve(self):
        data = {
            'key': 'value'
        }
        response = self.app.post('/mcp/retrieve', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('data', response.json)

    def test_mcp_search(self):
        data = {
            'query': 'search term'
        }
        response = self.app.post('/mcp/search', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('context', response.json)

if __name__ == '__main__':
    unittest.main()
