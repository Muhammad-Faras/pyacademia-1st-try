from channels.consumer import SyncConsumer
import json
from asgiref.sync import async_to_sync
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('user = ', self.scope["user"])
        print('------------------ websocker_connect--------------')
        print('websocket connect...', event)
        print('channel layer...', self.channel_layer)   # channel layer
        print('channel layer...', self.channel_name)   # channel name
        # all methods are written in async consumers so firstly we have to change asyns_to_sync
        async_to_sync(self.channel_layer.group_add)(
            'programmers',
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept'
        })
    
    def websocket_receive(self, event):
        print('------------------ websocket receive--------------')
        print(event['text'])
        if self.scope['user'].is_authenticated:
             async_to_sync(self.channel_layer.group_send)('programmers',{
            'type': 'chat.message',
            'message':event['text']
            })
        else:
            response = {
            'msg': 'user is not authenticated'
            }
            json_response = json.dumps(response)
            self.send({
            'type': 'websocket.send',
            'text': json_response,
            })
    def chat_message(self, event):
        print('Event...',event)
        print('Event...',event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        }
        )
    def websocket_disconnect(self, event):
        print('------------------ websocker_disconnect--------------')
        print('websocket connect...', event)
        print('(disconnect)channel layer...', self.channel_layer)   # channel layer
        print('(disconnect)channel layer...', self.channel_name)   # channel name
        # all methods are written in async consumers so firstly we have to change asyns_to_sync
        async_to_sync(self.channel_layer.group_discard)(
            'programmers',
            self.channel_name
        )