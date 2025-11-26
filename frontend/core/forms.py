from django import forms

class CareerForm(forms.Form):  # <--- Name must match what is in views.py
    target_role = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Enter your dream job...'
        })
    )
    current_skills = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4,
            'placeholder': 'e.g. HTML, Basic Python, Communication...'
        })
    )