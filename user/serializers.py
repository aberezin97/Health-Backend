from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user.models import User, Product


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password',)

    def get_image(self, user):
        image = None
        try:
            image = user.image.url
        except ValueError:
            return image
        request = self.context.get('request')
        if request is None:
            return image
        return request.build_absolute_uri(image)


class UserSerializerShort(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image']

    def get_image(self, user):
        image = None
        try:
            image = user.image.url
        except ValueError:
            return image
        request = self.context.get('request')
        if request is None:
            return image
        return request.build_absolute_uri(image)


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


class UserDefaultGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'default_goal_liquid',
            'default_limit_calories',
            'default_limit_proteins',
            'default_limit_fats',
            'default_limit_carbohydrates',
            'default_goal_calories',
            'default_goal_proteins',
            'default_goal_fats',
            'default_goal_carbohydrates'
        )
        extra_kwargs = {
            'default_goal_liquid': {
                'required': True,
            },
            'default_limit_calories': {
                'required': True,
            },
            'default_limit_proteins': {
                'required': True,
            },
            'default_limit_fats': {
                'required': True,
            },
            'default_limit_carbohydrates': {
                'required': True,
            },
            'default_goal_calories': {
                'required': True,
            },
            'default_goal_proteins': {
                'required': True,
            },
            'default_goal_fats': {
                'required': True,
            },
            'default_goal_carbohydrates': {
                'required': True,
            },
        }