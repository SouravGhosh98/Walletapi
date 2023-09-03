# Create your views here.
import jwt
import uuid
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

class WithdrawView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.auth
        try:
            user_data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token')

        withdraw_account = request.data.get('withdraw_account')
        to_be_paid_account = request.data.get('to_be_paid_account')

        if not withdraw_account or not to_be_paid_account:
            return Response({'error': 'Withdraw account and to-be-paid account are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Process the withdrawal (simulate with a simple response)
        transaction_id = str(uuid.uuid4())
        message = 'Withdrawal successful'

        return Response({'transaction_id': transaction_id, 'message': message}, status=status.HTTP_200_OK)
