from behave import given
from your_project.models import Product  # Import your Product model

@given('I have the following products in the database')
def create_products(context):
    products_data=context.table
    for row in products_data:
        product=Product(
            name=row['name'],
            description=row['description'],
            price=row['price'],
            category=row['category'],
            availability=row['availability']
        )
        product.save()
