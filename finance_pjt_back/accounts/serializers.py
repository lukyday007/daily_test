from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=255)
    age = serializers.IntegerField(required=False, allow_null=True)
    salary = serializers.IntegerField(required=False, allow_null=True)
    balance = serializers.IntegerField(required=False, allow_null=True)
    debt = serializers.IntegerField(required=False, allow_null=True)
    creditscore = serializers.IntegerField(required=False, allow_null=True)
    profile_image = serializers.ImageField(required=False, allow_null=True, use_url=True)
    def get_cleaned_data(self):
        return {
            'profile_image': self.validated_data.get('profile_image', ''),
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'nickname': self.validated_data.get('nickname', ''),
            'age': self.validated_data.get('age', ''),
            'salary': self.validated_data.get('salary', ''),
            'balance': self.validated_data.get('balance', ''),
            'debt': self.validated_data.get('debt', ''),
            'creditscore': self.validated_data.get('creditscore', ''),
        }
    
UserModel = get_user_model()
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []

        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')
        if hasattr(UserModel, 'age'):
            extra_fields.append('age')
        if hasattr(UserModel, 'salary'):
            extra_fields.append('salary')
        if hasattr(UserModel, 'balance'):
            extra_fields.append('balance')
        if hasattr(UserModel, 'debt'):
            extra_fields.append('debt')
        if hasattr(UserModel, 'creditscore'):
            extra_fields.append('creditscore')
        if hasattr(UserModel, 'profile_image'):
            extra_fields.append('profile_image')
        model = UserModel
        fields = '__all__'
        # fields = ('pk', *extra_fields)
        read_only_fields = ('email',)