from django.shortcuts import render
from django.conf import settings
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts, LoanOptions, LoanProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer, LoanOptionsSerializer, LoanProductsSerializer

API_KEY = '664b04c24b9ab5090e97c4dc608cce44'

# def index(request):
#     url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
#     response = requests.get(url).json().get('result')
    
#     return JsonResponse(response)


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