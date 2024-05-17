from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_field, user_username
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    balance = models.IntegerField()
    debt = models.IntegerField()
    creditscore = models.IntegerField()
    joinproduct = models.CharField(max_length=100)
    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile_image/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
    )
# class CustomAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=True):
#         data = form.cleaned_data
#         first_name = data.get("first_name")
#         last_name = data.get("last_name")
#         email = data.get("email")
#         username = data.get("username")

#         nickname = data.get("nickname")
#         age = data.get("age")
#         salary = data.get("salary")
#         balance = data.get("balance")
#         debt = data.get("debt")
#         creditscore = data.get("creditscore")

#         user = super().save_user(request, user, form, False)
#         # 추가 저장 필드: profile_image
        
#         if first_name:
#             user_field(user, "first_name", first_name)
#         if last_name:
#             user_field(user, "last_name", last_name)
#         if email:
#             user_field(user, "email", email)
#         if username:
#             user_field(user, "username", username)
#         if nickname:
#             user_field(user, "nickname", nickname)
#         if age:
#             user_field(user, "age", age)
#         if salary:
#             user_field(user, "salary", salary)
#         if balance:
#             user_field(user, "balance", balance)
#         if debt:
#             user_field(user, "debt", debt)
#         if creditscore:
#             user_field(user, "creditscore", creditscore)
#         if "password1" in data:
#             user.set_password(data["password1"])
#         else:
#             user.set_unusable_password()
#         self.populate_username(request, user)
#         # if commit:
#         user.save()
#         return user

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

# class User(AbstractUser):
#     pass
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



