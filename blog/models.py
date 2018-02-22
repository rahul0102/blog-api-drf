from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    published_date = models.DateTimeField(blank = True, null = True)
    slug = models.SlugField() #used for url of perticular blog
    author = models.ForeignKey(User, default = None)
    thumbnail = models.ImageField(default = 'default.png', blank = True, null= True)

    def publish(self, author):
        self.published_date = timezone.now()
        new_title = self.title.lower()
        new_slug = '-'.join(new_title.split(" "))
        self.slug = new_slug
        self.author = author
        self.save()

    # return the informal representation of aticle object
    # means what aticle object should display when we fetch from database using Article.objects.all()
    def __str__(self):
        return self.title
