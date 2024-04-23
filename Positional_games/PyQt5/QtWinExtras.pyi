# The PEP 484 type hints stub file for the QtWinExtras module.
#
# Generated by SIP 6.7.12
#
# Copyright (c) 2023 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QtWin(PyQt5.sip.simplewrapper):

    class WindowFlip3DPolicy(int):
        FlipDefault = ... # type: QtWin.WindowFlip3DPolicy
        FlipExcludeBelow = ... # type: QtWin.WindowFlip3DPolicy
        FlipExcludeAbove = ... # type: QtWin.WindowFlip3DPolicy

    class HBitmapFormat(int):
        HBitmapNoAlpha = ... # type: QtWin.HBitmapFormat
        HBitmapPremultipliedAlpha = ... # type: QtWin.HBitmapFormat
        HBitmapAlpha = ... # type: QtWin.HBitmapFormat

    @typing.overload
    def taskbarDeleteTab(self, a0: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def taskbarDeleteTab(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def taskbarAddTab(self, a0: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def taskbarAddTab(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def taskbarActivateTabAlt(self, a0: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def taskbarActivateTabAlt(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def taskbarActivateTab(self, a0: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def taskbarActivateTab(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def markFullscreenWindow(self, a0: typing.Optional[QtGui.QWindow], fullscreen: bool = ...) -> None: ...
    @typing.overload
    def markFullscreenWindow(self, window: typing.Optional[QtWidgets.QWidget], fullscreen: bool = ...) -> None: ...
    def setCurrentProcessExplicitAppUserModelID(self, id: typing.Optional[str]) -> None: ...
    def isCompositionOpaque(self) -> bool: ...
    def setCompositionEnabled(self, enabled: bool) -> None: ...
    def isCompositionEnabled(self) -> bool: ...
    @typing.overload
    def disableBlurBehindWindow(self, window: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def disableBlurBehindWindow(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def enableBlurBehindWindow(self, window: typing.Optional[QtGui.QWindow], region: QtGui.QRegion) -> None: ...
    @typing.overload
    def enableBlurBehindWindow(self, window: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def enableBlurBehindWindow(self, window: typing.Optional[QtWidgets.QWidget], region: QtGui.QRegion) -> None: ...
    @typing.overload
    def enableBlurBehindWindow(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def resetExtendedFrame(self, window: typing.Optional[QtGui.QWindow]) -> None: ...
    @typing.overload
    def resetExtendedFrame(self, window: typing.Optional[QtWidgets.QWidget]) -> None: ...
    @typing.overload
    def extendFrameIntoClientArea(self, window: typing.Optional[QtGui.QWindow], left: int, top: int, right: int, bottom: int) -> None: ...
    @typing.overload
    def extendFrameIntoClientArea(self, window: typing.Optional[QtGui.QWindow], margins: QtCore.QMargins) -> None: ...
    @typing.overload
    def extendFrameIntoClientArea(self, window: typing.Optional[QtWidgets.QWidget], margins: QtCore.QMargins) -> None: ...
    @typing.overload
    def extendFrameIntoClientArea(self, window: typing.Optional[QtWidgets.QWidget], left: int, top: int, right: int, bottom: int) -> None: ...
    @typing.overload
    def windowFlip3DPolicy(self, a0: typing.Optional[QtGui.QWindow]) -> 'QtWin.WindowFlip3DPolicy': ...
    @typing.overload
    def windowFlip3DPolicy(self, window: typing.Optional[QtWidgets.QWidget]) -> 'QtWin.WindowFlip3DPolicy': ...
    @typing.overload
    def setWindowFlip3DPolicy(self, window: typing.Optional[QtGui.QWindow], policy: 'QtWin.WindowFlip3DPolicy') -> None: ...
    @typing.overload
    def setWindowFlip3DPolicy(self, window: typing.Optional[QtWidgets.QWidget], policy: 'QtWin.WindowFlip3DPolicy') -> None: ...
    @typing.overload
    def isWindowPeekDisallowed(self, window: typing.Optional[QtGui.QWindow]) -> bool: ...
    @typing.overload
    def isWindowPeekDisallowed(self, window: typing.Optional[QtWidgets.QWidget]) -> bool: ...
    @typing.overload
    def setWindowDisallowPeek(self, window: typing.Optional[QtGui.QWindow], disallow: bool) -> None: ...
    @typing.overload
    def setWindowDisallowPeek(self, window: typing.Optional[QtWidgets.QWidget], disallow: bool) -> None: ...
    @typing.overload
    def isWindowExcludedFromPeek(self, window: typing.Optional[QtGui.QWindow]) -> bool: ...
    @typing.overload
    def isWindowExcludedFromPeek(self, window: typing.Optional[QtWidgets.QWidget]) -> bool: ...
    @typing.overload
    def setWindowExcludedFromPeek(self, window: typing.Optional[QtGui.QWindow], exclude: bool) -> None: ...
    @typing.overload
    def setWindowExcludedFromPeek(self, window: typing.Optional[QtWidgets.QWidget], exclude: bool) -> None: ...
    def realColorizationColor(self) -> QtGui.QColor: ...
    def colorizationColor(self) -> typing.Tuple[QtGui.QColor, typing.Optional[bool]]: ...
    def errorStringFromHresult(self, hresult: int) -> str: ...
    def stringFromHresult(self, hresult: int) -> str: ...
    def fromHRGN(self, hrgn: typing.Optional[PyQt5.sip.voidptr]) -> QtGui.QRegion: ...
    def toHRGN(self, region: QtGui.QRegion) -> typing.Optional[PyQt5.sip.voidptr]: ...
    def fromHICON(self, icon: typing.Optional[PyQt5.sip.voidptr]) -> QtGui.QPixmap: ...
    def imageFromHBITMAP(self, hdc: typing.Optional[PyQt5.sip.voidptr], bitmap: typing.Optional[PyQt5.sip.voidptr], width: int, height: int) -> QtGui.QImage: ...
    def toHICON(self, p: QtGui.QPixmap) -> typing.Optional[PyQt5.sip.voidptr]: ...
    def fromHBITMAP(self, bitmap: typing.Optional[PyQt5.sip.voidptr], format: 'QtWin.HBitmapFormat' = ...) -> QtGui.QPixmap: ...
    def toHBITMAP(self, p: QtGui.QPixmap, format: 'QtWin.HBitmapFormat' = ...) -> typing.Optional[PyQt5.sip.voidptr]: ...
    def createMask(self, bitmap: QtGui.QBitmap) -> typing.Optional[PyQt5.sip.voidptr]: ...


class QWinJumpList(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def clear(self) -> None: ...
    @typing.overload
    def addCategory(self, category: typing.Optional['QWinJumpListCategory']) -> None: ...
    @typing.overload
    def addCategory(self, title: typing.Optional[str], items: typing.Iterable['QWinJumpListItem'] = ...) -> typing.Optional['QWinJumpListCategory']: ...
    def categories(self) -> typing.List['QWinJumpListCategory']: ...
    def tasks(self) -> typing.Optional['QWinJumpListCategory']: ...
    def frequent(self) -> typing.Optional['QWinJumpListCategory']: ...
    def recent(self) -> typing.Optional['QWinJumpListCategory']: ...
    def setIdentifier(self, identifier: typing.Optional[str]) -> None: ...
    def identifier(self) -> str: ...


class QWinJumpListCategory(PyQt5.sip.wrapper):

    class Type(int):
        Custom = ... # type: QWinJumpListCategory.Type
        Recent = ... # type: QWinJumpListCategory.Type
        Frequent = ... # type: QWinJumpListCategory.Type
        Tasks = ... # type: QWinJumpListCategory.Type

    def __init__(self, title: typing.Optional[str] = ...) -> None: ...

    def clear(self) -> None: ...
    def addSeparator(self) -> typing.Optional['QWinJumpListItem']: ...
    @typing.overload
    def addLink(self, title: typing.Optional[str], executablePath: typing.Optional[str], arguments: typing.Iterable[typing.Optional[str]] = ...) -> typing.Optional['QWinJumpListItem']: ...
    @typing.overload
    def addLink(self, icon: QtGui.QIcon, title: typing.Optional[str], executablePath: typing.Optional[str], arguments: typing.Iterable[typing.Optional[str]] = ...) -> typing.Optional['QWinJumpListItem']: ...
    def addDestination(self, filePath: typing.Optional[str]) -> typing.Optional['QWinJumpListItem']: ...
    def addItem(self, item: typing.Optional['QWinJumpListItem']) -> None: ...
    def items(self) -> typing.List['QWinJumpListItem']: ...
    def isEmpty(self) -> bool: ...
    def count(self) -> int: ...
    def setTitle(self, title: typing.Optional[str]) -> None: ...
    def title(self) -> str: ...
    def setVisible(self, visible: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def type(self) -> 'QWinJumpListCategory.Type': ...


class QWinJumpListItem(PyQt5.sip.wrapper):

    class Type(int):
        Destination = ... # type: QWinJumpListItem.Type
        Link = ... # type: QWinJumpListItem.Type
        Separator = ... # type: QWinJumpListItem.Type

    def __init__(self, type: 'QWinJumpListItem.Type') -> None: ...

    def arguments(self) -> typing.List[str]: ...
    def setArguments(self, arguments: typing.Iterable[typing.Optional[str]]) -> None: ...
    def description(self) -> str: ...
    def setDescription(self, description: typing.Optional[str]) -> None: ...
    def title(self) -> str: ...
    def setTitle(self, title: typing.Optional[str]) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def setIcon(self, icon: QtGui.QIcon) -> None: ...
    def workingDirectory(self) -> str: ...
    def setWorkingDirectory(self, workingDirectory: typing.Optional[str]) -> None: ...
    def filePath(self) -> str: ...
    def setFilePath(self, filePath: typing.Optional[str]) -> None: ...
    def type(self) -> 'QWinJumpListItem.Type': ...
    def setType(self, type: 'QWinJumpListItem.Type') -> None: ...


class QWinTaskbarButton(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def clearOverlayIcon(self) -> None: ...
    def setOverlayAccessibleDescription(self, description: typing.Optional[str]) -> None: ...
    def setOverlayIcon(self, icon: QtGui.QIcon) -> None: ...
    def eventFilter(self, a0: typing.Optional[QtCore.QObject], a1: typing.Optional[QtCore.QEvent]) -> bool: ...
    def progress(self) -> typing.Optional['QWinTaskbarProgress']: ...
    def overlayAccessibleDescription(self) -> str: ...
    def overlayIcon(self) -> QtGui.QIcon: ...
    def window(self) -> typing.Optional[QtGui.QWindow]: ...
    def setWindow(self, window: typing.Optional[QtGui.QWindow]) -> None: ...


class QWinTaskbarProgress(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    visibilityChanged: typing.ClassVar[QtCore.pyqtSignal]
    maximumChanged: typing.ClassVar[QtCore.pyqtSignal]
    minimumChanged: typing.ClassVar[QtCore.pyqtSignal]
    valueChanged: typing.ClassVar[QtCore.pyqtSignal]
    def stop(self) -> None: ...
    def setPaused(self, paused: bool) -> None: ...
    def resume(self) -> None: ...
    def pause(self) -> None: ...
    def setVisible(self, visible: bool) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def reset(self) -> None: ...
    def setRange(self, minimum: int, maximum: int) -> None: ...
    def setMaximum(self, maximum: int) -> None: ...
    def setMinimum(self, minimum: int) -> None: ...
    def setValue(self, value: int) -> None: ...
    def isStopped(self) -> bool: ...
    def isPaused(self) -> bool: ...
    def isVisible(self) -> bool: ...
    def maximum(self) -> int: ...
    def minimum(self) -> int: ...
    def value(self) -> int: ...


class QWinThumbnailToolBar(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    iconicLivePreviewPixmapRequested: typing.ClassVar[QtCore.pyqtSignal]
    iconicThumbnailPixmapRequested: typing.ClassVar[QtCore.pyqtSignal]
    def setIconicLivePreviewPixmap(self, a0: QtGui.QPixmap) -> None: ...
    def setIconicThumbnailPixmap(self, a0: QtGui.QPixmap) -> None: ...
    def clear(self) -> None: ...
    def iconicLivePreviewPixmap(self) -> QtGui.QPixmap: ...
    def iconicThumbnailPixmap(self) -> QtGui.QPixmap: ...
    def setIconicPixmapNotificationsEnabled(self, enabled: bool) -> None: ...
    def iconicPixmapNotificationsEnabled(self) -> bool: ...
    def count(self) -> int: ...
    def buttons(self) -> typing.List['QWinThumbnailToolButton']: ...
    def setButtons(self, buttons: typing.Iterable['QWinThumbnailToolButton']) -> None: ...
    def removeButton(self, button: typing.Optional['QWinThumbnailToolButton']) -> None: ...
    def addButton(self, button: typing.Optional['QWinThumbnailToolButton']) -> None: ...
    def window(self) -> typing.Optional[QtGui.QWindow]: ...
    def setWindow(self, window: typing.Optional[QtGui.QWindow]) -> None: ...


class QWinThumbnailToolButton(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    clicked: typing.ClassVar[QtCore.pyqtSignal]
    def click(self) -> None: ...
    def isFlat(self) -> bool: ...
    def setFlat(self, flat: bool) -> None: ...
    def dismissOnClick(self) -> bool: ...
    def setDismissOnClick(self, dismiss: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def setVisible(self, visible: bool) -> None: ...
    def isInteractive(self) -> bool: ...
    def setInteractive(self, interactive: bool) -> None: ...
    def isEnabled(self) -> bool: ...
    def setEnabled(self, enabled: bool) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def setIcon(self, icon: QtGui.QIcon) -> None: ...
    def toolTip(self) -> str: ...
    def setToolTip(self, toolTip: typing.Optional[str]) -> None: ...
