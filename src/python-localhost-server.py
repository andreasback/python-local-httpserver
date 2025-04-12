import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CustomServer(SimpleHTTPRequestHandler):
  # https://stackoverflow.com/questions/39801718/how-to-run-a-http-server-which-serves-a-specific-path
  def __init__(self, *args, **kwargs):
    super().__init__(*args, directory='www', **kwargs)

  def do_GET(self):
    path = self.translate_path(self.path)
    #print(f'{self.path} -> {path}')

    if not os.path.exists(path):
      print('not found :)')
      index_path = self.translate_path('/index.html')

      if os.path.exists(index_path):
        print("redirecting to index.html")
        self.path = '/index.html'
      else:
        print("no index.html found to redirect to")

    SimpleHTTPRequestHandler.do_GET(self)

print("Server available at http://localhost:3000")
httpd = HTTPServer(('', 3000), CustomServer)
httpd.serve_forever()
