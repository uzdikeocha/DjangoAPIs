from rest_framework import serializers
from .models import link

class linkserializer(serializers.modelserializer)
    class meta:
         model = link
         fields = "__all__"