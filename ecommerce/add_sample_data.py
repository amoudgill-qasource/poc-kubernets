#!/usr/bin/env python
import os
import django
import sys

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

# Setup Django
django.setup()

from eshop.models import Category, Products

def add_sample_data():
    print("Checking existing data...")

    # Check existing categories and products
    categories_count = Category.objects.count()
    products_count = Products.objects.count()

    print(f"Existing Categories: {categories_count}")
    print(f"Existing Products: {products_count}")

    if categories_count == 0:
        print("Adding sample categories...")

        # Create categories
        categories_data = [
            {
                'name': 'Shoes',
                'description': 'Comfortable and stylish footwear for all occasions',
                'status': 0,
                'trending': 1
            },
            {
                'name': 'Shirts',
                'description': 'Casual and formal shirts for men and women',
                'status': 0,
                'trending': 1
            },
            {
                'name': 'T-Shirts',
                'description': 'Trendy t-shirts with various designs and colors',
                'status': 0,
                'trending': 1
            },
            {
                'name': 'Mobile Phones',
                'description': 'Latest smartphones from top brands',
                'status': 0,
                'trending': 1
            },
            {
                'name': 'Laptops',
                'description': 'High-performance laptops for work and gaming',
                'status': 0,
                'trending': 0
            }
        ]

        for cat_data in categories_data:
            category = Category.objects.create(**cat_data)
            print(f"Created category: {category.name}")

    # Always recreate products to ensure they have images
    print("Recreating sample products with images...")
    Products.objects.all().delete()

    # Get categories
    shoes_cat = Category.objects.get(name='Shoes')
    shirts_cat = Category.objects.get(name='Shirts')
    tshirts_cat = Category.objects.get(name='T-Shirts')
    mobiles_cat = Category.objects.get(name='Mobile Phones')
    laptops_cat = Category.objects.get(name='Laptops')

    # Sample products data
    products_data = [
        # Shoes
        {
            'category': shoes_cat,
            'name': 'Nike Revolution 6',
            'vendor': 'Nike',
            'product_image': 'uploads/240419111656Nike_Revolution.jpg',
            'quantity': 50,
            'original_price': 5000,
            'selling_price': 4500,
            'description': 'Running shoes with advanced cushioning and support',
            'status': 0,
            'trending': 1
        },
        {
            'category': shoes_cat,
            'name': 'Puma Flex Run',
            'vendor': 'Puma',
            'product_image': 'uploads/240419111830Puma_Black.jpg',
            'quantity': 30,
            'original_price': 4000,
            'selling_price': 3500,
            'description': 'Lightweight running shoes with flexible sole',
            'status': 0,
            'trending': 1
        },
            {
                'category': shoes_cat,
                'name': 'Adidas Ultraboost',
                'vendor': 'Adidas',
                'product_image': 'uploads/240416181003f1.jpg',
                'quantity': 25,
                'original_price': 8000,
                'selling_price': 7200,
                'description': 'Premium running shoes with Boost technology',
                'status': 0,
                'trending': 1
            },
            {
                'category': shoes_cat,
                'name': 'White Sports Shoe',
                'vendor': 'MultiZone',
                'quantity': 40,
                'original_price': 3000,
                'selling_price': 2500,
                'description': 'Classic white sports shoes for everyday wear',
                'status': 0,
                'trending': 0
            },
            {
                'category': shoes_cat,
                'name': 'Nike Flex Run 11',
                'vendor': 'Nike',
                'quantity': 35,
                'original_price': 5500,
                'selling_price': 4800,
                'description': 'Next generation running shoes with enhanced flexibility',
                'status': 0,
                'trending': 1
            },

            # Shirts
            {
                'category': shirts_cat,
                'name': 'White Formal Shirt',
                'vendor': 'MultiZone',
                'quantity': 60,
                'original_price': 2000,
                'selling_price': 1800,
                'description': 'Classic white formal shirt perfect for office wear',
                'status': 0,
                'trending': 0
            },
            {
                'category': shirts_cat,
                'name': 'Black Formal Shirt',
                'vendor': 'MultiZone',
                'quantity': 45,
                'original_price': 2200,
                'selling_price': 1900,
                'description': 'Elegant black formal shirt for professional look',
                'status': 0,
                'trending': 0
            },
            {
                'category': shirts_cat,
                'name': 'Yellow Casual Shirt',
                'vendor': 'MultiZone',
                'quantity': 30,
                'original_price': 1800,
                'selling_price': 1500,
                'description': 'Bright yellow casual shirt for weekend outings',
                'status': 0,
                'trending': 0
            },
            {
                'category': shirts_cat,
                'name': 'Ash Grey Shirt',
                'vendor': 'MultiZone',
                'quantity': 25,
                'original_price': 1900,
                'selling_price': 1600,
                'description': 'Stylish ash grey shirt with modern design',
                'status': 0,
                'trending': 0
            },
            {
                'category': shirts_cat,
                'name': 'Coffee Striped Shirt',
                'vendor': 'MultiZone',
                'quantity': 35,
                'original_price': 2100,
                'selling_price': 1800,
                'description': 'Coffee colored striped shirt for casual wear',
                'status': 0,
                'trending': 0
            },

            # T-Shirts
            {
                'category': tshirts_cat,
                'name': 'Marathon T-Shirt',
                'vendor': 'MultiZone',
                'product_image': 'uploads/240419112527Marathon_T-Shirt.jpg',
                'quantity': 80,
                'original_price': 800,
                'selling_price': 650,
                'description': 'Comfortable cotton t-shirt for running and fitness',
                'status': 0,
                'trending': 1
            },
            {
                'category': tshirts_cat,
                'name': 'Vibes T-Shirt',
                'vendor': 'MultiZone',
                'product_image': 'uploads/240419112539Vibes_T-Shirt.jpg',
                'quantity': 70,
                'original_price': 750,
                'selling_price': 600,
                'description': 'Trendy vibes t-shirt with cool design',
                'status': 0,
                'trending': 1
            },
            {
                'category': tshirts_cat,
                'name': 'Spiritual T-Shirt',
                'vendor': 'MultiZone',
                'quantity': 50,
                'original_price': 850,
                'selling_price': 700,
                'description': 'Spiritual themed t-shirt with meaningful design',
                'status': 0,
                'trending': 0
            },
            {
                'category': tshirts_cat,
                'name': 'Run T-Shirt',
                'vendor': 'MultiZone',
                'quantity': 65,
                'original_price': 780,
                'selling_price': 620,
                'description': 'Lightweight running t-shirt for athletes',
                'status': 0,
                'trending': 1
            },
            {
                'category': tshirts_cat,
                'name': 'Graphic T-Shirt',
                'vendor': 'MultiZone',
                'quantity': 40,
                'original_price': 900,
                'selling_price': 750,
                'description': 'Trendy graphic t-shirt with modern artwork',
                'status': 0,
                'trending': 1
            },

            # Mobile Phones
            {
                'category': mobiles_cat,
                'name': 'Redmi 12',
                'vendor': 'Xiaomi',
                'quantity': 20,
                'original_price': 15000,
                'selling_price': 13500,
                'description': 'Latest Redmi smartphone with advanced features',
                'status': 0,
                'trending': 1
            },
            {
                'category': mobiles_cat,
                'name': 'Redmi Note 12',
                'vendor': 'Xiaomi',
                'quantity': 15,
                'original_price': 18000,
                'selling_price': 16000,
                'description': 'Note series smartphone with large display',
                'status': 0,
                'trending': 1
            },
            {
                'category': mobiles_cat,
                'name': 'Poco X4',
                'vendor': 'Xiaomi',
                'quantity': 18,
                'original_price': 20000,
                'selling_price': 17500,
                'description': 'Gaming smartphone with high performance',
                'status': 0,
                'trending': 1
            },
            {
                'category': mobiles_cat,
                'name': 'Oppo A16k',
                'vendor': 'Oppo',
                'quantity': 12,
                'original_price': 12000,
                'selling_price': 10500,
                'description': 'Budget smartphone with good camera',
                'status': 0,
                'trending': 0
            },
            {
                'category': mobiles_cat,
                'name': 'Oppo',
                'vendor': 'Oppo',
                'quantity': 10,
                'original_price': 25000,
                'selling_price': 22000,
                'description': 'Premium Oppo smartphone with flagship features',
                'status': 0,
                'trending': 1
            },
            {
                'category': mobiles_cat,
                'name': 'Motorola Edge 40',
                'vendor': 'Motorola',
                'quantity': 8,
                'original_price': 30000,
                'selling_price': 27000,
                'description': 'Edge series smartphone with curved display',
                'status': 0,
                'trending': 1
            },
            {
                'category': mobiles_cat,
                'name': 'Samsung Galaxy',
                'vendor': 'Samsung',
                'quantity': 6,
                'original_price': 35000,
                'selling_price': 32000,
                'description': 'Samsung Galaxy series with premium features',
                'status': 0,
                'trending': 1
            },

            # Laptops
            {
                'category': laptops_cat,
                'name': 'Apple Macbook Pro 2023',
                'vendor': 'Apple',
                'quantity': 5,
                'original_price': 150000,
                'selling_price': 140000,
                'description': 'Professional MacBook Pro with M3 chip',
                'status': 0,
                'trending': 1
            },
            {
                'category': laptops_cat,
                'name': 'Apple Macbook 2022',
                'vendor': 'Apple',
                'quantity': 7,
                'original_price': 120000,
                'selling_price': 110000,
                'description': 'MacBook with M2 chip for everyday use',
                'status': 0,
                'trending': 1
            },
            {
                'category': laptops_cat,
                'name': 'ASUS TUF Gaming F15',
                'vendor': 'ASUS',
                'quantity': 10,
                'original_price': 80000,
                'selling_price': 75000,
                'description': 'Gaming laptop with high-end graphics',
                'status': 0,
                'trending': 1
            },
            {
                'category': laptops_cat,
                'name': 'ASUS TUF Gaming',
                'vendor': 'ASUS',
                'quantity': 8,
                'original_price': 90000,
                'selling_price': 82000,
                'description': 'Advanced gaming laptop with RGB keyboard',
                'status': 0,
                'trending': 1
            },
            {
                'category': laptops_cat,
                'name': 'Lenovo IdeaPad 3',
                'vendor': 'Lenovo',
                'quantity': 12,
                'original_price': 45000,
                'selling_price': 40000,
                'description': 'Budget laptop for students and professionals',
                'status': 0,
                'trending': 0
            },
            {
                'category': laptops_cat,
                'name': 'Lenovo IdeaPad Slim 3',
                'vendor': 'Lenovo',
                'quantity': 15,
                'original_price': 55000,
                'selling_price': 48000,
                'description': 'Slim and lightweight laptop for portability',
                'status': 0,
                'trending': 0
            }
        ]

        for prod_data in products_data:
            product = Products.objects.create(**prod_data)
            print(f"Created product: {product.name}")

    print("Sample data addition completed!")
    print(f"Final count - Categories: {Category.objects.count()}, Products: {Products.objects.count()}")

if __name__ == '__main__':
    add_sample_data()
