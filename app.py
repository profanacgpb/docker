from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        mensagem = "Minha primeira aplicação web em Python!"
        corpo = mensagem.encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers("content-length", str(len(corpo)))
        self.end_headers()
        self.wfile.write(corpo)

servidor = HTTPServer(('0.0.0.0', 8000), RequestHandler)
print("Aplicação iniciada na porta 8000", flush=True)
servidor.serve_forever()
