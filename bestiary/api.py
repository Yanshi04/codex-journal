from rest_framework import generics, permissions
from .models import Monster
from .serializers import MonsterSerializer
from .permissions import IsOwnerOrReadOnly

class MonsterListCreateAPI(generics.ListCreateAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    # everyone can read but only logged in users and profiles can edit/create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(hunter = self.request.user.profile)

class MonsterDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]