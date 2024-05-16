from django.db import models
from django.contrib.auth.models import AbstractUser

# # -------- 모델링 목록 ------------
# # user_id (Var)
# # password (var)
# # first_name 이름 (var)
# # last_name 성 (var)
# # email (email)
# # nickname (var)
# # profile_img(blank=True)
# # finance_prdt_list(list)
# # age (integer)
# # balance (통장 잔고) (integer)
# # salary (연봉) (integer)
# # debt  (대출금액) (integer)
# # credit_score (신용점수) (float)
# # is_superuser (boolean)

class User(AbstractUser):
    pass
#    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
#    nickname = models.CharField(max_length=30, unique=True)
#    first_name = models.CharField(max_length=20)    # 이름
#    last_name = models.CharField(max_length=20)     # 성
#    email = models.EmailField(max_length=100, blank=True, unique=True, null=True)
#    profile_img = models.ImageField(upload_to='image/',  default='image/user.png')
#    finance_prdt_list = models.TextField(blank=True, null=True)
#    age = models.IntegerField(blank=True, null=True)
#    balance = models.IntegerField(blank=True, null=True)
#    salary = models.IntegerField(blank=True, null=True)
#    debt = models.IntegerField(blank=True, null=True)
#    credit_score = models.FloatField(blank=True, null=True)
#    is_superuser = models.BooleanField(default=False)



