# 1. Nested Dictionary (Real-world Data Format)
student_profile = {
    "name": "Muhammad Zohaib",
    "degree": "BSCS",
    "skills": ["Python", "Git", "AI Engineering"],
    "is_active": True
}

# 2. List Comprehension (Fast Data Processing)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]

# 3. Tuple Unpacking & Sets (Unique Data)
coordinates = (30.1978, 71.4711)  # Lat, Long
lat, lon = coordinates

raw_tags = ["python", "ai", "python", "git", "ai"]
unique_tags = list(set(raw_tags))

# Displaying Outputs
print("--- Student Profile ---")
print(f"Name: {student_profile['name']}")
print(f"Skills Count: {len(student_profile['skills'])}")

print("\n--- Processed Data ---")
print(f"Even Numbers: {even_numbers}")
print(f"Coordinates: Latitude {lat}, Longitude {lon}")
print(f"Unique Skills/Tags: {unique_tags}")