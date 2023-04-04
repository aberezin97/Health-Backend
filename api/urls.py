from user.views import (
    UsersAPIView,
    SignInAPIView,
    SignUpAPIView,
    DeleteUserAPIView,
    ActivateUserAPIView,
    UserProductsAPIView,
    UserProductDetailsAPIView,
    ChangeUserPasswordAPIView,
    ChangeUserDataAPIView,
    ChangeUserImageAPIView,
    UserAPIView,
    UserDefaultGoalsAPIView,
    PermissionsAPIView,
    ModifyPermissionsAPIView,
    CreatePermissionsAPIView
)
from nutrition.views import (
    ModifyGoalsAPIView,
    NutritionAPIView,
    ModifyNutritionAPIView,
    LiquidAPIView,
    DeleteLiquidAPIView
)
from weight.views import WeightAPIView, ModifyWeightAPIView
from stats.views import StatsAPIView
from exercises.views import ExercisesAPIView, ModifyExerciseAPIView
from django.urls import path, include

urlpatterns = [
    path('user/<int:pk>/', UserAPIView.as_view()),
    path('user/', UsersAPIView.as_view()),
    path('user/signin/', SignInAPIView.as_view()),
    path('user/signup/', SignUpAPIView.as_view()),
    path('user/delete/', DeleteUserAPIView.as_view()),
    path('user/activate/<str:uidb64>/<str:token>/', ActivateUserAPIView.as_view()),
    path('user/password_reset/', include('django_rest_passwordreset.urls')),
    path('user/products/', UserProductsAPIView.as_view()),
    path('user/products/<int:pk>/', UserProductDetailsAPIView.as_view()),
    path('user/permissions/', PermissionsAPIView.as_view()),
    path('user/create_permission/', CreatePermissionsAPIView.as_view()),
    path('user/permissions/<int:pk>/', ModifyPermissionsAPIView.as_view()),
    path('user/change_password/', ChangeUserPasswordAPIView.as_view()),
    path('user/change_data/', ChangeUserDataAPIView.as_view()),
    path('user/change_image/', ChangeUserImageAPIView.as_view()),
    path('user/default_goals/', UserDefaultGoalsAPIView.as_view()),
    path('<int:user_id>/nutrition/<int:year>/<int:month>/<int:day>/modify_goals/', ModifyGoalsAPIView.as_view()),
    path('<int:user_id>/nutrition/<int:year>/<int:month>/<int:day>/', NutritionAPIView.as_view()),
    path('nutrition/<int:pk>/', ModifyNutritionAPIView.as_view()),
    path('<int:user_id>/nutrition/modify_goals/', ModifyGoalsAPIView.as_view()),
    path('<int:user_id>/nutrition/', NutritionAPIView.as_view()),
    path('<int:user_id>/nutrition/liquid/', LiquidAPIView.as_view()),
    path('nutrition/liquid/<int:pk>/', DeleteLiquidAPIView.as_view()),
    path('<int:user_id>/exercises/', ExercisesAPIView.as_view()),
    path('<int:user_id>/exercises/<int:year>/<int:month>/<int:day>/', ExercisesAPIView.as_view()),
    path('exercises/<int:pk>/', ModifyExerciseAPIView.as_view()),
    path('weight/<int:pk>/', ModifyWeightAPIView.as_view()),
    path('<int:user_id>/weight/', WeightAPIView.as_view()),
    path('<int:user_id>/stats/', StatsAPIView.as_view()),
]
