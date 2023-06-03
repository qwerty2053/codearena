# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from .models import Submission
from .serializers import SubmissionSerializer, SubmissionWithCodeSerializer


class SubmissionViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):

    queryset = Submission.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SubmissionWithCodeSerializer
        return SubmissionSerializer
