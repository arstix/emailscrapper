from rest_framework import serializers
from .models import *

class EmailsSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=200)
