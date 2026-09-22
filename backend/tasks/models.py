from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Progress', 'Progress')
    ]

    title= models.CharField(max_length=200)
    description=models.TextField()
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending',
    )

    employee=models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='tasks',

    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
