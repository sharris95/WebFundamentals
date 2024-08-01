BookHaven Database and Web Fundamentals
Welcome to the "BookHaven" project and Web Fundamentals exploration! This repo contains my work on designing a relational database for a bookstore and practicing Python programming with web technologies. Below is a breakdown of what you'll find here and how to get started.

Contents
BookHaven Database Schema
Exploring Web Technologies and Python Programming
BookHaven Database Schema
Overview
In this part of the project, I created a database schema for a fictional bookstore called "BookHaven." The goal was to manage data about books, authors, customers, and transactions more efficiently.

Entity-Relationship Diagram (ERD)
The ERD shows how different tables in the database are connected. The main tables are:

Authors: Info about authors.
Books: Details of books, including which author wrote them.
Customers: Info about customers.
Transactions: Records of books bought by customers.
Database Schema
Here’s the schema I designed, including the columns and their data types:


Authors:

author_id (INT, PK): Unique ID for each author
name (VARCHAR(255)): Author's name
biography (TEXT): A short bio


Books:

book_id (INT, PK): Unique ID for each book
title (VARCHAR(255)): Title of the book
author_id (INT, FK): ID of the author (foreign key)
genre (VARCHAR(100)): Genre of the book
price (DECIMAL(10, 2)): Price of the book
publication_date (DATE): When the book was published
available (BOOLEAN): Whether the book is available


Customers:

customer_id (INT, PK): Unique ID for each customer
name (VARCHAR(255)): Customer's name
email (VARCHAR(255)): Customer's email address
phone (VARCHAR(20)): Customer's phone number


Transactions:

transaction_id (INT, PK): Unique ID for each transaction
book_id (INT, FK): ID of the book bought (foreign key)
customer_id (INT, FK): ID of the customer (foreign key)
transaction_date (DATE): Date of the transaction
quantity (INT): Number of books bought
total_price (DECIMAL(10, 2)): Total price paid

Exploring Web Technologies and Python Programming
Overview
This part of the project is about using Python to interact with web APIs and handle data. I created scripts to fetch data from public APIs and do some basic data processing.

Setup Instructions
Clone the Repo:

sh
git clone https://github.com/sharris95/DatabaseFundamentals.git
cd DatabaseFundamentals
Create and Activate a Virtual Environment:

On macOS and Linux:
sh
python3 -m venv env
source env/bin/activate

On Windows:
sh

python -m venv env
.\env\Scripts\activate
Install Required Packages:

sh
pip install requests beautifulsoup4
Scripts
Pokemon API Script (pokemon_api.py):

Description: This script gets data from the Pokémon API. It fetches and prints the names and abilities of certain Pokémon and calculates their average weight.
How to Run:
sh
python pokemon_api.py
Space API Script (space_api.py):

Description: This script fetches data about planets from a space API, prints their details, and finds the heaviest planet.
How to Run:
sh

python space_api.py
