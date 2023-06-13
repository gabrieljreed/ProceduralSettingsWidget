"""Input widgets for procedural settings widget."""

from PySide2 import QtWidgets, QtCore, QtGui


class InputWidget(QtWidgets.QWidget):
    """Base class for input widgets."""

    def __init__(self, parent=None) -> None:
        """Initialize the widget."""
        super().__init__(parent)


class LargeInputWidget(InputWidget):
    """Large input widget."""

    def __init__(self, parent=None) -> None:
        """Initialize the widget."""
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.label)

        self.input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.input)

    def setLabel(self, text: str) -> None:
        """Set the label text."""
        self.label.setText(text)

    def setValue(self, value: str) -> None:
        """Set the value."""
        self.input.setText(value)

    def getValue(self) -> str:
        """Return the value."""
        return self.input.text()


class SmallInputWidget(InputWidget):
    """Small input widget."""

    def __init__(self, parent=None) -> None:
        """Initialize the widget."""
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel()
        self.layout.addWidget(self.label)

        self.input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.input)

    def setLabel(self, text: str) -> None:
        """Set the label text."""
        self.label.setText(text)

    def setValue(self, value: str) -> None:
        """Set the value."""
        self.input.setText(value)

    def getValue(self) -> str:
        """Return the value."""
        return self.input.text()
