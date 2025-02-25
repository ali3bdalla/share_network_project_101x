import http.server
import socketserver

PORT = 8000

# Comment

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
# this comment has been added to the file locally
print("Contribution from Alex")