from django.urls import path
from . import views

urlpatterns = [
    #ex: /api/questions/all
    path('questions/all/', views.QuestionReadView.as_view()),
    #ex: /api/questions/add
    path('questions/add/', views.QuestionCreateView.as_view()),
    #ex: /api/questions/delete/2
    path('questions/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
    #ex: /api/questions/edit/2
    path('questions/edit/<int:pk>/', views.QuestionUpdateView.as_view()),
    #ex: /api/votes/all
    path('choices/all/', views.ChoiceReadView.as_view()),
]

# Using angle brackets “captures” part of the URL and sends it as a keyword argument to the view function.
# The :question_id> part of the string defines the name that will be used to identify the matched pattern
# and the <int: part is a converter that determines what patterns should match this part of the URL path.
# pk is short for primary key, which is a unique identifier for each record in a database. 
# Every Django model has a field which serves as its primary key, 
# and whatever other name it has, it can also be referred to as "pk".