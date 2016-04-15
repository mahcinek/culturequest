from django.shortcuts import render
from main.models import Gm, Question, Quest, Answer, Location
from main.serializers import GmSerializer, QuestionSerializer, QuestSerializer, AnswerSerializer, LocationSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class GmList(generics.ListCreateAPIView):
    queryset = Gm.objects.all()
    serializer_class = GmSerializer


class GmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gm.objects.all()
    serializer_class = GmSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestList(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


class QuestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer


class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Create your views here.
