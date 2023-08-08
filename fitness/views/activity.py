from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from ..models.account import Account
from ..models.activity import Activity
from ..serializers.activity import ActivitySerializer


class ActivityListView(APIView):
    def get(self, request, account_id):
        account = Account.objects.filter(id=account_id).first()
        if not account:
            return Response(
                {"error": f"Account with id {account_id} not found."}, status=status.HTTP_404_NOT_FOUND
            )

        activities = Activity.objects.filter(account=account)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, account_id):
        # TODO: verify payload is correct format
        data = {
            "title": request.data.get("title"),
        }

        account = Account.objects.filter(id=account_id).first()
        if not account:
            return Response({"error": f"Account with id {account_id} not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
        serializer = ActivitySerializer(data=data)
        if serializer.is_valid():
            serializer.save(account=account)  # Assign the 'account' to the new activity
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityView(APIView):
    def get(self, request, pk):
        activity = Activity.objects.filter(id=pk).first()
        if not activity:
            return Response(
                {"error": "Activity not found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ActivitySerializer(activity)
        return Response(serializer.data, status=status.HTTP_200_OK)
