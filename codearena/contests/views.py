from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Contest
from contests.serializers import ContestDetailSerializer, ContestSerializer


class ContestViewSet(ReadOnlyModelViewSet):
    queryset = Contest.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ContestDetailSerializer
        return ContestSerializer
