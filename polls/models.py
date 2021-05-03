from django.db import models

# Create your models here.
# Here, each model is represented by a class that subclasses django.db.models.Model. 
# Each model has a number of class variables, each of which represents a database field in the model.

# Each field is represented by an instance of a Field class – 
# e.g., CharField for character fields and DateTimeField for datetimes.
# This tells Django what type of data each field holds.

# The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. 
# You’ll use this value in your Python code, and your database will use it as the column name


# Finally, note a relationship is defined, using ForeignKey. 
# That tells Django each Choice is related to a single Question. 
# Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    #Sets the object representation to be the question
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text