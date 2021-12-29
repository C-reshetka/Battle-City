import sys

from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from map_states import H, P, u, a, E, w, m, R, S, A, h, s

import maps
from menu import Menu


class Designer(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 600)
        self.setWindowTitle('Designer')
        self.layout = QGridLayout(self)
        self.layout.setVerticalSpacing(1)
        self.layout.setHorizontalSpacing(1)
        self.setLayout(self.layout)
        img = QPixmap('images\empty.png')
        img = img.scaledToWidth(25)
        img = img.scaledToHeight(25)
        for i in range(20):
            for j in range(20):
                if i == 0 or j == 0 or i == 19 or j == 19:
                    continue
                label = DropLabel(self, pos=(i, j))
                label.setPixmap(img)
                self.layout.addWidget(label, i, j)

        label = self.create_drag_picture('pl_up')
        self.layout.addWidget(label, 21, 0)
        label = self.create_drag_picture('headquartes')
        self.layout.addWidget(label, 21, 1)
        label = self.create_drag_picture('uncrashed_wall')
        self.layout.addWidget(label, 21, 2)
        label = self.create_drag_picture('wall')
        self.layout.addWidget(label, 21, 3)
        label = self.create_drag_picture('water')
        self.layout.addWidget(label, 21, 4)
        label = self.create_drag_picture('mirror_wall')
        self.layout.addWidget(label, 21, 5)
        label = self.create_drag_picture('enemy_up')
        self.layout.addWidget(label, 21, 6)
        label = self.create_drag_picture('re_up')
        self.layout.addWidget(label, 21, 7)
        label = self.create_drag_picture('ae_up')
        self.layout.addWidget(label, 21, 8)
        label = self.create_drag_picture('ss_up')
        self.layout.addWidget(label, 21, 9)
        label = self.create_drag_picture('heart')
        self.layout.addWidget(label, 21, 10)
        label = self.create_drag_picture('shield')
        self.layout.addWidget(label, 21, 11)
        self.create_btn = QPushButton('Create!', self)
        self.layout.addWidget(self.create_btn, 20, 13, 20, 13)
        self.create_btn.clicked.connect(self.save_level)

    def create_drag_picture(self, name):
        img = QPixmap('images\\' + name + '.png')
        img = img.scaledToWidth(25)
        img = img.scaledToHeight(25)
        label = DragLabel(self, name)
        label.resize(25, 25)
        label.setPixmap(img)
        return label

    def save_level(self):
        for i in range(20):
            for j in range(20):
                if i == 0 or j == 0 or i == 19 or j == 19:
                    continue
                now = self.layout.itemAtPosition(i, j).widget()
                now: DropLabel
                img = now.i_name
                if img == 'empty':
                    maps.map_c[i][j] = 0
                elif img == 'pl_up':
                    maps.map_c[i][j] = P
                elif img == 'headquartes':
                    maps.map_c[i][j] = H
                elif img == 'uncrashed_wall':
                    maps.map_c[i][j] = u
                elif img == 'wall':
                    maps.map_c[i][j] = a
                elif img == 'mirror_wall':
                    maps.map_c[i][j] = m
                elif img == 'enemy_up':
                    maps.map_c[i][j] = E
                elif img == 're_up':
                    maps.map_c[i][j] = R
                elif img == 'ae_up':
                    maps.map_c[i][j] = A
                elif img == 'ss_up':
                    maps.map_c[i][j] = S
                elif img == 'heart':
                    maps.map_c[i][j] = h
                elif img == 'shield':
                    maps.map_c[i][j] = s
        self.close()
        Menu()


class DragLabel(QLabel):
    def __init__(self, parent, name='empty'):
        super().__init__(parent)
        self.i_name = name

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        else:
            drag = QDrag(self)

            mimedata = QMimeData()
            mimedata.setText(self.i_name)
            mimedata.setImageData(self.pixmap())

            drag.setMimeData(mimedata)

            # creating the dragging effect
            pixmap = QPixmap(self.size())  # label size

            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()

            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)


class DropLabel(QLabel):
    def __init__(self, parent, pos, name='empty'):
        super().__init__(parent)
        self.i_name = name
        self.pos = pos
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        image = event.mimeData().imageData()
        self.setPixmap(image)
        self.i_name = event.mimeData().text()
        event.acceptProposedAction()


app = QApplication(sys.argv)
view = Designer()
view.show()
sys.exit(app.exec_())