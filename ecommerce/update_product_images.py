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

def update_product_images():
    print("Updating product images...")

    # Define image mappings for products
    image_mappings = {
        # Shoes
        'Nike Revolution 6': 'uploads/240419111656Nike_Revolution.jpg',
        'Puma Flex Run': 'uploads/240419111830Puma_Black.jpg',
        'Adidas Ultraboost': 'uploads/240416181003f1.jpg',
        'White Sports Shoe': 'uploads/240419110604White_Shoe.jpg',
        'Nike Flex Run 11': 'uploads/240419111625Nike_Flex_Run11.jpg',

        # Shirts
        'White Formal Shirt': 'uploads/240419114631White_Shirt.jpg',
        'Black Formal Shirt': 'uploads/240419114529Black_Shirt.jpg',
        'Yellow Casual Shirt': 'uploads/240419114604Yellow_Shirt.jpg',
        'Ash Grey Shirt': 'uploads/240419114450Ash_Grey_Shirt.jpg',
        'Coffee Striped Shirt': 'uploads/240419115151Coffee_Striped.jpg',

        # T-Shirts
        'Marathon T-Shirt': 'uploads/240419112527Marathon_T-Shirt.jpg',
        'Vibes T-Shirt': 'uploads/240419112539Vibes_T-Shirt.jpg',
        'Spiritual T-Shirt': 'uploads/240419112555Spiritual_T-Shirt.jpg',
        'Run T-Shirt': 'uploads/240419112612Run_T-Shirt.jpg',
        'Graphic T-Shirt': 'uploads/240419170948graphic-shirt-trendy-design-mockup.jpg',

        # Mobile Phones
        'Redmi 12': 'uploads/240419111212Redmi_12.jpg',
        'Redmi Note 12': 'uploads/240419111242Redmi_Note_12.jpg',
        'Poco X4': 'uploads/240419111123Poco_X4.jpg',
        'Oppo A16k': 'uploads/240419110942Oppo_A16k.jpg',
        'Oppo': 'uploads/240419111038Oppo.jpg',
        'Motorola Edge 40': 'uploads/240419110849Motorola_Edge_40.jpg',
        'Samsung Galaxy': 'uploads/240419111319Samsung_Galaxy.jpg',

        # Laptops
        'Apple Macbook Pro 2023': 'uploads/240420133955Apple_Macbook_Pro_2023.jpg',
        'Apple Macbook 2022': 'uploads/240420133858Apple_Macbook_2022.jpg',
        'ASUS TUF Gaming F15': 'uploads/240420134057ASUS_TUF_Gamming_F15.jpg',
        'ASUS TUF Gaming': 'uploads/240420134150ASUS_TUF_Gamming.jpg',
        'Lenovo IdeaPad 3': 'uploads/240420134339Lenovo_Idea_pad_3.jpg',
        'Lenovo IdeaPad Slim 3': 'uploads/240420134432Lenovo_Ideapad_slim_3.jpg'
    }

    # Update products with images
    for product_name, image_path in image_mappings.items():
        try:
            product = Products.objects.get(name=product_name)
            # Create a file-like object for the image path
            from django.core.files.base import ContentFile
            from django.core.files.storage import default_storage

            # Since we can't easily copy files in this context, let's just set the image path
            # In a real scenario, you'd copy the file to the media directory
            # For now, we'll just set the image name to simulate having an image
            product.product_image.name = image_path
            product.save()
            print(f"Updated image for: {product_name}")
        except Products.DoesNotExist:
            print(f"Product not found: {product_name}")
        except Exception as e:
            print(f"Error updating {product_name}: {e}")

    print("Product image update completed!")
    print(f"Total products with images: {Products.objects.exclude(product_image='').count()}")

if __name__ == '__main__':
    update_product_images()
