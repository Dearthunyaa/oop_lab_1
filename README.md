# OOP Programming Laboratory 3

## Lab Overview
This lab demonstrates how to build a simple mini-database system using Object-Oriented Programming (OOP).  
The program loads CSV files, stores them in tables, and supports operations such as filtering, aggregation, and joining — similar to a lightweight database implemented without SQL.

## Project Structure
- Cities.csv – city dataset  
- Countries.csv – country dataset  
- main.py – implementation of DataLoader, DB, and Table classes  
- README.md – documentation  

## Class Overview

### DataLoader
Purpose: Load CSV files into Python.  
Methods:
- `__init__()` – sets base directory  
- `load_csv()` – reads CSV file and returns list of dictionaries  

### DB
Purpose: Simple in-memory database for storing multiple tables.  
Methods:
- `insert()` – stores a Table object  
- `search()` – retrieves a table by name  

### Table
Purpose: Represent tabular data and provide operations.  
Methods:
- `filter()` – returns a new Table with rows matching a condition  
- `aggregate()` – applies an aggregation function to a column  
- `join()` – combines two tables using a shared key (if implemented)  
- `__str__()` – displays table contents  

## How to Run
```bash
1.Place Cities.csv and Countries.csv in the same folder as main.py
2.Run: python main.py
3.The program will display results from filtering, aggregation, and joining to confirm that the mini-database is working correctly.
