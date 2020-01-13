import unittest
import json

from app.services.data_error_service import create_app
from app.model_auth.model import db, ReportModel

class ReportsTestCase(unittest.TestCase):
    report_id = 4
    data = {
        "created_at": "2017-11-23",
        "inventory": [
            {
                "name": "Flower pot",
                "price": "2.00"
            },
            {
                "name": "Roses, 24",
                "price": "50.00"
            }

        ],
        "organization": "Flowers Inc.",
        "reported_at": "2017-11-19"
    }

    def setUp(self):
        self.app = create_app('config')

        self.context = self.app.app_context()
        self.context.push()

        db.create_all()
        report_model = ReportModel(report_id=self.report_id, data=json.dumps(self.data))
        db.session.add(report_model)
        db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_home_page(self):
        rv = self.client.get('/')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.headers['Content-Type'], 'text/plain')
        self.assertEqual(rv.data, b'TEST application')

    def test_report_json(self):
        rv = self.client.get('/reports/4')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.headers['Content-Type'], 'application/json')

        data = json.loads(rv.data)
        self.assertTrue('organization' in data)
        self.assertTrue('reported_at' in data)
        self.assertTrue('created_at' in data)
        self.assertTrue('inventory' in data)

    def test_report_xml(self):
        rv = self.client.get('/reports/4?format=xml')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.headers['Content-Type'], 'application/xml')

    def test_report_pdf(self):
        rv = self.client.get('/reports/4?format=pdf')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.headers['Content-Type'], 'application/pdf')

    def test_report_not_found(self):
        rv = self.client.get('/reports/3')
        self.assertEqual(rv.status_code, 404)


if __name__ == '__main__':
    unittest.main()
