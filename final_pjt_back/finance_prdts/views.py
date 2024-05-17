from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Prefetch

from .models import *
from .serializers import *

API_KEY = '664b04c24b9ab5090e97c4dc608cce44'


def save_products(request):
    ## 예금
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')

    for li in response.get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        fin_co_no = li.get('fin_co_no')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')
        mtrt_int = li.get('mtrt_int')
        max_limit = li.get('max_limit')
        save_data = {
            'fin_co_no':fin_co_no,
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
            'mtrt_int':mtrt_int,
            'max_limit':max_limit,
        }
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')
        if DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, save_trm=save_trm).exists():
            continue
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        deposit = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        optionserializer = DepositOptionsSerializer(data=save_data)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(deposit=deposit)

    ## 적금
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')

    for li in response.get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if SavingProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        fin_co_no = li.get('fin_co_no')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')
        mtrt_int = li.get('mtrt_int')
        max_limit = li.get('max_limit')
        save_data = {
            'fin_co_no':fin_co_no,
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
            'mtrt_int':mtrt_int,
            'max_limit':max_limit,
        }
        serializer = SavingProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        rsrv_type_nm = li.get('rsrv_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')
        if SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, save_trm=save_trm).exists():
            continue
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'rsrv_type_nm':rsrv_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        saving = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        optionserializer = SavingOptionsSerializer(data=save_data)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(saving=saving)

    
    ## 대출
    url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json().get('result')

    for li in response.get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        if LoanProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        fin_co_no = li.get('fin_co_no')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        crdt_prdt_type_nm = li.get('crdt_prdt_type_nm')
        join_way = li.get('join_way')
        cd_name = li.get('cd_name')
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'fin_co_no':fin_co_no,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'crdt_prdt_type_nm':crdt_prdt_type_nm,
            'join_way':join_way,
            'cd_name':cd_name
        }
        serializer = LoanProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in response.get('optionList'):
        fin_prdt_cd = li.get('fin_prdt_cd')
        crdt_lend_rate_type = li.get('crdt_lend_rate_type')
        if LoanOptions.objects.filter(fin_prdt_cd=fin_prdt_cd, crdt_lend_rate_type=crdt_lend_rate_type).exists():
            continue
        crdt_lend_rate_type_nm = li.get('crdt_lend_rate_type_nm')
        crdt_grad_1 = li.get('crdt_grad_1')
        crdt_grad_4 = li.get('crdt_grad_4')
        crdt_grad_5 = li.get('crdt_grad_5')
        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'crdt_lend_rate_type':crdt_lend_rate_type,
            'crdt_lend_rate_type_nm':crdt_lend_rate_type_nm,
            'crdt_grad_1':crdt_grad_1,
            'crdt_grad_4':crdt_grad_4,
            'crdt_grad_5':crdt_grad_5,
        }
        loan = LoanProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        optionserializer = LoanOptionsSerializer(data=save_data)
        if optionserializer.is_valid(raise_exception=True):
            optionserializer.save(loan=loan)

    return JsonResponse({'message':'finance 저장'})

# ============================ 예금 ============================

@api_view(['GET'])
#    전체 예금상품 목록 조회 
#   path('dep_list/', views.dep_list),
def dep_list(request):
    deposits  = DepositProducts.objects.all()
    serializers = DepositProductsSerializer(deposits , many=True)
    return Response(serializers.data)


@api_view(['GET'])
#    은행 코드로 예금상폼 목록 조회 
#   path('dep_list/<str:dep_cd>/', views.dep_detail),
def dep_detail(request, dep_cd):
    dep_prdts = get_object_or_404(DepositProducts, fin_prdt_cd=dep_cd)
    serializers = DepositProductsSerializer(dep_prdts)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 예금상품 옵션 목록 조회 
#   path('dep_list/<str:dep_cd>/opt_list/', views.depOpt_list),
def depOpt_list(request, dep_cd):
    dep_prdt = get_object_or_404(DepositProducts, fin_prdt_cd=dep_cd)
    dep_options = DepositOptions.objects.filter(deposit=dep_prdt)
    serializers = DepositOptionsSerializer(dep_options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 예금상품 옵션 단일 조회 
#   path('dep_list/<str:dep_cd>/opt_list/<int:depOpt_pk>/', views.depOpt_detail),
def depOpt_detail(request, dep_cd, depOpt_pk):
    dep_prdt = get_object_or_404(DepositProducts, fin_prdt_cd=dep_cd)
    dep_option = get_object_or_404(DepositOptions, pk=depOpt_pk, deposit=dep_prdt)
    serializers = DepositOptionsSerializer(dep_option)
    return Response(serializers.data)

# ---------------------- 예금 조건 정렬 -----------------------

# 모든 은행 상품 조회 bank - products - options 
# all_dep_prdts_by_bank/
@api_view(['GET'])
def all_dep_prdts_by_bank(request):
    dep_prdts = DepositProducts.objects.all()
    serializers = AllDepositProductsOptionsSerializer(dep_prdts, many=True)
    return Response(serializers.data)


# 특정 은행 상품 조회 bank - products - options 
@api_view(['GET'])
def dep_prdts_by_bank(request, fin_co_no):
    dep_prdts = DepositProducts.objects.filter(fin_co_no=fin_co_no)
    serializers = AllDepositProductsOptionsSerializer(dep_prdts, many=True)
    return Response(serializers.data)


# 가입 방식별 정렬 
@api_view(['GET'])
def dep_prdts_by_joinway(request):
    pass


# 기간 6, 12, 24, 36
@api_view(['GET'])
def dep_prdts_save_trm(request, save_trm):

    # dep_options_prefetch = Prefetch('depositoptions_set', queryset=DepositOptions.objects.filter(save_trm=save_trm).order_by('intr_rate'))
    # dep_prdts = DepositProducts.objects.prefetch_related(dep_options_prefetch).filter(depositoptions__save_trm=save_trm).distinct()

    dep_options_prefetch = Prefetch(
        'depositoptions_set', 
        queryset=DepositOptions.objects.filter(save_trm=save_trm).order_by('intr_rate')
    )

    dep_prdts = DepositProducts.objects.prefetch_related(dep_options_prefetch).distinct()
    serializer = OrderOptionDepositSerializer(dep_prdts, many=True)
    return Response(serializer.data)


# 은행 이율 내림차순 정렬
@api_view(['GET']) 
def dep_prdts_sorted_by_rate(request):
    rate_order_prefetch = Prefetch(
        'depositoptions_set',
        queryset=DepositOptions.objects.all().order_by('-intr_rate')
    )
    dep_prdts = DepositProducts.objects.prefetch_related(rate_order_prefetch).distinct()
    serializer = OrderOptionDepositSerializer(dep_prdts, many=True)
    return Response(serializer.data)


# ============================ 적금 ============================


@api_view(['GET'])
#   전체 적금상품 목록 조회
#   path('sav_list/', views.sav_list),
def sav_list(request):
    sav_prdts = SavingProducts.objects.all()
    serializers = SavingProductsSerializer(sav_prdts, many=True)
    return Response(serializers.data)
    

@api_view(['GET'])
#   은행 코드로 적금상품 목록 조회 
#   path('sav_list/<str:sav_cd>/', views.sav_detail),
def sav_detail(request, sav_cd):
    sav_prdts = get_object_or_404(SavingProducts, fin_prdt_cd=sav_cd)
    serializers = SavingProductsSerializer(sav_prdts)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 적금상품 옵션 목록 조회
#   path('sav_list/<str:sav_cd>/opt_list/', views.savOpt_list),
def savOpt_list(request, sav_cd):
    sav_prdt = get_object_or_404(SavingProducts, fin_prdt_cd=sav_cd)
    sav_options = SavingOptions.objects.filter(saving=sav_prdt)
    serializers = SavingOptionsSerializer(sav_options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 적금상폼 옵션 단일 조회 
#   path('sav_list/<str:sav_cd>/opt_list/<int:savOpt_pk>/', views.savOpt_detail),
def savOpt_detail(request, sav_cd, savOpt_pk):
    sav_prdt = get_object_or_404(SavingProducts, fin_prdt_cd=sav_cd)
    sav_option = get_object_or_404(SavingOptions, pk=savOpt_pk, saving=sav_prdt)
    serializers = SavingOptionsSerializer(sav_option)
    return Response(serializers.data)


# ---------------------- 적금 조건 정렬 -----------------------

# 모든 은행 상품 조회 bank - products - options 
@api_view(['GET'])
def all_sav_prdts_by_bank(request):
    sav_prdts = SavingProducts.objects.all()
    serializers = AllSavingProductsOptionsSerializer(sav_prdts, many=True)
    return Response(serializers.data)


# 특정 은행 상품 조회 bank - products - options 
@api_view(['GET'])
def sav_prdts_by_bank(request, fin_co_no):
    sav_prdts = SavingProducts.objects.filter(fin_co_no=fin_co_no)
    serializers = AllSavingProductsOptionsSerializer(sav_prdts, many=True)
    return Response(serializers.data)

# 가입 방식별 정렬 
@api_view(['GET'])
def sav_prdts_by_joinway(request):
    pass


# 기간 6, 12, 24, 36
@api_view(['GET'])
def sav_prdts_save_trm(request, save_trm):
    sav_options_prefetch = Prefetch(
        'savingoptions_set',
        queryset=SavingOptions.objects.filter(save_trm=save_trm).order_by('intr_rate2')
    )
    sav_prdts = SavingProducts.objects.prefetch_related(sav_options_prefetch).distinct()
    serializers = OrderOptionSavingSerializer(sav_prdts, many=True)
    return Response(serializers.data)


# 은행 이율 내림차순 정렬 
@api_view(['GET'])
def sav_prdts_sorted_by_rate(request):
    rate_order_prefetch = Prefetch(
        'savingoptions_set',
        queryset=SavingOptions.objects.all().order_by('-intr_rate')
    )
    sav_prdts = SavingProducts.objects.prefetch_related(rate_order_prefetch).distinct()
    serializer = OrderOptionSavingSerializer(sav_prdts, many=True)
    return Response(serializer.data) 


# ============================ 대출 ============================


@api_view(['GET'])
#   전체 대출상품 목록 조회 
#   path('loan_list/', views.loan_list),
def loan_list(request):
    loan_prdts = LoanProducts.objects.all()
    serializers = LoanProductsSerializer(loan_prdts, many=True)
    return Response(serializers.data)


@api_view(['GET'])
#   은행 코드로 대출 상품 목록 조회 
#   path('loan_list/<str:loan_cd>/', views.loan_detail),
def loan_detail(request, loan_cd):
    loan_prdts = get_object_or_404(LoanProducts, fin_prdt_cd=loan_cd)
    serializers = LoanProductsSerializer(loan_prdts)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 대출상품 옵션 목록 조회 
#   path('loan_list/<str:loan_cd>/opt_list/', views.loanOpt_list),
def loanOpt_list(request, loan_cd):
    loan_prdts = get_object_or_404(LoanProducts, fin_prdt_cd=loan_cd)
    loan_options = LoanOptions.objects.filter(loan=loan_prdts)
    serializers = LoanOptionsSerializer(loan_options, many=True)
    return Response(serializers.data)


@api_view(['GET'])
#   해당 은행 코드 대출상품 옵션 단일 조회 
#   path('loan_list/<str:loan_cd>/opt_list/<int:loanOpt_pk>/', views.loanOpt_detail),
def loanOpt_detail(request, loan_cd, loanOpt_pk):
    loan_prdt = get_object_or_404(LoanProducts, fin_prdt_cd=loan_cd)
    loan_option = get_object_or_404(LoanOptions, pk=loanOpt_pk, loan=loan_prdt)
    serializers = LoanOptionsSerializer(loan_option)
    return Response(serializers.data)


# ---------------------- 대출 조건 정렬 -----------------------

# 모든 은행 상품 조회 bank - products - options 
@api_view(['GET'])
def all_loan_prdts_by_bank(request):
    loan_prdts = LoanProducts.objects.all()
    serializers = AllLoanProductsOptionsSerializer(loan_prdts, many=True)
    return Response(serializers.data)


# 특정 은행 상품 조회 bank - products - options 
@api_view(['GET'])
def loan_prdts_by_bank(request, fin_co_no):
    loan_prdts = LoanProducts.objects.filter(fin_co_no=fin_co_no)
    serializers = AllLoanProductsOptionsSerializer(loan_prdts, many=True)
    return Response(serializers.data)


# 대출 방식별 정렬 crdt_prdt_type_nm
@api_view(['GET'])
def loan_prdts_by_loanway(request, loanway):
    loan_prdts = LoanProducts.objects.filter(crdt_prdt_type_nm=loanway)
    serializers = AllLoanProductsOptionsSerializer(loan_prdts, many=True)
    return Response(serializers.data)

# 은행 이율 내림차순 정렬 
# 신용 점수가 아닌!!! 신용 등급으로만 접근 가능 1-3
# 추천에서 이용? 
@api_view(['GET'])
# def loan_prdts_sorted_by_rate(request, credit_grade):
def loan_prdts_sorted_by_rate(request, credit_score):
    if credit_score > 900:
        rate_order_prefetch = Prefetch(
            'loanoptions_set',
            queryset=LoanOptions.objects.all().order_by('crdt_grad_1')
        )
    elif 800 < credit_score <= 900:
        rate_order_prefetch = Prefetch(
            'loanoptions_set',
            queryset=LoanOptions.objects.all().order_by('crdt_grad_4')
        )
    elif 700 < credit_score <= 800:
        rate_order_prefetch = Prefetch(
            'loanoptions_set',
            queryset=LoanOptions.objects.all().order_by('crdt_grad_5')
        )
    sav_prdts = LoanProducts.objects.prefetch_related(rate_order_prefetch).distinct()
    serializer = OrderOptionLoanSerializer(sav_prdts, many=True)
    return Response(serializer.data) 
