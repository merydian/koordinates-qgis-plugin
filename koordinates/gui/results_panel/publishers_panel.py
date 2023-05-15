import os
from typing import (
    Optional
)

from qgis.PyQt.QtWidgets import (
    QVBoxLayout,
    QWidget
)

from .results_panel_widget import ResultsPanelWidget
from ..publisher_filter_widget import PublisherSelectionWidget

pluginPath = os.path.split(os.path.dirname(__file__))[0]


class PublishersPanelWidget(ResultsPanelWidget):
    """
    Results panel widget for "publishers" panel
    """

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        vl = QVBoxLayout()
        vl.setContentsMargins(0, 0, 0, 0)

        self.publisher_widget = PublisherSelectionWidget(
            highlight_search_box=True
        )
        self.publisher_widget.layout().setContentsMargins(0, 0, 0, 0)
        vl.addWidget(self.publisher_widget)

        self.setLayout(vl)
