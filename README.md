# Mercado Insights: Brazilian E-Commerce Data Analysis


<img width="1497" height="714" alt="Untitled" src="https://github.com/user-attachments/assets/093be1a2-08fc-45ac-8101-dbd096e6fd53" />

Project Overview
This project analyzes the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) using **PostgreSQL** and **Python**.  
It demonstrates skills in **data visualization, SQL analysis, and Python-Postgres integration**.  

Tools & Technologies
- PostgreSQL (Database)
- pgAdmin 4 (DB management)
- Python 3 (Analysis)
- Psycopg2 & Pandas (DB connection & data processing)
- VS Code (IDE)

Project Structure
mercadoinsights-olist-ecommerce/

│── main.py # Python script to run queries

│── requirements.txt # Python dependencies

│── README.md # Documentation

│

├── sql/

│ ├── schema.sql # Database schema

│ └── queries.sql # Analytical SQL queries

│

├── outputs/ # Query results (CSV)

│ ├── query_01.csv

│ ├── query_02.csv

│ └── ...

│

├── er_diagram.png # ER diagram of DB tables

│

└── venv/ # Virtual environment


sql

Setup Instructions

1. Database Setup
1. Open **pgAdmin** and log in as superuser (`postgres`).
2. Create role:
   ```sql
   CREATE USER mi_user WITH PASSWORD 'strongpass' LOGIN;
Create database:

sql

CREATE DATABASE mercadoinsights_db OWNER mi_user;
Open sql/schema.sql in pgAdmin Query Tool → run it.

Import CSVs into their matching tables (customers, orders, order_items, etc.).

2. Python Setup
visual studio bash code
cd C:\Users\musta\mercadoinsights-olist-ecommerce
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
4. Outputs
All results are saved into the outputs/ folder as CSV files.

Example:

query_01.csv → list of recent orders

query_03.csv → monthly revenue

query_04.csv → top-selling categories

query_07.csv → payment methods analysis


Project Startup Instructions

Database (pgAdmin)

Open pgAdmin 4

Connect as postgres → check that your database exists: mercadoinsights_db

Verify that it has 9 tables (olist_customers, olist_orders, etc.).

If empty → re-run schema.sql in Query Tool, then import CSVs.

VS Code (Python)

navigating terminal to pgadmin or project environment
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U mi_user -d mercadoinsights_db -W
then password: "strongpass"


Activate virtual environment:

venv\Scripts\activate.bat


Run project:

python main.py


This will:

* Connect to Postgres

* Run queries from sql/queries.sql


* Save results into outputs/ as CSV files.

# Assignment5_3D Model Processing with Open3D

Overview

This project demonstrates 3D geometry processing using the Open3D Python library.
The goal is to load a 3D model, analyze its structure, and apply multiple transformations — from mesh to point cloud, voxel grid, and clipped surfaces — all visualized step by step.

Each stage opens a new visualization window and prints information about vertices, triangles, and color attributes.


Project Steps
1️⃣ Loading and Visualization

Loaded the file: my_model_mustafa.ply

Displayed the original mesh using Open3D’s 3D viewer.

Printed the number of vertices, triangles, and checked for color/normals.

💬 Purpose: View and understand the raw geometry before processing.


2️⃣ Conversion to Point Cloud

Converted the mesh to a point cloud (5000 uniform points).

Printed the number of points and checked for color.

💬 Purpose: Create a simplified version suitable for surface reconstruction and voxelization.

3️⃣ Surface Reconstruction

Used Poisson reconstruction to generate a smooth surface from the point cloud.

Cropped unwanted parts using a bounding box.

Printed vertex and triangle counts.

💬 Purpose: Reconstruct a clean and continuous mesh from scattered point data.

4️⃣ Voxelization

Created a voxel grid (voxel_size = 0.05).

Counted the number of voxels.

Displayed the voxel model.

💬 Purpose: Represent the model as small cubes — useful for volumetric analysis.

5️⃣ Adding a Plane

Created a flat reference plane under the model using create_box().

Painted it gray and displayed together with the object.

💬 Purpose: Simulate a floor or background surface for visual comparison.

6️⃣ Surface Clipping

Removed all points on one side of the plane (e.g., Y > 0).

Displayed the clipped model.

Printed the updated vertex and triangle counts.

💬 Purpose: Demonstrate slicing or sectioning for inspection or segmentation.

7️⃣ Coloring and Extremes

Applied a color gradient along the Z-axis.

Found the lowest and highest points and marked them with spheres.

Printed their coordinates.

💬 Purpose: Visualize height-based variation and locate extremes on the model.

Technologies Used

Python 3

Open3D

NumPy

Folder Structure
Assignment5/
│
├── assignment5_open3d.py        # Main processing script

├── my_model_mustafa.ply         # 3D model file

└── README.md                    # Description and steps

How to Run
cd C:\Users\musta\mercadoinsights-olist-ecommerce\Assignment5
python assignment5_open3d.py


Each step will:

Open a visualization window

Print geometry details (vertices, triangles, colors, voxels)

Final Note

All 7 steps are implemented in sequence.
Missing any step results in 0 points according to the assignment rules.
This project demonstrates a full 3D processing pipeline: from raw geometry to reconstructed, voxelized, and color-analyzed visualization.


