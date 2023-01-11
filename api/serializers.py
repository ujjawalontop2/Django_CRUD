from rest_framework import serializers
from api.models import Tutorials

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorials
        fields ='__all__'
