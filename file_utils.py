import json

def save_json_data(file_path: str, data: dict) -> bool:
    """
    Safely writes a dictionary to a JSON file using with open().
    """
    try:
        # HINT 1: Modern file handling syntax (write mode 'w')
        with open(file_path, "w") as file:
            # HINT 2: json module ka function jo data ko file me dump karta hai
            json.dump(data, file, indent=4)
        print(f"[SUCCESS] Data saved to {file_path}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save data: {e}")
        return False


def read_json_data(file_path: str) -> dict:
    """
    Safely reads a JSON file and returns dictionary.
    Handles FileNotFoundError gracefully.
    """
    try:
        # HINT 3: Read mode 'r' me open karein
        with open(file_path, "r") as file:
            # HINT 4: json module ka function jo file se data load karta hai
            return json.load(file)
            
    # HINT 5: Agar file na mile toh konsa specific Exception catch karte hain?
    except FileNotFoundError:
        print(f"[WARNING] File '{file_path}' does not exist.")
        return {}
        
    finally:
        # HINT 6: Yeh block success ho ya fail, HAMESHA chalega
        print(f"[LOG] Read attempt finished for '{file_path}'")