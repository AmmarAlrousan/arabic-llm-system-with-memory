from PyQt5 import QtWidgets, QtCore
import sys
from core.asm import ASM


class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.asm = ASM()

        self.setWindowTitle("ASM – Arab Synthetic Mind (Prototype)")
        self.resize(700, 600)

        layout = QtWidgets.QVBoxLayout(self)

        self.chat = QtWidgets.QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setLayoutDirection(QtCore.Qt.RightToLeft)
        layout.addWidget(self.chat)

        self.input = QtWidgets.QLineEdit()
        self.input.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.input.returnPressed.connect(self.send)
        layout.addWidget(self.input)

        send_btn = QtWidgets.QPushButton("إرسال")
        send_btn.clicked.connect(self.send)
        layout.addWidget(send_btn)

        self.append("ASM", "أهلاً، أنا ASM. كيف أستطيع مساعدتك؟")

    def append(self, sender, text):
        self.chat.append(f"<b>{sender}:</b><br>{text}<br><hr>")

    def send(self):
        msg = self.input.text().strip()
        if not msg:
            return

        self.append("أنت", msg)
        self.input.clear()

        reply = self.asm.respond(msg)
        self.append("ASM", reply)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = ChatWindow()
    win.show()
    sys.exit(app.exec_())
