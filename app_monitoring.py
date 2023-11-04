import http.server
from prometheus_client import start_http_server


class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Construct the response content
        response_content = bytes(
            "<html><head><title>First Python Application</title></head>"
            "<body style='color: #333; margin-top: 30px;'>"
            "<h1>Welcome to my first Python application!</h1>"
            "<p>This is a paragraph in the application.</p>"
            "</body></html>",
            "utf-8"
        )

        # Respond with the content
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(response_content)))
        self.end_headers()
        self.wfile.write(response_content)
        # Do not manually close self.wfile, it's handled by the underlying http.server logic

if __name__ == "__main__":
    start_http_server(5001)
    server_address = ('', 5000)  # '' is equivalent to 'localhost'
    httpd = http.server.HTTPServer(server_address, HandleRequests)
    print(f"Server started on localhost:{server_address[1]}")
    httpd.serve_forever()
