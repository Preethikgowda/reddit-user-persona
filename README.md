# 🧠 Reddit User Persona Generator using GPT-3.5

This project generates detailed and structured **user personas** from any public Reddit profile using **Reddit API + OpenAI GPT-3.5**.  
The output includes the user’s inferred age, personality traits (MBTI), motivations, frustrations, habits — all backed by **citations from their actual posts and comments**.

> 🔍 Developed as part of the **Generative AI Internship Task** at BeyondChats.

---

## 🚀 Features

✅ Scrapes up to 10 posts and 20 comments from a Reddit profile  
✅ Builds structured user personas with GPT-3.5  
✅ Cites user’s original comments/posts for each trait  
✅ Output saved to a `.txt` file (`persona_<username>.txt`)  
✅ Clean `.env` handling with `.gitignore`  
✅ Perfect for internships, AI profiling, and LLM-driven UX research

---

## 🧩 Technologies Used

- Python 3
- [`praw`](https://praw.readthedocs.io/) – Reddit API Wrapper  
- [`openai`](https://platform.openai.com/) – GPT-3.5 for AI persona generation  
- `python-dotenv` – Securely handle environment variables  

---

## 💻 How to Run This Project

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/Preethikgowda/reddit-user-persona.git
cd reddit-user-persona
```
###✅ 2. Set Up Your Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

###✅ 3. Create Your .env File
Create a .env file in the root folder based on .env.example:

env
```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=script by u/your_reddit_username
OPENAI_API_KEY=your_openai_key
```
🔒 Do NOT share this .env file. It’s in .gitignore by default.

###✅ 4. Run the Script
```bash
python generate_persona.py
```
When prompted, enter a Reddit profile URL:

```bash
Enter Reddit user profile URL: https://www.reddit.com/user/spez/
```
🔄 Sample Input & Output
🧷 Input:
```ruby
https://www.reddit.com/user/_purple_Giraffe/
```
📄 Output: persona__purple_Giraffe.txt
<details> <summary>Click to expand sample</summary>
# _purple_Giraffe

**AGE**  
27

**OCCUPATION**  
Graphic Designer

**STATUS**  
Single

**LOCATION**  
Seattle, Washington

**TIER**  
Casual User

**ARCHETYPE**  
Lurker


## GOALS & NEEDS  
- "I aim to improve my graphic design skills..."
- "I want to connect with like-minded creatives..."

## FRUSTRATIONS  
- "Trolls and negativity are annoying."
- "Too much misinformation."


</details>
✅ The model uses actual Reddit content to infer all traits. If the user has fewer comments, GPT may generalize.

📁 Folder Structure
bash
Copy code
reddit-user-persona/
├── generate_persona.py       # Main script
├── .env.example              # Placeholder for environment secrets
├── requirements.txt          # Python dependencies
├── .gitignore                # Ignores .env, venv, output files
├── persona_<username>.txt    # AI-generated persona (ignored by Git)
🛡️ Security Notes
All secrets are kept in .env and never pushed to GitHub

Persona files (persona_*.txt) are also excluded via .gitignore

🙋‍♀️ Developed By
Preethi T K
preethikgowda26@gmail.com
