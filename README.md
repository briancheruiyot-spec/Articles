# 📰 Articles Project

A simple Python project that models relationships between Authors, Magazines, and Articles using **raw SQL with SQLite3** and **Object-Oriented Programming (OOP)**.

## 📁 Project Structure

Articles/
├── lib/
│ ├── db/
│ │ ├── articles.db
│ │ ├── schema.sql
│ │ └── seed.py
│ ├── models/
│ │ ├── author.py
│ │ ├── article.py
│ │ └── magazine.py
│ └── debug.py
├── scripts/
│ ├── setup_db.py
├── tests/
│ ├── test_author.py 
│ ├── test_article.py 
│ └── test_magazine.py 
├── .gitignore
├── README.md
└── Pipfile


---

## ✅ Features

- Define models with encapsulated database logic
- Raw SQL queries for CRUD operations
- Circular import-safe model structure
- Seeding & test scripts
- No external ORMs like SQLAlchemy

---

## 🔧 Setup

### 1. Install Python environment (if needed)

Use **pipenv** or a virtual environment:

pip install pipenv
pipenv shell

### Initialize the Database

PYTHONPATH=. python scripts/setup_db.py

This creates the necessary tables in lib/db/articles.db.

### Seed the Database

PYTHONPATH=. python lib/debug.py

## Author–Article–Magazine Relationship
- An Author can write many Articles.
- An Article belongs to one Author and one Magazine.
- A Magazine can have many Articles.

## Author
Brian cheruiyot
briancheruiyot6@gmail.com


