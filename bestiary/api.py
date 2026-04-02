from rest_framework import generics, permissions, filters
from .models import Monster
from .serializers import MonsterSerializer
from .permissions import IsOwnerOrReadOnly

class MonsterListCreateAPI(generics.ListCreateAPIView):
    serializer_class = MonsterSerializer
    # everyone can read but only logged in users and profiles can edit/create
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['monster_name', 'my_notes']
    ordering_fields = ['level_of_danger', 'monster_name']

    def get_queryset(self):
        return Monster.objects.filter(hunter=self.request.user.profile)

    def perform_create(self, serializer):
        serializer.save(hunter = self.request.user.profile)

class MonsterDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MonsterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Monster.objects.filter(hunter=self.request.user.profile)