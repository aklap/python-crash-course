from django.db import models
from datetime import date


# Create your models here.
class BlogPost(models.Model):
    """A post in the blog."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def formatted_date(self):
        """Format the date as a strin."""
        return self.date_added.strftime('%B %m, %Y')
