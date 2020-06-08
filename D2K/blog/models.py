from django.db import models
from django.utils import timezone
# Create your models here.

class Title(models.Model):
    Title_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.Title_text
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Subtitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, default = '')
    pub_date = models.DateTimeField('date published')
    context = models.CharField(max_length=200,default = '' )
    def __str__(self):
        return self.context

class Paragraph(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, default = '')
    subtitle = models.ForeignKey(Subtitle, on_delete=models.CASCADE, default = '' )
    pub_date = models.DateTimeField('date published')
    context = models.TextField(max_length=5000)
    #Label = models.CharField(max_length=200, default = '')
    def __str__(self):
        return self.context
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



