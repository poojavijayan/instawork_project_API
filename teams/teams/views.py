from django.http import JsonResponse
from .models import TeamMembers
from .serializer import TeamSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Method to expose get and post methods
# Functionalities of fetch and insert team member details to db
@api_view(['GET', 'POST'])
def get_or_post_team(request, format=None):
    if request.method == 'GET':
        team = TeamMembers.objects.all()
        employeeSerial = TeamSerializer(team, many=True)
        return JsonResponse({'team': employeeSerial.data}, safe=False)
    if request.method == 'POST':
        eSerial = TeamSerializer(data=request.data)
        if eSerial.is_valid():
            eSerial.save()
            return Response(eSerial.data, status=status.HTTP_200_OK)


# Method to expose PUT and DELETE methods
# Functionalities of update and delete team members
@api_view(['PUT', 'DELETE'])
def update_delete_team(request, id, format=None):
    try:
        team = TeamMembers.objects.get(pk=id)
    except TeamMembers.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        eSerial = TeamSerializer(team, data=request.data)
        if eSerial.is_valid():
            eSerial.save()
            return Response(eSerial.data, status=status.HTTP_200_OK)
        return Response(eSerial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
