"""
Day 9: Pandas Transformations & Aggregations
Grouping, Merging DataFrames, and Exporting Data
"""
import pandas as pd

def main():
    # Dataset 1: Department wise Sales Log
    sales_data = {
        "Emp_ID": [101, 102, 103, 104, 105, 106],
        "Department": ["AI", "AI", "Web", "Web", "AI", "Web"],
        "Sales": [1500, 2300, 1200, 1800, 3100, 900]
    }
    
    # Dataset 2: Employee Profile Details
    emp_details = {
        "Emp_ID": [101, 102, 103, 104, 105, 106],
        "Name": ["Zohaib", "Ali", "Sara", "Ahmed", "Usman", "Ayesha"]
    }

    df_sales = pd.DataFrame(sales_data)
    df_emp = pd.DataFrame(emp_details)

    print("--- 1. Grouping & Aggregations ---")
    # SENIOR TIP: Groupby ke baad column select karke aggregation method (.mean(), .sum()) lagate hain.
    # HINT 1: Department ke hisab se Sales ka average (mean) nikalein
    avg_sales_per_dept = df_sales.groupby("Department")["Sales"].mean()
    print("Average Sales per Department:")
    print(avg_sales_per_dept)

    print("\n--- 2. Merging DataFrames ---")
    # SENIOR TIP: SQL Join ki tarah dono tables ko common 'Emp_ID' key par link karein.
    # HINT 2: pd.merge mein primary key pass karein
    merged_df = pd.merge(df_emp, df_sales, on="Emp_ID")
    print("Merged Employee Profile & Sales Data:")
    print(merged_df)

    print("\n--- 3. Exporting Clean Report ---")
    # SENIOR TIP: index=False rakhne se extra row-index numbers file mein save nahi hote.
    # HINT 3: CSV file mein export karne ke liye Pandas ka function
    merged_df.to_csv("processed_sales_report.csv", index=False)
    print("[SUCCESS] Processed report exported to 'processed_sales_report.csv'")

if __name__ == "__main__":
    main()