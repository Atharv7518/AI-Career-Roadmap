from django.db import models

class CareerRole(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserRequest(models.Model):
    target_role = models.CharField(max_length=100)
    current_skills = models.TextField()
    generated_roadmap = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target_role} - {self.created_at}"