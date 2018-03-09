from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    CharField,
    EmailField,
)

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q

class UserCreateSerializer(ModelSerializer):
    cnfPassword = CharField(max_length = 50, label = "Confirm Password", write_only = True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'cnfPassword',
        ]
        # make password write only
        extra_kwargs = {
            'password':{
                'write_only':True,
            },
        }

    def validate_email(self, value):
        data = self.get_initial()
        user_qs = User.objects.filter(email=value)
        if user_qs.exists():
            raise ValidationError("User with this email address already exist!")
        return value
    def validate_cnfPassword(self, value):
        data = self.get_initial()
        # print(data)
        password = data.get('password')
        cnf_passoword = value
        if password != cnf_passoword:
            raise ValidationError("Confirm Password does not match")
        return value

    def create(self, validated_data):
        # print(validated_data)
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(read_only = True, allow_blank =True)
    username = CharField(required = False,allow_blank =True)
    email = EmailField(label = 'Email Address', required = False,allow_blank =True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token',
        ]
        write_only_fields = ['password']
        # make password write only
        extra_kwargs = {
            'password':{
                'write_only':True,
            },
        }

    def validate(self, data):
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password')
        user_obj = None
        token = None
        # check if email or username is provided
        if not email and not username:
            raise ValidationError("Email or Username is required")

        # check if user with that email or username is exist in database
        user = User.objects.filter(
            (Q(email__exact = email) & ~Q(email__iexact = ''))
            |Q(username = username)
        ).distinct()
        # print(username,email,"\nUser", user)

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Invalid username or email")

        # check if password is right
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Invalid credentials")
            else:
                # User is valid then generate Token
                token, _ = Token.objects.get_or_create(user = user_obj)
                print("Token", token)
        # generate token and pass it with data
        data["token"] = token.key
        # print(data)
        return data

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        read_only_fields = ['username']
