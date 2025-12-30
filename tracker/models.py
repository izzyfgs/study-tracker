from django.db import models

from django.db import models

class Score(models.Model):
    SUBJECT_CHOICES = [
        ('Maths', 'Maths'),
        ('English', 'English'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemistry'),
    ]

    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    year = models.IntegerField()
    total_questions = models.IntegerField(default=50)
    score = models.IntegerField()
    percentage = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically calculate percentage
        self.percentage = (self.score / self.total_questions) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject} {self.year} - {self.score}/{self.total_questions}"

