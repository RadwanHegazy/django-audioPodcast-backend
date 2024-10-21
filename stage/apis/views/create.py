from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView
from ..serializers import StageSerializer

class CreateStage(CreateAPIView) : 
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StageSerializer

    def get_serializer_context(self):
        return {
            'user' : self.request.user
        }