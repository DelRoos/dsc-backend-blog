from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    name = SerializerMethodField()
    email = SerializerMethodField()
    description = SerializerMethodField()
    image = SerializerMethodField()
    tel = SerializerMethodField()
    location = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
                    'id',
                    'name',
                    'email', 
                    'description', 
                    'image', 
                    'tel',
                    'github',
                    'linked_in',
                    'location', 
                    'created_at', 
                ]

    def get_email(self, obj):
        return str(obj.profile.user.email)

    def get_name(self, obj):
        return str(obj.profile.user.username)

    def get_description(self, obj):
        return str(obj.profile.description)

    def get_image(self, obj):
        return str(obj.profile.image)

    def get_tel(self, obj):
        return str(obj.profile.tel)

    def get_github(self, obj):
        return str(obj.profile.github)
    
    def get_linked_in(self, obj):
        return str(obj.profile.linked_in)

    def get_location(self, obj):
        return str(obj.profile.location)
    
    def get_created_at(self, obj):
        return str(obj.profile.created_at)

class UserProfileDetailSerializer(serializers.ModelSerializer):
    name = SerializerMethodField()
    email = SerializerMethodField()
    description = SerializerMethodField()
    image = SerializerMethodField()
    tel = SerializerMethodField()
    location = SerializerMethodField()
    created_at = SerializerMethodField()
    is_redactor = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
                    'id',
                    'name',
                    'email', 
                    'description', 
                    'image', 
                    'tel',
                    'github',
                    'linked_in',
                    'location', 
                    'created_at',
                    'is_redactor',
                ]

    def get_email(self, obj):
        return str(obj.email)

    def get_name(self, obj):
        return str(obj.username)

    def get_description(self, obj):
        return str(obj.profile.description)

    def get_image(self, obj):
        return str(obj.profile.image)

    def get_tel(self, obj):
        return str(obj.profile.tel)

    def get_github(self, obj):
        return str(obj.profile.github)
    
    def get_linked_in(self, obj):
        return str(obj.profile.linked_in)

    def get_location(self, obj):
        return str(obj.profile.location)
    
    def get_created_at(self, obj):
        return str(obj.profile.created_at)
    
    def get_is_redactor(self, obj):
        return str(obj.profile.is_redactor)

class ProfileDetailSerializer(serializers.ModelSerializer):
    name = SerializerMethodField()
    email = SerializerMethodField()
    description = SerializerMethodField()
    image = SerializerMethodField()
    tel = SerializerMethodField()
    location = SerializerMethodField()
    created_at = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
                    'id',
                    'name',
                    'email', 
                    'description', 
                    'image', 
                    'tel',
                    'github',
                    'linked_in',
                    'location', 
                    'created_at',
                    'is_redactor'
                ]

    def get_email(self, obj):
        return str(obj.user.email)

    def get_name(self, obj):
        return str(obj.user.username)

    def get_description(self, obj):
        return str(obj.description)

    def get_image(self, obj):
        return str(obj.image)

    def get_tel(self, obj):
        return str(obj.tel)

    def get_github(self, obj):
        return str(obj.github)
    
    def get_linked_in(self, obj):
        return str(obj.linked_in)

    def get_location(self, obj):
        return str(obj.location)
    
    def get_created_at(self, obj):
        return str(obj.created_at)

class UserListPostSerializer(serializers.ModelSerializer):
    formations = SerializerMethodField()
    posts = SerializerMethodField()
    
    class Meta:
        model = User
        fields = (
            'formations',
            'posts',
        )
    
    def get_posts(self, obj):
        posts = obj.posts_user.all()
        posts_data = []
        for post in posts:
            item = {
                'slug':post.slug,
                'title':post.title,
                'category':post.category.title,
                'description':post.description, 
                'banner':post.banner,
                'publish_at':post.publish_at,
                'status': post.status
            }
            posts_data.append(item)
        return posts_data
    
    def get_formations(self, obj):
        formations = obj.formation_user.all()
        formations_data = []
        for formation in formations:
            item = {
                'slug':formation.slug,
                'title':formation.title,
                'category':formation.formation_category.title,
                'description':formation.description, 
                'banner':formation.banner,
                'publish_at':formation.publish_at,
                'status': formation.status
            }
            formations_data.append(item)
        return formations_data