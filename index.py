import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
<<<<<<< HEAD

print("test github from VScode")
=======
print("Hello World") 
>>>>>>> 73491667d89f13c3f081617355d395fe7221856d
