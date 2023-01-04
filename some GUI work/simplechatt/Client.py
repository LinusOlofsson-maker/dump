import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import socket
import threading

kivy.require("2.1.0")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def send_message(self):
        client.send(f"{self.nickname_text.text}: {self.message_text.text}".encode('utf-8'))

    def connect_to_server(self):
        if self.nickname_text != "":
            # print(self.ip_text.text)
            client.connect((self.ip_text.text, 5050))
            # client.connect(("127.0.0.1", 5050))
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(self.nickname_text.text.encode('utf-8'))
                self.send_btn.disabled = False
                self.message_text.disabled = False
                self.connect_btn.disabled = True
                self.ip_text.disabled = True

                self.make_invisible(self.connection_grid)
                self.make_invisible(self.connect_btn)

                thread = threading.Thread(target=self.receive)
                thread.start()

    def make_invisible(self, widget):
        widget.visible = False
        widget.size_hint_x = None
        widget.size_hint_y = None
        widget.height = 0
        widget.width = 0
        widget.text = ""
        widget.opacity = 0

    def receive(self):
        stop = False
        while not stop:
            try:
                message = client.recv(1024).decode('utf-8')
                print(message)
                self.ids.chat_text.text += message + "\n"  # self.chat_text.text +


            except:
                pass
                # print("Error")
                # client.close()
                # stop = True


class cdesign(App):

    def build(self):
        return MyRoot()


DemoChatApp = cdesign()
DemoChatApp.run()
