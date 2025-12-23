# Python Full Stack - COAPPS

# Project Details
- PROJECT TITLE      : Retail E-commerce
- BRAND NAME         : MultiZone



# Setup

## Environment Variables
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` file and set your configuration values:
   - Generate a secure SECRET_KEY for production
   - Set DEBUG=False for production
   - Configure ALLOWED_HOSTS with your domain
   - Set up database credentials

## Local Development (SQLite)
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   cd ecommerce
   python manage.py migrate
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Docker Development (MySQL)
1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Run migrations in the container:
   ```bash
   docker-compose exec web python ecommerce/manage.py migrate
   ```

# Project Description: 
In this internship project, We are developing a retail e-commerce platform using Python full stack technologies. The project aims to create a robust and user-friendly online shopping experience, incorporating features such as product catalog management, user authentication, shopping cart functionality, and secure payment processing. 

# Technologies Used
1. Python Django
2. HTML
3. CSS
4. JavaScript
5. MySQL

# Output
<img width="100%" src="./HomePage.png">
