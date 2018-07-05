from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        a = self.raw_requestline.decode().split()[1][1:]
        if a == "hello":
            self.wfile.write(b'u a welcome')
        elif isint(a):
            db = open("db.", "r").read()
            db = db.split('\n')
            line = db[randint(0, len(db) - 1)]
            self.wfile.write(line.encode())
        else:
            self.wfile.write(b'He110')




    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read()

        print(body)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Не110!'.encode())


if __name__ == '__main__':
    #serv = HTTPServer(("85.140.1.241", 430), HttpProcessor)
    serv = HTTPServer(("127.0.0.1", 430), HttpProcessor)
    #serv = HTTPServer(("77.108.206.208", 430), HttpProcessor)
    serv.serve_forever()
