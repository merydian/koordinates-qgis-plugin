from enum import (
    Enum,
    auto
)


class TabStyle(Enum):
    Flat = auto()
    Rounded = auto()


class FilterWidgetAppearance(Enum):
    Horizontal = auto()
    Vertical = auto()


class ExploreMode:
    Popular = auto()
    Browse = auto()
    Publishers = auto()
    Recent = auto()