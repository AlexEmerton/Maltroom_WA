from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NotesList(APIView):
    @staticmethod
    def get(request, format=None):
        notes = Notes.objects.all()
        serializer_class = NotesSerializer(notes, many=True)
        return Response(serializer_class.data)


class NameList(APIView):
    @staticmethod
    def get(request, format=None):
        names = Names.objects.all()
        serializer_class = NamesSerializer(names, many=True)
        return Response(serializer_class.data)


class NoseList(APIView):
    @staticmethod
    def get(request, format=None):
        noses = Nose.objects.all()
        serializer_class = NoseSerializer(noses, many=True)
        return Response(serializer_class.data)


class PalateList(APIView):
    @staticmethod
    def get(request, format=None):
        palates = Palate.objects.all()
        serializer_class = PalateSerializer(palates, many=True)
        return Response(serializer_class.data)


class FinishList(APIView):
    @staticmethod
    def get(request, format=None):
        finishes = Finish.objects.all()
        serializer_class = FinishSerializer(finishes, many=True)
        return Response(serializer_class.data)
