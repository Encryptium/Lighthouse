import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    image = models.ImageField(upload_to=f'static/uploads/%Y/%m/%d/{uuid.uuid4()}', default='static/img/lighthouse.svg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    # set date field only to current date and uneditable
    date = models.DateField(auto_now_add=True, editable=False)


    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.title