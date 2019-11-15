import unittest
from drivefx_python_sdk.invoice import InvoiceService, Invoice, Product, Costumer

class HiPayTest(unittest.TestCase):
    def setUp(self):
        backend_url = "*"
        app_id = "*"
        user_code ="*"
        password = "*"

        self.invoice_service = InvoiceService(backend_url=backend_url, app_id=app_id, user_code=user_code, password=password)

    def tearDown(self):
        pass

    def testAuth(self):

        output = self.invoice_service.auth()

        self.assertIsNotNone(output)

    def testCreateInvoice(self):

        costumer = Costumer(
            name="teste",
            email="mail@mail.com",
            tax_number="243649371",
            address="Test address",
            postal_code="2900-616",
            city="Setubal"
        )

        product1 = Product(
            reference="C021",
            designation="product teste",
            unit_price=10
        )

        products = [product1]

        invoice = Invoice(costumer=costumer, products=products)

        invoice = self.invoice_service.create_invoice(invoice=invoice)

        self.assertIsNotNone(invoice)
        self.assertIn("pdf", invoice)


