"""Widget to display and edit procedural settings."""

from PySide2 import QtWidgets, QtCore, QtGui

from . import settingsVariables
from . import inputWidgets


class SettingsWidget(QtWidgets.QWidget):
    """Widget to display and edit procedural settings."""

    def __init__(self, inObject, variables: list = None, parent=None):
        """Initialize the widget.

        Arguments:
            inObject {object} -- The object to display and edit.
            variables {list} -- The variables to display and edit. This can be a list of strings, or a list of tuples with the first element being the variable name and the second element being the label text. Defaults to None.
        """
        super().__init__(parent=parent)

        self.inObject = inObject
        self.variables = variables
        if self.variables is None:
            self.variables = vars(self.inObject).keys()

    def setupVariables(self):
        """Set up the variables."""
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        for variable in self.variables:
            self.addVariable(variable)

    def addVariable(self, variable):
        """Add a variable to the widget."""
        if isinstance(variable, str):
            self.addVariableStr(variable)
        elif isinstance(variable, settingsVariables.settingsVar):
            self.addVariableClass(variable)

    def addVariableStr(self, variable):
        pass

    def addVariableClass(self, variable):
        pass
