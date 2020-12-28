from rest_framework.serializers import SerializerMethodField
from rest_framework import serializers
from .models import UserProfile

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=False, allow_blank=True)
#     email = serializers.EmailField(required=False, allow_blank=True)
#     password = serializers.CharField(style={'input_type': 'password'})

#     def authenticate(self, **kwargs):
#         return authenticate(self.context['request'], **kwargs)

#     def _validate_email(self, email, password):
#         user = None

#         if email and password:
#             user = self.authenticate(email=email, password=password)
#         else:
#             msg = _('Must include "email" and "password".')
#             raise exceptions.ValidationError(msg)

#         return user

#     def _validate_username(self, username, password):
#         user = None

#         if username and password:
#             user = self.authenticate(username=username, password=password)
#         else:
#             msg = _('Must include "username" and "password".')
#             raise exceptions.ValidationError(msg)

#         return user

#     def _validate_username_email(self, username, email, password):
#         user = None

#         if email and password:
#             user = self.authenticate(email=email, password=password)
#         elif username and password:
#             user = self.authenticate(username=username, password=password)
#         else:
#             msg = _('Must include either "username" or "email" and "password".')
#             raise exceptions.ValidationError(msg)

#         return user

#     def get_auth_user_using_allauth(self, username, email, password):
#         from allauth.account import app_settings

#         # Authentication through email
#         if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
#             return self._validate_email(email, password)

#         # Authentication through username
#         if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
#             return self._validate_username(username, password)

#         # Authentication through either username or email
#         return self._validate_username_email(username, email, password)

#     def get_auth_user_using_orm(self, username, email, password):
#         if email:
#             try:
#                 username = UserModel.objects.get(email__iexact=email).get_username()
#             except UserModel.DoesNotExist:
#                 pass

#         if username:
#             return self._validate_username_email(username, '', password)

#         return None

#     def get_auth_user(self, username, email, password):
#         """
#         Retrieve the auth user from given POST payload by using
#         either `allauth` auth scheme or bare Django auth scheme.
#         Returns the authenticated user instance if credentials are correct,
#         else `None` will be returned
#         """
#         if 'allauth' in settings.INSTALLED_APPS:
#             return self.get_auth_user_using_allauth(username, email, password)
#         return self.get_auth_user_using_orm(username, email, password)

#     def validate_auth_user_status(self, user):
#         if not user.is_active:
#             msg = _('User account is disabled.')
#             raise exceptions.ValidationError(msg)

#     def validate_email_verification_status(self, user):
#         from allauth.account import app_settings
#         if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
#             email_address = user.emailaddress_set.get(email=user.email)
#             if not email_address.verified:
#                 raise serializers.ValidationError(_('E-mail is not verified.'))

#     def validate(self, attrs):
#         username = attrs.get('username')
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user = self.get_auth_user(username, email, password)

#         if not user:
#             msg = _('Unable to log in with provided credentials.')
#             raise exceptions.ValidationError(msg)

#         # Did we get back an active user?
#         self.validate_auth_user_status(user)

#         # If required, is the email verified?
#         if 'dj_rest_auth.registration' in settings.INSTALLED_APPS:
#             self.validate_email_verification_status(user)

#         attrs['user'] = user
#         return attrs
    

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