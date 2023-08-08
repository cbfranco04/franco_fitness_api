from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from ..models import Account
from ..serializers.account import AccountSerializer


class AccountListView(APIView):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # TODO: verify payload is correct format

        data = {
            "username": request.data.get("username"),
            "first_name": request.data.get("first_name"),
        }
        serializer = AccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, account_id, *args, **kwargs):
        print(account_id)
        account_instance = self.get_object(account_id)
        if not account_instance:
            return Response(
                {"error": f"Account with id {account_id} does not exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = AccountSerializer(account_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, account_id):
        try:
            return Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return None
