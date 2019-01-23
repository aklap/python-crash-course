from django.db import models
from datetime import date


# Create your models here.
class BlogPost(models.Model):
    """A written entry in the blog."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def formatted_date(self):
        """Format the date of post create."""
        # Returns as 'Month day, year'
        return self.date_added.strftime('%B %d, %Y')

