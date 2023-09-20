from django.db import models

# Create your models here.
class Track(models.Model):
    title = models.CharField( max_length=300)
    category = models.CharField(max_length=150)
    type = models.CharField( max_length= 100 ,choices=[('', 'Select'),('Income', 'Income'), ('Expenditure', 'Expenditure')])
    amount = models.IntegerField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title 
    