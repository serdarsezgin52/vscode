import sys
from PyQt5.QtWidgets import QApplication, QWidget

# Create the main Qt app, passing command line arguments
app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle('Hello')
win.resize(250, 250)
win.show()

# Run the app, passing it's exit code back through `sys.exit()`
# The app will exit when the close button is pressed on the main window.
sys.exit(app.exec_())
