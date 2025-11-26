import google.generativeai as genai

# PASTE YOUR KEY HERE
GOOGLE_API_KEY = "AIzaSyD7TRGeHw8XKRSd5SPnQjD5gRtN2iez_sg"

def generate_roadmap(role, current_skills):
    """
    Hybrid Logic: Tries AI first. If AI fails, falls back to manual rules.
    """
    print(f"Generating roadmap for: {role}...") # Debug print
    
    # --- ATTEMPT 1: GOOGLE AI ---
    try:
        genai.configure(api_key="AIzaSyD7TRGeHw8XKRSd5SPnQjD5gRtN2iez_sg")
        
        # Try the most standard model first
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""
        Create a 5-step learning path for a '{role}'.
        Current skills: '{current_skills}'.
        Return ONLY a clean list of 5 steps. No intro text.
        """
        
        response = model.generate_content(prompt)
        
        # Process the AI response
        if response.text:
            roadmap = [step.strip().replace('*', '') for step in response.text.split('\n') if step.strip()]
            return roadmap[:5] # Ensure we only return 5 steps

    except Exception as e:
        print(f"⚠️ AI Failed: {e}")
        print("🔄 Switching to Manual Mode...")

    # --- ATTEMPT 2: MANUAL FALLBACK (Backup Plan) ---
    role = role.lower()
    if "python" in role or "django" in role:
        return [
            "Week 1: Master Python Syntax & OOP",
            "Week 2: Learn Django ORM & Models",
            "Week 3: Build a REST API",
            "Week 4: Learn SQL/Database Management",
            "Week 5: Deploy a project to Heroku/Render"
        ]
    elif "frontend" in role or "react" in role:
        return [
            "Week 1: HTML5, CSS3 & Flexbox",
            "Week 2: JavaScript ES6+ Features",
            "Week 3: Learn React Components & Hooks",
            "Week 4: State Management (Redux)",
            "Week 5: Build a Portfolio Website"
        ]
    else:
        return [
            f"Step 1: Research the core skills for {role}",
            "Step 2: Find a top-rated course on Udemy/Coursera",
            "Step 3: Build a beginner capstone project",
            "Step 4: Network with professionals on LinkedIn",
            "Step 5: Apply for internships or junior roles"
        ]