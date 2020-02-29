from django.db import models

class Post(models.Model):
    
    text = models.TextField()

    def __str__(self):
        # Return the first 50 chars of the text field
        return self.text[:50]
