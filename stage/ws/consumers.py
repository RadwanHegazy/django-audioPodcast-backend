from channels.generic.websocket import WebsocketConsumer
from ..models import Stage

class StageConsumer(WebsocketConsumer) : 

    def connect(self):
        stage_id = self.scope['url_route']['kwargs']['stage_id']
        
        try : 
            self.stage = Stage.objects.get(id=stage_id)
            self.accept()
        except Stage.DoesNotExist:
            self.close()
            return

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        print("recived : ", text_data)

    