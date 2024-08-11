import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget,
    QToolBar, QStatusBar, QFileDialog
)
from PySide6.QtGui import QAction, QFont
from PySide6.QtCore import Qt, QSize

class MinimalEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minimal for Preview Tawitch")
        self.setGeometry(100, 100, 800, 600)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Text editor
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("SF Pro Text", 14))
        layout.addWidget(self.text_edit)

        # Toolbar
        self.create_toolbar()

        # Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

        # Set style
        self.setStyleSheet("""
            QMainWindow, QTextEdit {
                background-color: #f0f0f0;
                color: #333;
            }
            QToolBar {
                background-color: #e0e0e0;
                border-bottom: 1px solid #ccc;
            }
            QStatusBar {
                background-color: #e0e0e0;
            }
        """)

    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(Qt.TopToolBarArea, toolbar)

        # New file action
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        # Open file action
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        # Save file action
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

    def new_file(self):
        self.text_edit.clear()
        self.statusBar.showMessage("New file created", 2000)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text_edit.setPlainText(file.read())
                self.statusBar.showMessage(f"Opened {file_path}", 2000)
            except Exception as e:
                self.statusBar.showMessage(f"Error opening file: {str(e)}", 2000)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text_edit.toPlainText())
                self.statusBar.showMessage(f"Saved to {file_path}", 2000)
            except Exception as e:
                self.statusBar.showMessage(f"Error saving file: {str(e)}", 2000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = MinimalEditor()
    editor.show()
    sys.exit(app.exec())