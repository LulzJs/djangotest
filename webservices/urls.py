from rest_framework import routers
from webservices.views import QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)