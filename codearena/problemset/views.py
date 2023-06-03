from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Problem
from .serializers import ProblemDetailSerializer, ProblemSerializer


class ProblemViewSet(ReadOnlyModelViewSet):
    queryset = Problem.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProblemDetailSerializer
        return ProblemSerializer
