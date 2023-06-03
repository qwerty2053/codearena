from django.urls import include, path
from rest_framework import routers
# from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from problemset.views import ProblemViewSet
from contests.views import ContestViewSet
from submissions.views import SubmissionViewSet


router = routers.DefaultRouter()
router.register(r'problemset', ProblemViewSet, basename='problemset')
router.register(r'contest', ContestViewSet, basename='contest')
router.register(r'submission', SubmissionViewSet, basename='submission')


urlpatterns = [
    path('', include(router.urls)),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
