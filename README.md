# E-Commerce Data Analytics Project

## Overview

This project presents an end-to-end data analytics workflow using PostgreSQL and Python.  
The goal is to extract meaningful insights from an e-commerce dataset through structured queries, data processing, and visualization.

The project demonstrates how raw transactional data can be transformed into actionable business insights.

---

## Objectives

- Analyze customer behavior and purchasing patterns
- Identify top-performing product categories
- Evaluate delivery performance across regions
- Understand revenue trends over time
- Build visual reports for decision-making

---

## Technologies Used

- **Database:** PostgreSQL (pgAdmin)
- **Programming:** Python
- **Libraries:**
  - pandas
  - matplotlib
  - plotly
  - sqlalchemy
  - psycopg2
  - openpyxl

---

## Project Structure


project-root/
│
├── sql/
│ ├── schema.sql
│ ├── queries.sql
│
├── src/
│ ├── main.py
│ ├── analytics.py
│
├── charts/
├── exports/
│ └── mercadoinsights_report.xlsx
│
├── requirements.txt
└── README.md


---

## Data Source

The dataset is based on a real-world e-commerce dataset (Brazilian Olist dataset), containing:

- Orders
- Customers
- Products
- Payments
- Delivery information

---

## Key Analysis

### 1. Payment Distribution
- Identifies the most common payment methods used by customers

### 2. Top Product Categories
- Shows the highest revenue-generating product categories

### 3. Delivery Performance
- Measures average delivery time across different states

### 4. Revenue Trends
- Monthly revenue analysis over time

### 5. Price vs Freight Analysis
- Examines relationship between product price and shipping cost

---

## Visualizations

The project generates multiple types of charts:

- Pie chart → Payment type distribution  
- Bar chart → Top product categories  
- Horizontal bar → Delivery time by state  
- Line chart → Monthly revenue trend  
- Histogram → Price distribution  
- Scatter plot → Price vs freight value  

Interactive visualizations are also generated using Plotly.

---

## Sample Outputs

<img width="1497" height="714" alt="Untitled" src="https://github.com/user-attachments/assets/093be1a2-08fc-45ac-8101-dbd096e6fd53" />


---

## How to Run

### 1. Setup PostgreSQL

- Create database: `mercadoinsights_db`
- Import dataset tables using pgAdmin

### 2. Run SQL scripts

Execute:


sql/schema.sql
sql/queries.sql


---

### 3. Install dependencies


pip install -r requirements.txt


---

### 4. Run analytics


python src/main.py


---

## Outputs

- Excel report with multiple sheets
- Saved charts (PNG)
- Interactive Plotly HTML visualizations

---

## Key Results

- Identified top-performing product categories by revenue
- Observed seasonal trends in monthly sales
- Detected variations in delivery time across regions
- Found correlation between product price and freight cost

---

## Type

Academic Project (Data Visualization & Analytics)

---

## Future Improvements

- Add dashboard (Streamlit or Power BI)
- Real-time data integration
- Advanced predictive analytics

---

## License

MIT License
