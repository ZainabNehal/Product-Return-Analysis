# Product-Return-Analysis
This project analyzes product return patterns using Power BI and Python. It highlights key return reasons, time-based trends, and region-specific issues. The dashboard helps identify areas for improvement in product quality, descriptions, and customer satisfaction strategies.

✅ Data cleaning script (Python)

✅ Cleaned dataset

✅ Power BI interactive dashboard

📁 Project Structure
bash
Copy code
├── product.py                          # Python script to clean raw data
├── Cleaned_Product_Return_Data.csv     # Cleaned dataset for analysis
├── Product Return Analysis Dashboard.pbix  # Power BI dashboard file
⚙️ How to Use
1️⃣ Data Cleaning (Python)
Script: product.py
This script reads the raw dataset (ecommerce_returns_synthetic_data.csv), performs basic cleaning, and outputs a clean CSV file.

Note: The raw CSV file (ecommerce_returns_synthetic_data.csv) must be placed in the same directory before running.

Run the script:

bash
Copy code
python product.py
The cleaned file will be saved as Cleaned_Product_Return_Data.csv.

2️⃣ Data Visualization (Power BI)
File: Product Return Analysis Dashboard.pbix

Open the .pbix file in Power BI Desktop to explore the dashboard:

Return trends by region, product category, and reason

Top reasons for returns

Interactive filters and drilldowns

📝 Requirements
Python:

pandas

Install dependencies:

bash
Copy code
pip install pandas
Power BI:

Power BI Desktop (free)

💡 Project Objectives
✅ Clean raw e-commerce return data
✅ Generate a ready-to-analyze dataset
✅ Build an interactive dashboard to:

Discover patterns in return reasons

Identify high-return product categories

Support business decision-making
