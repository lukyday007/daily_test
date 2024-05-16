# from django.shortcuts import render, redirect
# from django.contrib.auth import login as auth_login
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# # from .forms import ReviewerChangeForm, ReviewerCreationForm

# # login.html 렌더링    => GET
# # 로그인 절차 진행 후 index로 리다이렉트    => POST 
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('movies:index')

#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('movies:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)

# # DB와 클라이언트의 쿠키에서 인증된 사용자의 세션 데이터 삭제   => POST
# @login_required
# def logout(request):
#     auth_logout(request)
#     return redirect('movies:index')

# # sign.html 렌더링      => GET
# # 유효성 검증 및 회원 데이터 저장 후 index로 리다이렉트     => POST
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('movies:index')

#     if request.method == 'POST':
#         form = ReviewerCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('movies:index')
#     else:
#         form = ReviewerCreationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/signup.html', context)


# @login_required
# def delete(request):
#     request.user.delete()
#     return redirect('movies:index')


# @login_required
# def update_userinfo(request):
#     if request.method == 'POST':
#         form = ReviewerChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('movies:index')
#     else:
#         form = ReviewerChangeForm(instance=request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/update_userinfo.html', context)


# @login_required
# def password_change(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('movies:index')
#     else:
#         form = PasswordChangeForm(user = request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/password_change.html', context)

# # profile.html 렌더링   => POST
# # 단일 회원 데이터 및 작성한 영화, 댓글, 팔로우 수, 팔로잉 수 조회 
# def profile(request, username):
#     User = get_user_model()
#     member = User.objects.get(username=username)
#     context = {
#         'member': member,
#     }
#     return render(request, 'accounts/profile.html', context)    

# @login_required
# def follow(request, user_pk):
#     me = request.user
#     you = get_user_model().objects.get(pk=user_pk)

#     if me != you:
#         if me in you.followers.all():
#             you.followers.remove(me)
#         else:
#             you.followers.add(me)
#     return redirect('accounts:profile', you.username)


