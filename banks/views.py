from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.decorators import action

from .models import Banks, Branches
from .serializers import BankSerializer, BranchSerializer
from .error import QueryParameterException


class BranchListView(generics.ListAPIView):
    # This is needed here in order to decode JSON as a python datatype
    serializer_class = BranchSerializer

    def get_queryset(self):
        # Get the bank name from query params
        # defaults to null if not provided
        bank_name = self.request.query_params.get('bank_name')

        # Get city from the query params
        # defaults to null if not provided
        city = self.request.query_params.get('city')

        # Check if data provided for making a request is present
        if city is None or bank_name is None:
            raise QueryParameterException(
                detail='Failed to retrieve branch. Provide Bank name or city.')

        if city:
            res = Branches.objects.filter(city=city)
        if bank_name:
            res = res.filter(bank__name=bank_name)
        
        return res

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BranchRetrieveView(generics.RetrieveAPIView):
    # Decode JSON as a native python datatype
    serializer_class = BranchSerializer

    def get_object(self):
        ifsc = self.kwargs.get('ifsc', None)

        if ifsc is None:
            raise QueryParameterException(
                detail='Please provide IFSC code.')

        return get_object_or_404(Branches, ifsc=ifsc)