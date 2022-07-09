from user.views import UsersAPIView, SignInAPIView, SignUpAPIView, DeleteUserAPIView, ActivateUserAPIView, \
    UserProductsAPIView, UserProductDetailsAPIView, ChangeUserPasswordAPIView, ChangeUserDataAPIView, ChangeUserImageAPIView
from nutrition.views import ModifyGoalsAPIView, NutritionAPIView, ModifyNutritionAPIView
from weight.views import WeightAPIView, ModifyWeightAPIView
from stats.views import StatsAPIView
from django.urls import path, include

urlpatterns = [
    path('user/', UsersAPIView.as_view()),
    path('user/signin/', SignInAPIView.as_view()),
    path('user/signup/', SignUpAPIView.as_view()),
    path('user/delete/', DeleteUserAPIView.as_view()),
    path('user/activate/<str:uidb64>/<str:token>/', ActivateUserAPIView.as_view()),
    path('user/password_reset/', include('django_rest_passwordreset.urls')),
    path('user/products/', UserProductsAPIView.as_view()),
    path('user/products/<int:pk>/', UserProductDetailsAPIView.as_view()),
    path('user/change_password/', ChangeUserPasswordAPIView.as_view()),
    path('user/change_data/', ChangeUserDataAPIView.as_view()),
    path('user/change_image/', ChangeUserImageAPIView.as_view()),
    path('nutrition/<int:year>/<int:month>/<int:day>/modify_goals/', ModifyGoalsAPIView.as_view()),
    path('nutrition/<int:year>/<int:month>/<int:day>/', NutritionAPIView.as_view()),
    path('nutrition/<int:pk>/', ModifyNutritionAPIView.as_view()),
    path('nutrition/modify_goals/', ModifyGoalsAPIView.as_view()),
    path('nutrition/', NutritionAPIView.as_view()),
    path('weight/<int:pk>/', ModifyWeightAPIView.as_view()),
    path('weight/', WeightAPIView.as_view()),
    path('stats/', StatsAPIView.as_view()),
]
