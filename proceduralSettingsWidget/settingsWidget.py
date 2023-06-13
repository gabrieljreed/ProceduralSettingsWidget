"""Widget to display and edit procedural settings."""

from PySide2 import QtWidgets, QtCore, QtGui


class SettingsWidget(QtWidgets.QWidget):
    """Widget to display and edit procedural settings."""

    def __init__(self, inObject, variables: list = None, parent=None):
        """Initialize the widget."""
        super().__init__(parent=parent)

        self.inObject = inObject
        self.variables = variables
        if self.variables is None:
            self.variables = vars(self.inObject).keys()

    def setupVariables(self):
        """Setup the variables."""
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        for variable in self.variables:
            self.addVariable(variable)
