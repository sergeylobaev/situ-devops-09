"""Простое cloud-native приложение: минимальный HTTP-сервер."""

import http.server
import socketserver

PORT = 8000


class ServerInfo:
    """Вспомогательный класс с логикой приложения, покрытой тестами."""

    def take_four(self):
        """Возвращает число 4 (используется в юнит-тестах)."""
        return 4

    def port(self):
        """Возвращает порт, на котором слушает сервер."""
        return PORT


def main():
    """Запускает простой HTTP-сервер, отдающий файлы текущей директории."""
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
