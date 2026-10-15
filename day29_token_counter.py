
import tiktoken

# Select tokenizer
encoding = tiktoken.get_encoding("cl100k_base")

# Get text from user
text = input("Enter your text: ")

# Count words
words = len(text.split())

# Count characters
characters = len(text)

# Count tokens
tokens = encoding.encode(text)
total_tokens = len(tokens)

# Display results
print("\n--- Token Counter Results ---")
print("Your text:", text)
print("Word count:", words)
print("Character count:", characters)
print("Token count:", total_tokens)
print("Token IDs:", tokens)
