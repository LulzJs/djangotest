from web.models import Question, Choice
from rest_framework import viewsets
from webservices.serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-pub_date')
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer