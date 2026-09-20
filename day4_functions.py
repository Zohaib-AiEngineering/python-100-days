# Day 4: Functions, Type Hints, Docstrings, *args & **kwargs

def process_user_data(username: str, *skills: str, **extra_info) -> dict:
    """
    Processes user profile data, cleans skill names, and packs extra metadata.

    Args:
        username (str): The main name of the candidate.
        *skills (str): Unlimited skill strings to be formatted.
        **extra_info: Flexible key-value pairs for extra details.

    Returns:
        dict: A structured dictionary containing cleaned user profile.
    """
    # List comprehension to clean spaces and capitalize skill names
    formatted_skills = [skill.strip().title() for skill in skills]
    
    # Building structured dictionary
    profile = {
        "user": username,
        "skills": formatted_skills,
        "skills_count": len(formatted_skills),
        "details": extra_info
    }
    return profile


# --- Testing the Function ---
if __name__ == "__main__":
    # Calling function with multiple skills (*args) and metadata (**kwargs)
    user_data = process_user_data(
        "Muhammad Zohaib",
        "python ", " git ", "ai engineering", "web scraping",
        role="AI Engineer",
        location="Lahore",
        status="Active Learner"
    )

    # Printing Structured Output (Clean & Formatted)
    print("===================================")
    print("       USER PROFILE SUMMARY        ")
    print("===================================")
    print(f"User Name    : {user_data['user']}")
    print(f"Total Skills : {user_data['skills_count']}")
    print(f"Skills List  : {', '.join(user_data['skills'])}")
    print(f"Role         : {user_data['details'].get('role')}")
    print(f"Location     : {user_data['details'].get('location')}")
    print(f"Status       : {user_data['details'].get('status')}")
    print("===================================")