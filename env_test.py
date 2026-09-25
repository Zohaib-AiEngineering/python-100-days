import os
from dotenv import load_dotenv

# .env file load karein
load_dotenv()

# Variable read karke print karein
my_name = os.getenv("MY_NAME")
print(f"My name is {my_name}")