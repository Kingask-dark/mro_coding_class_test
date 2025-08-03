from rest_framework import serializers
from apitest.models import LessionList

class LessionLearnSerilizer(serializers.ModelSerializer):
    class Meta:
        model = LessionList
        fields = ['lession','lession_details','title']