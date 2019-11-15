# DriveFX PythonSDK

DriveFx SDK for Python. DriveFx is a stock managements, logistics and invoices platform. For more info about this see the website https://www.drivefx.net

### Install

```
pip install drivefx-python-sdk
```

### Use Invoices

```
from drivefx_python_sdk.invoice import InvoiceService, Product, Invoice, Costumer
backend_url = "*"
app_id = "*"
user_code ="*"
password = "*"

self.invoice_service = InvoiceService(backend_url=backend_url, app_id=app_id, user_code=user_code, password=password)
```

### Create Invoice

```
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
```

### Build and Publish

```
python setup.py sdist
twine upload dist/*
```
