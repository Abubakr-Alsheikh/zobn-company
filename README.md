# Zobn Company - Product Catalog Website

![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css)
![Flowbite](https://img.shields.io/badge/Flowbite-2.5-06B6D4?style=for-the-badge&logo=flowbite)

This project is a fully functional product catalog website for "Zobn Company," built with Django. It features a public-facing site for customers to browse products and a secure dashboard for administrators to manage the inventory. The user interface is designed in Arabic, using Tailwind CSS and Flowbite for a modern and responsive layout.

## ✨ Features

### Public-Facing Site
- **Homepage**: Displays featured products to attract customers.
- **Product Listings**: A paginated gallery of all available products.
- **Product Details**: A dedicated page for each product with detailed information, including images, descriptions, prices, available sizes/colors, and processing time.
- **Contact Form**: Allows users to send general inquiries or messages related to a specific product.
- **Static Pages**: Includes "About Us" and "Product Care Guides".
- **Responsive Design**: Mobile-first design that looks great on all devices.

### Administrator Dashboard
- **Secure Authentication**: Login/logout system for authorized users.
- **Product Management (CRUD)**:
    - **Create**: Add new products with images and details.
    - **Read**: View a comprehensive list of all products.
    - **Update**: Edit existing product information.
    - **Delete**: Remove products from the catalog.
- **Message Viewing**: A section to view messages from customers (currently marked as under development).
- **User-Friendly Interface**: Built with Flowbite components for easy navigation and management.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, JavaScript
- **Styling**: Tailwind CSS, Flowbite
- **Database**: SQLite3 (for development)
- **Deployment**: WSGI
- **Tooling**: `npm` for frontend dependency management.

## 📁 Project Structure

The project follows a standard Django structure:

```
abubakr-alsheikh-zobn-company/
├── core/                  # Main Django app for all core logic
│   ├── models.py          # Database models (Product, Contact, etc.)
│   ├── views.py           # View logic for both public site and dashboard
│   ├── urls.py            # URL routing for the 'core' app
│   └── ...
├── static/                # Static files (CSS, JS, images)
│   ├── src/input.css      # Main Tailwind CSS source file
│   └── js/scripts.js      # Custom JavaScript
├── templates/             # HTML templates
│   ├── home/              # Public-facing pages
│   └── dashboard/         # Administrator dashboard pages
├── zobn_company/          # Django project configuration
│   ├── settings.py        # Project settings
│   └── urls.py            # Root URL configuration
├── manage.py              # Django's command-line utility
├── requirements.txt       # Python dependencies
└── package.json           # Frontend (npm) dependencies
```
