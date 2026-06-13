import http.server
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, "websites", "osdev_wiki")

class OSDevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, directory=TARGET_DIR, **kwargs)

    def end_headers(self):
        if "." not in self.path.split('/')[-1].split('?')[0]:
            self.send_header("Content-Type", "text/html")
        super().end_headers()

if __name__ == '__main__':
    print(f"streaming {TARGET_DIR}")
    http.server.test(HandlerClass=OSDevHandler, port=8080, bind='127.0.0.1')
