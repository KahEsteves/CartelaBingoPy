import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from random import sample

class CartelaBingo(QWidget):
    def __init__(self):
        super().__init__()

        self.numeros_cartela = list(range(1, 76))  # Números da cartela
        self.init_ui()

    def init_ui(self):
        # Layout da cartela
        layout = QGridLayout()

        # Rótulo para exibir o último número sorteado
        self.label_ultimo_sorteado = QLabel("Último número sorteado: N/A")
        self.label_ultimo_sorteado.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_ultimo_sorteado, 0, 0, 1, 15)

        # Rótulo para exibir a lista dos números sorteados
        self.label_numeros_sorteados = QLabel("Números sorteados: ")
        layout.addWidget(self.label_numeros_sorteados, 1, 0, 1, 15)

        # Rótulo para o título "Bingo"
        label_titulo = QLabel("Gerador de números - Bingo")
        label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_titulo.setStyleSheet("font-size: 24px; color: #2B2A4C; margin-bottom: 20px;")
        layout.addWidget(label_titulo, 2, 0, 1, 15)

        # Botões para representar os números da cartela
        for i in range(5):
            for j in range(15):
                numero = self.numeros_cartela[i * 15 + j]
                btn_numero = QPushButton(str(numero))
                btn_numero.setFixedSize(40, 40)
                layout.addWidget(btn_numero, i + 3, j)
                btn_numero.setStyleSheet(
                    """
                    background-color: #F79327;
                    color: #EEE2DE;
                    border-radius: 4px;
                    """
                )

        # Botão para sortear um número
        self.btn_sortear = QPushButton("Sortear Número")
        self.btn_sortear.clicked.connect(self.sortear_numero)
        layout.addWidget(self.btn_sortear, 8, 0, 1, 7)
        self.btn_sortear.setStyleSheet(
            """
            font-size:15px;
            background-color: #2B2A4C;
            color: #EEE2DE;
            border-radius: 4px;
            """
        )

        # Botão para recomeçar o sorteio
        self.btn_recomecar = QPushButton("Recomeçar Sorteio")
        self.btn_recomecar.clicked.connect(self.recomecar_sorteio)
        layout.addWidget(self.btn_recomecar, 8, 8, 1, 7)
        self.btn_recomecar.setStyleSheet(
            """
            font-size:15px;
            background-color: #2B2A4C;
            color: #EEE2DE;
            border-radius: 4px;
            """
        )

        # Rótulo para exibir quando todos os números foram sorteados
        self.label_conclusao = QLabel("")
        layout.addWidget(self.label_conclusao, 9, 0, 1, 15)
        self.label_conclusao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Configuração do layout principal
        self.setLayout(layout)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Cartela de Bingo')

        self.numeros_sorteados = []  # Lista para armazenar os números sorteados

    def sortear_numero(self):
        if len(self.numeros_sorteados) < 75:
            numero_sorteado = sample(self.numeros_cartela, 1)[0]
            self.numeros_sorteados.append(numero_sorteado)
            self.numeros_cartela.remove(numero_sorteado)
            self.atualizar_interface(numero_sorteado)
            self.label_ultimo_sorteado.setText(f"Último número sorteado: {numero_sorteado}")
            if len(self.numeros_sorteados) % 20 == 0:
                self.label_numeros_sorteados.setText(f"{self.label_numeros_sorteados.text()}\n")
            self.label_numeros_sorteados.setText(f"{self.label_numeros_sorteados.text()}{numero_sorteado}, ")
            if len(self.numeros_sorteados) == 75:
                self.label_conclusao.setText("Parabéns! Todos os números foram sorteados!")

    def atualizar_interface(self, numero):
        # Encontrar o botão com o número sorteado e alterar sua aparência
        for i in range(5):
            for j in range(15):
                btn_numero = self.layout().itemAtPosition(i + 3, j).widget()
                if btn_numero.text() == str(numero):
                    btn_numero.setStyleSheet(
                        """
                        background-color: #B31312;
                        color: #EEE2DE;
                        border-radius: 4px;
                        """
                    )
                    btn_numero.setEnabled(False)
                    break

    def recomecar_sorteio(self):
        # Reiniciar a cartela e a lista de números sorteados
        self.numeros_cartela = list(range(1, 76))
        self.numeros_sorteados = []
        self.label_conclusao.clear()
        self.label_ultimo_sorteado.setText("Último número sorteado: N/A")
        self.label_numeros_sorteados.setText("Números sorteados: ")

        # Atualizar a aparência dos botões para o estado inicial
        for i in range(5):
            for j in range(15):
                btn_numero = self.layout().itemAtPosition(i + 3, j).widget()
                btn_numero.setStyleSheet(
                    """
                    background-color: #F79327;
                    color: #EEE2DE;
                    border-radius: 4px;
                    """
                )
                btn_numero.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    cartela = CartelaBingo()
    cartela.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
