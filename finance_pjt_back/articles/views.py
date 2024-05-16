from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, UserSerializer
from .models import Article, Comment

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    # 게시글 조회 
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시글 생성 
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=request.user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 단일 게시글 조회 
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 단일 게시글 삭제 
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 단일 게시글 수정 
    elif request.method == 'PUT':
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # 해당 게시글 전체 댓글 조회
    if request.method == 'GET':
        comments = get_list_or_404(Comment, article=article)
        # 직렬화 진행
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    # 해당 게시글 댓글 생성 
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
        # 1
        # postman 콘솔에 this field is required 는 게시글의 외래키가 입력되지 않아서 생기는 오류 
            # commit=False 가 없고 
            # article=article로 해당 게시글 정보를 넣어주자! 
            # 하지만 여전히 오류 ... 왜?
            # 2
            # 유효성 검사에서 외래키가 걸리기 때문! 
            # solution : read-only로 바꿔주자! -> serializers.py

            # 해당 article 정보를 제공  
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):

    comment = get_object_or_404(Comment, pk=comment_pk)

    # 단일 댓글 삭제 
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # 단일 댓글 수정 
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)\
                

# 아이디로 게시글 조회 
@api_view(['GET'])
def get_list_by_user(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    user_articles = user.article_set.all()
    serializer = UserSerializer(user_articles, many=True)
    return Response(serializer.data)


