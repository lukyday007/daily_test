from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Article, Comment, Category


# 게시글 전체 조회 
class ArticleListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        model = get_user_model()
    
    # 닉네임 포함 
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'article_content', 'category', 'user', )
        read_only_fields = ['like_users']


# 단일 게시글 조회 
class ArticleSerializer(serializers.ModelSerializer):
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'article_content', )
    
    comment_set = CommentDetailSerializer(read_only=True, many=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


# 전체 댓글 조회
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'article', ]
    

# 카테고리가 있는 게시글 => views.py에 사용하지 않음, 일단 구상만
class CategorySerializer(serializers.ModelSerializer):
    article_set = ArticleListSerializer(read_only=True, many=True) 

    class Meta:
        model = Category
        fields = '__all__'


# 아이디로 게시글 조회 
class UserArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'article_content', 'category', )

class UserSerializer(serializers.ModelSerializer):
    article_set = UserArticleListSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'article_set', )


    



