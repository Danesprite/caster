import json
import threading

from bottle import run, request
import bottle
from threading import Timer


class BottleServer:
    class Message:
        def __init__(self, content="", destination=""):
            self.content = content
            self.destination = destination
        
    def __init__(self, listening_port, lock=None):
        self.listening_port = listening_port
        self.lock = threading.Lock() if lock == None else lock
        self.incoming = []
        self.outgoing = []
        bottle.route('/process', method="POST")(self.receive_request)
        # make it nonblocking:
        Timer(0.1, self.start_run).start()
        
    def start_run(self):
        run(host='localhost', port=self.listening_port, debug=False, server='cherrypy')
    
    def receive_request(self):
        with self.lock: 
            self.incoming.append(json.loads(request.body.read()))
            # self.request_object = json.loads(request.body.read())
            # action_type = self.request_object["action_type"]
    
    def process_requests(self):
        '''override this'''









