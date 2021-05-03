from django.http import HttpResponse
from .models import Question, Choice
from django.shortcuts import render
from rest_framework import generics
from .serializers import QuestionSerializer, ChoiceSerializer

#Get method for questions
class QuestionReadView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#POST method for questions
class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#DELETE method for questions
class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#PUT method for questions
class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#GET method for choices
class ChoiceReadView(generics.ListAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


