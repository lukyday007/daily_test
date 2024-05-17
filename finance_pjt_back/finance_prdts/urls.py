from django.urls import path
from . import views

app_name="finance_prdts"
urlpatterns = [
    path('save_products/', views.save_products, name='save_products'), # DB에 저장

    path('dep_list/', views.dep_list),
    path('dep_list/<str:dep_cd>/', views.dep_detail),
    path('dep_list/<str:dep_cd>/opt_list/', views.depOpt_list),
    path('dep_list/<str:dep_cd>/opt_list/<int:depOpt_pk>/', views.depOpt_detail),
    
    path('sav_list/', views.sav_list),
    path('sav_list/<str:sav_cd>/', views.sav_detail),
    path('sav_list/<str:sav_cd>/opt_list/', views.savOpt_list),
    path('sav_list/<str:sav_cd>/opt_list/<int:savOpt_pk>/', views.savOpt_detail),

    path('loan_list/', views.loan_list),
    path('loan_list/<str:loan_cd>/', views.loan_detail),
    path('loan_list/<str:loan_cd>/opt_list/', views.loanOpt_list),
    path('loan_list/<str:loan_cd>/opt_list/<int:loanOpt_pk>/', views.loanOpt_detail),


# ---------------------- 예금 조건 정렬 -----------------------
# 모든 은행 상품 조회 bank - products - options 
    path('all_dep_prdts_by_bank/', views.all_dep_prdts_by_bank),
# 특정 은행 상품 조회 bank - products - options 
    path('dep_prdts_by_bank/<str:fin_co_no>/', views.dep_prdts_by_bank),
    
# 가입 방식별 정렬 
    path('dep_prdts_by_joinway/', views.dep_prdts_by_joinway),

# 기간 6, 12, 24, 36
    path('dep_prdts_save_trm/<int:save_trm>/', views.dep_prdts_save_trm),

# 은행 이율 내림차순 정렬 
    path('dep_prdts_sorted_by_rate/', views.dep_prdts_sorted_by_rate),


# ---------------------- 적금 조건 정렬 -----------------------
# 모든 은행 상품 조회 bank - products - options 
    path('all_sav_prdts_by_bank/', views.all_sav_prdts_by_bank),

# 특정 은행 상품 조회 bank - products - options 
    path('sav_prdts_by_bank/<str:fin_co_no>/', views.sav_prdts_by_bank),
    
# 가입 방식별 정렬 
    path('sav_prdts_by_joinway/', views.sav_prdts_by_joinway),

# 기간 6, 12, 24, 36
    path('sav_prdts_save_trm/<int:save_trm>/', views.sav_prdts_save_trm),

# 은행 이율 내림차순 정렬 
    path('sav_prdts_sorted_by_rate/', views.sav_prdts_sorted_by_rate),


# ---------------------- 대출 조건 정렬 -----------------------
# 가입 방식별 정렬 
# 모든 은행 상품 조회 bank - products - options 
    path('all_loan_prdts_by_bank/', views.all_loan_prdts_by_bank),

# 특정 은행 상품 조회 bank - products - options 
    path('loan_prdts_by_bank/<str:fin_co_no>/', views.loan_prdts_by_bank),

# 대출 방식별 정렬 (신용대출, 카드대출, 마이너스)
#                 creditloan, cardloan, minus
    path('loan_prdts_by_loanway/<str:loanway>/', views.loan_prdts_by_loanway),

# 은행 대출이자 오름차순 정렬 
    path('loan_prdts_sorted_by_rate/<int:credit_score>/', views.loan_prdts_sorted_by_rate),

# 신용점수 대비 합리적인 이율상품 추천 => 추천에  



   # path('deposit_list/<str:deposit_code>/contract/', views.contract_deposit, name='contract_deposit'),
   # path('saving_list/<str:saving_code>/contract/', views.contract_saving, name='contract_saving'),

   # path('get_bank_deposit/<str:kor_co_nm>/', views.get_bank_deposit),
   # path('get_bank_saving/<str:kor_co_nm>/', views.get_bank_saving),
   # path('recommend_product_one/', views.recommend_product_one),
   # path('recommend_product_two/', views.recommend_product_two),
   # path('make_financial_data/', views.make_financial_data)
]