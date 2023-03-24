# bookapp
An e-commerce web app for selling books. Built with Python and Django

This GitHub repository provides an e-commerce bookstore store web application built with Django and Python.

## Features

The app provides the following features:

* Authentication and authorization
* CRUD features like:
  * Adding books to cart
  * Updating cart
  * Deleting products from cart
  * Viewing cart
* Searching for books based on author name, title and category
* Payment integration system with Paystack
* Email confirmation of order

## Requirements

The app requires the following to be installed:

* Python 3.x
* Django 3.x
* Paystack API

## Installation

To install the app, simply clone the repository:

`git clone https://github.com/kerry407/bookapp.git`

Create a virtual environment for the Django app:

 `python3 -m venv my_env`

Activate the virtual environment:

`source my_env/bin/activate`

Change into the cloned repository:

`cd bookapp`

After navigating to the repository folder, run the following command to install the requirements:

`pip install -r requirements.txt`

Run migrations to create the app's database:

`python manage.py migrate`

Create a superuser for the app:

`python manage.py createsuperuser`

## Usage

To use the app, simply run the following command:

`python manage.py runserver`

Once the server is running, you can access the app at `http://localhost/`
