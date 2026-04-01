from rest_framework import generics, permissions
from .models import Quest
from .serializers import QuestSerializer
from .permissions import IsOwnerOrReadOnly

class QuestListApi(generics.ListCreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(profile = self.request.user.profile)

class QuestDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]