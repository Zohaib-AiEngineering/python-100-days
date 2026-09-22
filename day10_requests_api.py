"""
Day 10: Working with REST APIs & Requests Library
Fetching live data from public API endpoints
"""
import requests

def fetch_public_api_data():
    # Public JSON API endpoint for testing
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    print(f"[LOG] Fetching data from: {url}")
    
    # HINT 1: HTTP GET request bhejne ke liye requests library ka konsa method use hota hai?
    response = requests.get(url)
    
    # Check Status Code
    print(f"[LOG] Response Status Code: {response.status_code}")
    
    if response.status_code == 200:
        # HINT 2: Response body ko JSON (Python dict) mein convert karne ke liye method
        data = response.json()
        
        print("\n--- Raw JSON Data Received ---")
        print(data)
        
        print("\n--- Extracted Information ---")
        print(f"Post ID: {data.get('id')}")
        print(f"Title: {data.get('title')}")
        print(f"Body: {data.get('body')}")
    else:
        print(f"[ERROR] Failed to fetch data. Status Code: {response.status_code}")

def main():
    print("--- Day 10: REST API Data Fetcher ---")
    fetch_public_api_data()

if __name__ == "__main__":
    main()