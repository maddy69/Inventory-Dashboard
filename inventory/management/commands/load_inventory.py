import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from inventory.models import Inventory

class Command(BaseCommand):
    help = 'Load inventory data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to load data from')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.exists(csv_file):
            self.stderr.write(self.style.ERROR(f"File '{csv_file}' does not exist"))
            return

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames  
            print(f"CSV Header: {header}")  

            required_columns = [
                'timestamp', 'description', 'title', 'brand', 'price',
                'product_type', 'custom_label_0', 'condition'
            ]
            
            for column in required_columns:
                if column not in header:
                    self.stderr.write(self.style.ERROR(f"Missing required column: {column}"))
                    return

            for row in reader:
                timestamp = row['timestamp']
                description = row['description']
                title = row['title']
                brand = row['brand']
                price_str = row['price']
                price = self.extract_price(price_str)
                product_type = row['product_type']
                custom_label_0 = row['custom_label_0']
                condition = row['condition']

                Inventory.objects.create(
                    timestamp=timestamp, 
                    description=description,
                    title=title,
                    brand=brand,
                    price=price,
                    product_type=product_type,
                    custom_label_0=custom_label_0,
                    condition=condition,
                )

        self.stdout.write(self.style.SUCCESS('Data successfully loaded'))

    def extract_price(self, price_str):
        try:
            price = float(''.join(filter(str.isdigit, price_str)))
        except ValueError:
            price = None  
        return price
