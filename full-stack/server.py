from http.server import HTTPServer, BaseHTTPRequuestHandler

class Handler(BaseHTTPRequuestHandler):
    def do_sth_for_GET(self):
        self.send_response(200)
        self.send_header('Content_type','text/plain;charset=utf-8')
        self.end_header()

        self.wfile.write("Hello everyone, I am AI server~\n".encode())

if __name__ =='__main__':
    server_address=('',8000)
    httpd=HTTPServer(server_address,Handler)
    httpd.serve_forever()
