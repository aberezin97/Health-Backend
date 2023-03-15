from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import FormParser, MultiPartParser, CamelCaseJSONParser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import generics, status, permissions
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.hashers import check_password
from user.models import User, Product
from user.serializers import SignUpSerializer, UserSerializer, UserSerializerShort, ChangeUserPasswordSerializer, ChangeUserDataSerializer, ChangeUserImageSerializer, DeleteUserSerializer, UserProductSerializer
from user.tokens import account_activation_token
from user.permissions import IsOwner, IsProductOwner


# Create your views here.
class UsersAPIView(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializerShort
    permission_classes = (permissions.IsAuthenticated,)


class UserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializerShort
    permission_classes = (permissions.IsAuthenticated,)


class SignInAPIView(ObtainAuthToken):
    parser_classes = (FormParser, MultiPartParser, CamelCaseJSONParser)
    renderer_classes = (CamelCaseJSONRenderer,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'data': UserSerializer(user, context={'request': request}).data
        })


class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class ActivateUserAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = User

    def update(self, request, *args, **kwargs):
        try:
            uidb64 = kwargs['uidb64']
            token = kwargs['token']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            uid = force_str(urlsafe_base64_decode(uidb64).decode())
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            user_token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': user_token.key,
                'data': UserSerializer(user, context={'request': request}).data
            })
            # return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangeUserPasswordAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = ChangeUserPasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.update(request.user, serializer.validated_data)
        return Response(UserSerializer(instance, context={'request': request}).data)


class ChangeUserDataAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    serializer_class = ChangeUserDataSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.update(request.user, serializer.validated_data)
        return Response(UserSerializer(instance, context={'request': request}).data)


class ChangeUserImageAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ChangeUserImageSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.update(request.user, serializer.validated_data)
        return Response(UserSerializer(instance, context={'request': request}).data)


class DeleteUserAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DeleteUserSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=request.user.pk)
        current_password = user.password
        password = serializer.validated_data['password']
        if check_password(password, current_password):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProductSerializer

    def list(self, request, *args, **kwargs):
        products = Product.objects.filter(user=request.user)
        return Response(UserProductSerializer(products, many=True).data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(user=request.user, **serializer.validated_data)
        return Response(UserProductSerializer(product).data)


class UserProductDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsProductOwner)
    serializer_class = UserProductSerializer