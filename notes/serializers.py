from .models import *
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('name', 'description', 'rating')


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ('rating', 'name', 'nose', 'palate', 'finish', 'extra')


class NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = "__all__"


class NoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nose
        fields = "__all__"


class PalateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palate
        fields = "__all__"


class FinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finish
        fields = "__all__"
