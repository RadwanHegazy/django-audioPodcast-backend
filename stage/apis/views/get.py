from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..serializers import StageSerializer, Stage

class GetAllStages(ListAPIView) :
    queryset =  Stage.objects.all()
    serializer_class = StageSerializer

class RetriveStage(RetrieveAPIView) : 
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field = 'id'
