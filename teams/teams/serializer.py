from rest_framework import serializers
from .models import TeamMembers


# Class to serialize model data returned
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = "__all__"
