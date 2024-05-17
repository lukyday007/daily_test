from django.urls import path
from . import views

urlpatterns = [
    # 게시글 조회, 생성
    path('', views.article_list),

    # 단일 게시글 조회, 삭제, 수정 
    path('<int:article_pk>/', views.article_detail),

    # 해당 게시글 전체 댓글 조회, 생성
    path('<int:article_pk>/comments/', views.comment_list),

    # 해당 게시글 삭제, 수정 
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),

    # 아이디로 게시글 조회 
    path('<str:username>/', views.get_list_by_user),

    # 금융별 게시글 조회? -> 아이디어
    
]
