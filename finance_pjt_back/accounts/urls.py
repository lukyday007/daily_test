# from django.urls import path 
# from . import views

# app_name = 'accounts'
# urlpatterns = [
#     # login.html 렌더링    => GET
#     # 로그인 절차 진행 후 index로 리다이렉트    => POST 
#     path('login/', views.login, name='login'),

#     # DB와 클라이언트의 쿠키에서 인증된 사용자의 세션 데이터 삭제   => POST
#     path('logout/', views.logout, name='logout'),

#     # sign.html 렌더링      => GET
#     # 유효성 검증 및 회원 데이터 저장 후 index로 리다이렉트     => POST
#     path('signup/', views.signup, name='signup'),

#     # 단일 회원 데이터 삭제 및 index로 리다이렉트   => POST
#     path('delete/', views.delete, name='delete'),

#     # password_change.html 렌더링   => GET
#     # 비밀번호 변경 후 index로 리다이렉트   => POST 
#     path('password_change/', views.password_change, name='password_change'),

#     path('update_userinfo/', views.update_userinfo, name='update_userinfo'),
    
#     # profile.html 렌더링   => POST
#     # 단일 회원 데이터 및 작성한 영화, 댓글, 팔로우 수, 팔로잉 수 조회  
#     path('profile/<username>/', views.profile, name='profile'),

#     # 단일 회원 팔로우 기능 (이미 팔로우 한 경우 팔로우 취소)   => POST
#     # 팔로우 기능 동작 후 profile.html 로 리다이렉트     
#     path('follow/<int:user_pk>/', views.follow, name='follow'),

# ]