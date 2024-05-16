from django.db import models
from django.conf import settings

class DepositProduct(models.Model):
   fin_co_no = models.CharField(max_length=100)             # 금융회사 코드
   kor_co_nm = models.CharField(max_length=100)             # 금융회사명
   fin_prdt_cd = models.CharField(max_length=100)           # 금융상품 코드
   fin_prdt_nm = models.CharField(max_length=100)           # 금융상품명
   join_way = models.CharField(max_length=100)              # 가입 방법
   mtrt_int = models.TextField(blank=True, null=True)       # 만기 후 이자율
   spcl_cnd = models.TextField(blank=True, null=True)       # 우대 조건
   join_deny = models.IntegerField(blank=True, null=True)   # 가입 제한
   join_member = models.TextField(blank=True, null=True)    # 가입 대상
   etc_note = models.TextField(blank=True, null=True)       # 기타 유의사항
   max_limit = models.IntegerField(blank=True, null=True)   # 최고 한도
   contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='deposit_contract', null=True)     # 계약자 


class SavingProduct(models.Model):
   fin_co_no = models.CharField(max_length=100)             # 금융회사 코드
   kor_co_nm = models.CharField(max_length=100)             # 금융회사명
   fin_prdt_cd = models.CharField(max_length=100)           # 금융상품 코드
   fin_prdt_nm = models.CharField(max_length=100)           # 금융상품명
   join_way = models.CharField(max_length=100)              # 가입 방법
   mtrt_int = models.TextField(blank=True, null=True)       # 만기 후 이자율
   spcl_cnd = models.TextField(blank=True, null=True)       # 우대 조건
   join_deny = models.IntegerField(blank=True, null=True)   # 가입 제한
   join_member = models.TextField(blank=True, null=True)    # 가입 대상
   etc_note = models.TextField(blank=True, null=True)       # 기타 유의사항
   max_limit = models.IntegerField(blank=True, null=True)   # 최고 한도
   contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='saving_contract', null=True)     # 계약자 


class LoanProduct(models.Model):
   fin_co_no = models.CharField(max_length=100)             # 금융회사 코드
   kor_co_nm = models.CharField(max_length=100)             # 금융회사명
   fin_prdt_cd = models.CharField(max_length=100)           # 금융상품 코드
   fin_prdt_nm = models.CharField(max_length=100)           # 금융상품명
   crdt_prdt_type_nm = models.CharField(max_length=100)     # 대출 종류명
   join_way = models.CharField(max_length=100)              # 가입 방법
   cd_name = models.CharField(max_length=100)               # CB 회사명 (신용평가)
   contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='loan_contract', null=True)


class DepositOption(models.Model):
   deposit = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)   # 해당 예금 상품 외래키
   intr_rate_type_nm = models.CharField(max_length=2)    # 저축금리 유형명
   intr_rate = models.FloatField(null=True)              # 저축금리 
   intr_rate2 = models.FloatField(null=True)             # 최고 우대금리
   save_trm = models.CharField(max_length=3)             # 저축기간 (개월)


class SavingOption(models.Model):
   saving = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)  # 해당 적금 상품 외래키 
   intr_rate_type_nm = models.CharField(max_length=2)    # 저축금리 유형명
   rsrv_type_nm = models.CharField(max_length=10)        # 적립 유형명
   intr_rate = models.FloatField(null=True)              # 저축금리 
   intr_rate2 = models.FloatField(null=True)             # 최고 우대금리
   save_trm = models.CharField(max_length=3)             # 저축기간 (개월)


class LoanOption(models.Model):
   loan = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)   # 해당 대출 상품 외래키
   crdt_lend_rate_type = models.CharField(max_length=10)    # 금리 구분 코드
   crdt_lend_rate_type_nm = models.CharField(max_length=20) # 금리 구분
   crdt_grad_1 = models.FloatField(null=True)                # 신용점수 900점 초과
   crdt_grad_4 = models.FloatField(null=True)                # 801 ~ 900
   crdt_grad_5 = models.FloatField(null=True)                # 701 ~ 800

