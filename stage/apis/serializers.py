from stage.models import Stage
from rest_framework import serializers

class StageSerializer(serializers.ModelSerializer) : 

    class Meta:
        fields = ['title','id']
        model = Stage

    def validate(self, attrs):
        attrs['owner'] = self.context.get('user')
        return attrs
    
    def to_representation(self, instance:Stage):
        data = super().to_representation(instance)
        data['owner'] = {
            'id' : instance.owner.id,
            'full_name' : instance.owner.full_name,
            'picture' : instance.owner.picture.url,
        }
        return data
    