from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'email': {
                'required': True
            },
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.is_active = False
        user.save()
        return user


class ChangeUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({'old_password': 'Old password is not correct'})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class ChangeUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {
                'required': True,
                'validators': []
            },
            'first_name': {
                'required': True,
            },
            'last_name': {
                'required': True,
            }
        }

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value


class ChangeUserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image',)
        extra_kwargs = {
            'image': {
                'required': True,
            }
        }


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password',)


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'calories',
            'proteins',
            'fats',
            'carbohydrates',
        )
        extra_kwargs = {
            'name': {
                'required': True,
            },
            'calories': {
                'required': True,
            },
            'proteins': {
                'required': True,
            },
            'fats': {
                'required': True,
            },
            'carbohydrates': {
                'required': True,
            },
        }