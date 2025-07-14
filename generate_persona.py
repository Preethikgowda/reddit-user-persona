import os
import praw
import openai
from dotenv import load_dotenv

# Load sensitive credentials from .env file
load_dotenv()

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)
reddit.read_only = True

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")


def username(profile_url):
    """Extract Reddit username from profile URL."""
    if "/user/" in profile_url:
        return profile_url.strip("/").split("/user/")[-1].split("/")[0]
    raise ValueError("Invalid Reddit profile URL format")


def user_activity(username):
    """
    Retrieve recent posts and comments made by the given Reddit user.
    """
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=10):
            posts.append(f"[Post] {submission.title}\n{submission.selftext}")
        for comment in user.comments.new(limit=20):
            comments.append(f"[Comment] {comment.body}")
    except Exception as error:
        print(f"⚠️ Unable to fetch activity for '{username}': {error}")
    
    return comments, posts


def create_prompt(username, posts, comments):
    """
    Construct the prompt to generate a structured user persona based on the user's Reddit activity.
    """
    combined_content = "\n\n".join(posts + comments)

    prompt = f"""
You are a professional analyst. Create a structured, well-organized user persona for Reddit user "{username}" 
based on their public posts and comments. Use the following template and cite at least one quote for each section.

# {username}

**AGE**  
**OCCUPATION**  
**STATUS**  
**LOCATION**  
**TIER**  
**ARCHETYPE**  


## KEY TRAITS  
### [Trait 1]  
### [Trait 2]  
### [Trait 3]  


## MOTIVATIONS  
- **CONVENIENCE**  
- **WELLNESS**  
- **SPEED**  
- **PREFERENCES**  
- **COMFORT**  
- **DIETARY NEEDS**  


## PERSONALITY (MBTI)  

| INTROVERT | EXTROVERT |  
|-----------|-----------|  
| INTUITION | SENSING   |  
| FEELING   | THINKING  |  
| PERCEIVING| JUDGING   |  


## BEHAVIOUR & HABITS  
- [Example with short quote or post reference]  
- [Another behavior, include context]  


## GOALS & NEEDS  
- [Inferred goals with source citation]  
- [Secondary goals or habits]  


## FRUSTRATIONS  
- [Challenges or complaints they mention]  
- [Optional additional quote or observation]  


Use the content below to generate your insights:
{combined_content}
"""
    return prompt


def user_persona(prompt):
    """
    Use OpenAI's language model to generate a user persona based on the constructed prompt.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1800
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"⚠️ OpenAI API Error: {error}"


def save_result(username, persona_text):
    """
    Save the generated persona to a .txt file.
    """
    filename = f"persona_{username}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(persona_text)
    print(f"\n Persona saved as '{filename}'")


#MAIN EXECUTION BLOCK
if __name__ == "__main__":
    profile_url = input("Enter Reddit user profile URL: ").strip()
    username = username(profile_url)

    comments, posts = user_activity(username)

    if not comments and not posts:
        print(f"⚠️No posts or comments found for '{username}'. Try another user.")
        exit()

    prompt = create_prompt(username, posts, comments)
    persona_output = user_persona(prompt)
    save_result(username, persona_output)

