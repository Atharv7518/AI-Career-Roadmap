from django.shortcuts import render
from .forms import CareerForm
from .recommender import generate_roadmap
from .models import UserRequest

# 1. Landing Page (The Matrix Animation)
def landing_view(request):
    return render(request, 'core/landing.html')

# 2. Auth Page (Login/Signup)
def auth_view(request):
    return render(request, 'core/auth.html')

# 3. Home Page (The Blue Dashboard Home)
def home_view(request):  
    return render(request, 'core/home.html')

# 4. Input Page (The Form & AI Logic)
def input_view(request):
    if request.method == 'POST':
        # --- NEW LOGIC FOR THE UDAAN FORM ---
        # 1. Get data from the new HTML input names
        role = request.POST.get('dreamRole')   # Changed from 'target_role'
        skills = request.POST.get('skills')    # This stayed the same
        
        # (Optional) You can capture other fields too if you want to save them
        user_name = request.POST.get('name')
        
        # 2. Generate Roadmap
        if role and skills:
            roadmap = generate_roadmap(role, skills)
            
            # 3. Save to DB
            UserRequest.objects.create(
                target_role=role,
                current_skills=skills,
                generated_roadmap=str(roadmap)
            )
            
            # 4. Render Result
            return render(request, 'core/result.html', {'roadmap': roadmap, 'role': role})
            
    # If GET request, show the new Intake Form
    return render(request, 'core/input.html')

# 5. Dashboard Page (The Career Library) <--- ADDED HERE
def dashboard_view(request):
    return render(request, 'core/dashboard.html')