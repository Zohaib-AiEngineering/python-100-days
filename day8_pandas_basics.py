"""
Day 8: Pandas Fundamentals
Data Processing, Cleaning, and Analysis
"""
import pandas as pd

def main():
    # 1. Creating a Sample Dataset (Simulated User/AI Logs)
    raw_data = {
        "User_ID": [101, 102, 103, 104, 105],
        "Name": ["Zohaib", "Ali", "Sara", "Ahmed", None],  # Missing value
        "Score": [85, 92, None, 78, 88],                 # Missing value
        "Status": ["Active", "Active", "Inactive", "Active", "Pending"]
    }
    
    # HINT 1: Dictionary ko DataFrame mein convert karne ke liye pd ka konsa class use hota hai?
    df = pd.DataFrame(raw_data)
    
    print("--- 1. Original DataFrame ---")
    print(df)
    
    print("\n--- 2. Dataset Information ---")
    # HINT 2: Basic info aur missing values check karne wala method
    print(df.info())
    
    print("\n--- 3. Handling Missing Values ---")
    # HINT 3: 'Score' column ki missing values (None) ko 0 se fill karein
    df["Score"] = df["Score"].fillna(0)
    
    # HINT 4: Jin rows mein Name missing (None) hai unhe drop karein
    cleaned_df = df.dropna(subset=["Name"])
    
    print("Cleaned DataFrame:")
    print(cleaned_df)
    
    print("\n--- 4. Data Filtering ---")
    # Filter users with Score >= 80
    high_scorers = cleaned_df[cleaned_df["Score"] >= 80]
    print("High Scorers (Score >= 80):")
    print(high_scorers)

if __name__ == "__main__":
    main()