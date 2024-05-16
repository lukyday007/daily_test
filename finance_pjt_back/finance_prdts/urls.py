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


#    # path('deposit/6months/', views.get_deposits, {'save_trm': '6'}),
#    # path('deposit/12months/', views.get_deposits, {'save_trm': '12'}),
#    # path('deposit/24months/', views.get_deposits, {'save_trm': '24'}),
#    # path('deposit/36months/', views.get_deposits, {'save_trm': '36'}),
#    # path('saving/6months/', views.get_savings, {'save_trm': '6'}),
#    # path('saving/12months/', views.get_savings, {'save_trm': '12'}),
#    # path('saving/24months/', views.get_savings, {'save_trm': '24'}),
#    # path('saving/36months/', views.get_savings, {'save_trm': '36'}),
#    # path('deposit/-6months/', views.get_reverse_deposits, {'save_trm': '6'}),
#    # path('deposit/-12months/', views.get_reverse_deposits, {'save_trm': '12'}),
#    # path('deposit/-24months/', views.get_reverse_deposits, {'save_trm': '24'}),
#    # path('deposit/-36months/', views.get_reverse_deposits, {'save_trm': '36'}),
#    # path('saving/-6months/', views.get_reverse_savings, {'save_trm': '6'}),
#    # path('saving/-12months/', views.get_reverse_savings, {'save_trm': '12'}),
#    # path('saving/-24months/', views.get_reverse_savings, {'save_trm': '24'}),
#    # path('saving/-36months/', views.get_reverse_savings, {'save_trm': '36'}),
#    # path('deposit_list/<str:deposit_code>/contract/', views.contract_deposit, name='contract_deposit'),
#    # path('saving_list/<str:saving_code>/contract/', views.contract_saving, name='contract_saving'),
#    # path('get_bank_deposit/<str:kor_co_nm>/', views.get_bank_deposit),
#    # path('get_bank_saving/<str:kor_co_nm>/', views.get_bank_saving),
#    # path('recommend_product_one/', views.recommend_product_one),
#    # path('recommend_product_two/', views.recommend_product_two),
#    # path('make_financial_data/', views.make_financial_data)
]