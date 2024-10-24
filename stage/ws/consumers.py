from channels.generic.websocket import WebsocketConsumer
from ..models import Stage
import json
from asgiref.sync import async_to_sync

class StageConsumer(WebsocketConsumer) : 

    def connect(self):
        stage_id = self.scope['url_route']['kwargs']['stage_id']
        
        try : 
            self.stage = Stage.objects.get(id=stage_id)
        except Stage.DoesNotExist:
            self.close()
            return
        
        self.GROUP = f'group_{stage_id}'
        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP,
            self.channel_name
        )


    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        json_data = json.loads(text_data)
        action = json_data.get('action', None)

        if action == 'increase':
            total_counter = self.stage.visitor_counter + 1
            self.stage.visitor_counter = total_counter
            self.stage.save()
            async_to_sync(self.channel_layer.group_send)(
                self.GROUP,
                {
                    'type' : 'action',
                    'data' : {
                        'visitors' : total_counter
                    }
                }
            )

        if action == 'close':
            self.stage.delete()
            self.close()
            return

        async_to_sync(self.channel_layer.group_send)(
                self.GROUP,
                {
                    'type' : 'action',
                    'data' : json_data
                }
            )

    def action(self, data):
        self.send(text_data=json.dumps(data['data']))
