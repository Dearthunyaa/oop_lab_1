# Lab Overview  
This lab demonstrates how to load and analyze city temperature data from a CSV file using **Object-Oriented Programming (OOP)** concepts.  
You will learn to:  
- Use classes (`DataLoader`, `Table`) to organize code.  
- Apply **lambda** functions for filtering and aggregation.  
- Process and summarize data efficiently.  

---

# Project Structure  
- **`oop_lab_1/`** : Main directory for all files  
    - **`README.md`** : Overview and documentation for this lab  
    - **`Cities.csv`** : The dataset containing city, country, and temperature  
    - **`data_processing.py`** : Main Python script for data analysis  

---

# Design Overview  

## `DataLoader`  
Responsible for loading CSV data into a list of dictionaries.  

**Main Method:**  
- `load_csv(filename)` → Reads CSV file and returns rows as dictionaries.  

---

## `Table`  
Represents the data in a tabular form and allows data operations.  

**Main Methods:**  
- `filter(condition)` → Returns a new `Table` with rows that satisfy the given condition.  
- `aggregate(function, key)` → Applies a function (e.g., `sum`, `max`, `len`, custom lambda`) to a specified column.  

---

# Program Flow  
1. Load data from `Cities.csv` using `DataLoader`.  
2. Create a `Table` instance with the loaded data.  
3. Perform analyses such as:  
   - Finding the average temperature of all cities.  
   - Filtering cities by country or temperature threshold.  
   - Counting unique countries.  
   - Computing average or maximum temperature by country.  

---

# Design Notes  
- **Modular:** Each class has a single responsibility.  
- **Reusable:** Works for any CSV with similar structure.  
- **Extensible:** Can be expanded with new features (e.g., sorting, joining).  

---

# How to Test and Run  
Run the following command in the terminal:  
```
python data_processing.py
```

Expected output includes:  
- Average temperature of all cities.  
- Filtered lists of cities (e.g., Germany, Spain).  
- Unique country count.  
- Max and average temperature by country.  
