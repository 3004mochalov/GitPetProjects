import tkinter as tk
from flask import Flask, render_template
import threading
import webbrowser
import dns.resolver  # Добавляем библиотеку dnspython
import requests  # Добавляем библиотеку requests

app_flask = Flask(__name__)


@app_flask.route('/')
def hello():
    return 'Привет, мир! Это мой сайт на Python с использованием Flask.'


def run_flask():
    app_flask.run(debug=True)


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мой сайт на Python")

        # Добавляем текст на окно
        label = tk.Label(root, text="Привет, мир! Это мой сайт на Python.")
        label.pack(padx=20, pady=20)

        # Добавляем кнопку для открытия веб-сайта
        button = tk.Button(root, text="Открыть сайт", command=self.open_website)
        button.pack(pady=10)

    def open_website(self):
        # Получаем IP-адрес Flask-сервера
        flask_ip = "127.0.0.1"  # Замените на реальный IP-адрес Flask-сервера

        # Запускаем Flask в отдельном потоке
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()

        # Ждем, пока Flask запустится
        while not is_flask_running(flask_ip):
            pass

        # Настраиваем DNS-записи
        configure_dns_records(flask_ip)

        # Открываем веб-сайт
        webbrowser.open('http://www.ваш-домен.com')


def is_flask_running(ip):
    try:
        response = webbrowser.open(f'http://{ip}:5000')
        return response is not None
    except:
        return False


def configure_dns_records(ip):
    # Замените на свои реальные данные
    domain = "ваш-домен.com"
    dns_provider_username = "ваш-логин"
    dns_provider_password = "ваш-пароль"

    # Пример работы с DNS-записями с использованием dnspython
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8']  # Используем DNS Google, можно заменить на другие

    # Создаем A-запись для домена, направляя ее на IP-адрес Flask-сервера
    a_record = dns.resolver.ResourceRecord(domain, dns.rdatatype.A, dns.rdataclass.IN, 300, dns.rdata.A(ip))

    # Добавляем запись (может потребовать��я аутентификация)
    # Пример, используя сервис Cloudflare (замените на своего DNS-поставщика)
    dns_update_url = "https://api.cloudflare.com/client/v4/zones/ваш-zone-id/dns_records"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {dns_provider_password}"
    }
    data = {
        "type": "A",
        "name": domain,
        "content": ip,
        "ttl": 300,
        "proxied": False
    }
    response = requests.post(dns_update_url, json=data, headers=headers)


if __name__ == "__main__":
    # Запускаем Tkinter
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
