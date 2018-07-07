from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint
import pymysql
import json



# def autorisation(ip):
#     sessions = open('sessions.dat', 'r')
#     sessions_r = sessions.read()
#     sessions.close()
#     print(sessions_r)
#
#     if not(ip in sessions_r):
#         print(ip+' in '+sessions_r)
#         print(ip in sessions_r)
#         print(type(ip), type(sessions_r))
#         sessions = open('sessions.dat', 'a')
#         sessions.write(ip+' ')
#         sessions.close()


# def get_id():
#     sessions = open('sessions.dat', 'r')
#     sessions_r = sessions.read()
#     sessions.close()
#
#     sessions = open('sessions.dat', 'a')
#
#     if free_users:
#         num = min(free_users)  # id
#     else:
#         num = len(sessions_r.split())  # id
#
#     sessions.write(str(num)+' ')
#     sessions.close()
#     return str(num)


# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False

def new_item(a):
    cursor.execute('select * from main')
    fetch = cursor.fetchall()
    n = len(fetch) + 1
    l = a.replace('%20', ' ').split('|')
    print(l)
    print("insert into main values("+str(n)+", '"+l[0]+"', '"+l[1]+"', '"+l[2]+"')")
    cursor.execute("insert into main values("+str(n)+", '"+l[0]+"', '"+l[1]+"', '"+l[2]+"')")
    db.commit()
    fetch = cursor.fetchall()
    print(fetch)


# def del_item(num, n_item):
#     favors = open('users/'+num, 'r')
#     favors_r = favors.read()
#     favors.close()
#
#     favors =  open('users/'+num, 'r')


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        a = self.raw_requestline.decode().split()[1][1:]

        if a.split('/')[0] == "hello":
            self.wfile.write(b'u a welcome')
        elif a.split('/')[0] == 'getrandom':
            cursor.execute("select * from main")
            db = cursor.fetchall()
            db = db[randint(0, len(db)-1)]
            db = {'name': db[1],
                  'img': db[2],
                  'url': db[3]}
            self.wfile.write(json.dumps(db).encode())
            # db = open("db.dat", "r")
            # db_r = db.read()
            # db_r = db_r.split('\n')
            # line = db_r[randint(0, len(db_r) - 1)]
            # db.close()
            # self.wfile.write(line.encode())
        # elif a.split('/')[0] == 'getid':
        #     self.wfile.write(get_id())
        elif a[:7] == 'newitem':
            pprint(a[8:])
            new_item(a[8:])
        else:
            self.wfile.write(b'He110')

    def do_POST(self):
        body = self.rfile.read()

        print(body)

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Не110!'.encode())


if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "gfhjkm", "doni")
    cursor = db.cursor()
    cursor.execute("use doni")
    # free_users = []
    serv = HTTPServer(("127.0.0.1", 430), HttpProcessor)
    serv.serve_forever()
    db.close()
