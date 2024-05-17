from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts, LoanOptions, LoanProducts

# ========================== 예금 ==========================

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('deposit',)


# 모든 은행 상품 조회 bank - products - options 
class AllDepositProductsOptionsSerializer(serializers.ModelSerializer):
    
    depositoptions_set = DepositOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProducts
        fields = '__all__'


# 기간 6, 12, 24, 36
# 이자율
# 가입방식 
class OrderOptionDepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

    class DepositOptionsSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositOptions
            fields = '__all__'
            read_only_fields = ('deposit',)
    
    depositoptions_set = DepositOptionsSerializer(read_only=True, many=True)



# ========================== 적금 ==========================

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'


class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('saving',)


# 모든 은행 상품 조회 bank - products - options 
class AllSavingProductsOptionsSerializer(serializers.ModelSerializer):
    
    savingoptions_set = SavingOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = SavingProducts
        fields = '__all__'

# 기간 6, 12, 24, 36
class OrderOptionSavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

    class SavingOptionsSerializer(serializers.ModelSerializer):
        class Meta:
            model = SavingOptions
            fields = '__all__'
            read_only_fields = ('saving',)
    
    savingoptions_set = SavingOptionsSerializer(read_only=True, many=True)


# ============================ 대출 ============================

class LoanProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProducts
        fields = '__all__'


class LoanOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanOptions
        fields = '__all__'
        read_only_fields = ('loan',)


# 모든 은행 상품 조회 bank - products - options 
class AllLoanProductsOptionsSerializer(serializers.ModelSerializer):
    
    loanoptions_set = LoanOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = LoanProducts
        fields = '__all__'


# 기간 6, 12, 24, 36
# 이자율
# 가입방식 
class OrderOptionLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanProducts
        fields = '__all__'

    class LoanOptionsSerializer(serializers.ModelSerializer):
        class Meta:
            model = LoanOptions
            fields = '__all__'
            read_only_fields = ('loan',)
    
    loanoptions_set = LoanOptionsSerializer(read_only=True, many=True)