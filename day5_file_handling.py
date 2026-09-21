# HINT 1: file_utils module se dono functions import karein
from file_utils import save_json_data, read_json_data

def main():
    log_file = "ai_system_logs.json"
    
    # User Profile Data
    model_log = {
        "user": "Muhammad Zohaib",
        "role": "AI Engineer",
        "status": "Learning Hybrid Mode",
        "metrics": {"accuracy": 0.98}
    }
    
    print("--- 1. Testing File Saving ---")
    save_json_data(log_file, model_log)
    
    print("\n--- 2. Testing File Reading ---")
    # HINT 2: Read function call karein aur argument me variable log_file pass karein
    retrieved_data = read_json_data(log_file)
    
    # HINT 3: Dictionary ke .get() method me user key ("user") pass karein
    print(f"User Name: {retrieved_data.get('user')}")
    
    print("\n--- 3. Testing Missing File Error ---")
    # Missing file read karne ki koshish karein taake FileNotFoundError check ho sake
    read_json_data("missing_file.json")

if __name__ == "__main__":
    main()