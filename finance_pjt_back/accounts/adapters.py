from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        nickname = data.get("nickname")
        if nickname:
            user.nickname = nickname
        age = data.get("age")
        if age:
            user.age = age
        salary = data.get("salary")
        if salary:
            user.salary = salary
        balance = data.get("balance")
        if balance:
            user.balance = balance
        debt = data.get("debt")
        if debt:
            user.debt = debt
        creditscore = data.get("creditscore")
        if creditscore:
            user.creditscore = creditscore
        profile_image = data.get("profile_image")
        if profile_image:
            user.profile_image = profile_image

        user.save()
        return user
