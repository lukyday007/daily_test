from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts, LoanOptions, LoanProducts


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('deposit',)

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('saving',)

class LoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProducts
        fields = '__all__'

class LoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanOptions
        fields = '__all__'
        read_only_fields = ('loan',)