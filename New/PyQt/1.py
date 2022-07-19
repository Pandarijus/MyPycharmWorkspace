from PyQt5 import QtWidgets
import gui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = gui.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

