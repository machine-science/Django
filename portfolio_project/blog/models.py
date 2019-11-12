from django.db import models

# Create blog model.
# title
# publicationDate
# Body
# image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to= "images/")


# Add blog app to settings
# go to setting.py in project level
# add blog.apps.BlogConfig to INSTALLED_APPS list

# create a migrations
# Now go to terminal and run python manage.py makemigrations

# migrate
# Then do python manage.py migrate

# Add to the admin
# Go to admin.py from blog folder and add:
    # from .models import Blog
    # admin.site.register(Blog)
