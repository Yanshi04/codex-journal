from rest_framework import generics, permissions
from .models import Quest
from .serializers import QuestSerializer
from .permissions import IsOwnerOrReadOnly

class QuestListApi(generics.ListCreateAPIView):
    serializer_class = QuestSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Quest.objects.filter(profile=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(profile = self.request.user.profile)

class QuestDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestSerializer

    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Quest.objects.filter(profile=self.request.user.profile)