# The PEP 484 type hints stub file for the QtNfc module.
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

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]


class QNdefFilter(PyQt5.sipsimplewrapper):

    class Record(PyQt5.sipsimplewrapper):

        maximum = ... # type: int
        minimum = ... # type: int
        type = ... # type: typing.Union[QtCore.QByteArray, bytes, bytearray]
        typeNameFormat = ... # type: 'QNdefRecord.TypeNameFormat'

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QNdefFilter.Record') -> None: ...

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QNdefFilter') -> None: ...

    def recordAt(self, i: int) -> 'QNdefFilter.Record': ...
    def __len__(self) -> int: ...
    def recordCount(self) -> int: ...
    @typing.overload
    def appendRecord(self, typeNameFormat: 'QNdefRecord.TypeNameFormat', type: typing.Union[QtCore.QByteArray, bytes, bytearray], min: int = ..., max: int = ...) -> None: ...
    @typing.overload
    def appendRecord(self, record: 'QNdefFilter.Record') -> None: ...
    def orderMatch(self) -> bool: ...
    def setOrderMatch(self, on: bool) -> None: ...
    def clear(self) -> None: ...


class QNdefMessage(PyQt5.sipsimplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, record: 'QNdefRecord') -> None: ...
    @typing.overload
    def __init__(self, message: 'QNdefMessage') -> None: ...
    @typing.overload
    def __init__(self, records: typing.Iterable['QNdefRecord']) -> None: ...

    def __ne__(self, other: object): ...
    @staticmethod
    def fromByteArray(message: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> 'QNdefMessage': ...
    def __delitem__(self, i: int) -> None: ...
    def __setitem__(self, i: int, value: 'QNdefRecord') -> None: ...
    def __getitem__(self, i: int) -> 'QNdefRecord': ...
    def __len__(self) -> int: ...
    def toByteArray(self) -> QtCore.QByteArray: ...
    def __eq__(self, other: object): ...


class QNdefRecord(PyQt5.sipsimplewrapper):

    class TypeNameFormat(int):
        Empty = ... # type: QNdefRecord.TypeNameFormat
        NfcRtd = ... # type: QNdefRecord.TypeNameFormat
        Mime = ... # type: QNdefRecord.TypeNameFormat
        Uri = ... # type: QNdefRecord.TypeNameFormat
        ExternalRtd = ... # type: QNdefRecord.TypeNameFormat
        Unknown = ... # type: QNdefRecord.TypeNameFormat

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QNdefRecord') -> None: ...

    def __hash__(self) -> int: ...
    def __ne__(self, other: object): ...
    def __eq__(self, other: object): ...
    def isEmpty(self) -> bool: ...
    def payload(self) -> QtCore.QByteArray: ...
    def setPayload(self, payload: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def id(self) -> QtCore.QByteArray: ...
    def setId(self, id: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def type(self) -> QtCore.QByteArray: ...
    def setType(self, type: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def typeNameFormat(self) -> 'QNdefRecord.TypeNameFormat': ...
    def setTypeNameFormat(self, typeNameFormat: 'QNdefRecord.TypeNameFormat') -> None: ...


class QNdefNfcIconRecord(QNdefRecord):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QNdefNfcIconRecord') -> None: ...

    def data(self) -> QtCore.QByteArray: ...
    def setData(self, data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...


class QNdefNfcSmartPosterRecord(QNdefRecord):

    class Action(int):
        UnspecifiedAction = ... # type: QNdefNfcSmartPosterRecord.Action
        DoAction = ... # type: QNdefNfcSmartPosterRecord.Action
        SaveAction = ... # type: QNdefNfcSmartPosterRecord.Action
        EditAction = ... # type: QNdefNfcSmartPosterRecord.Action

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QNdefNfcSmartPosterRecord') -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...

    def setTypeInfo(self, type: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def typeInfo(self) -> QtCore.QByteArray: ...
    def setSize(self, size: int) -> None: ...
    def size(self) -> int: ...
    def setIcons(self, icons: typing.Iterable[QNdefNfcIconRecord]) -> None: ...
    @typing.overload
    def removeIcon(self, icon: QNdefNfcIconRecord) -> bool: ...
    @typing.overload
    def removeIcon(self, type: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> bool: ...
    @typing.overload
    def addIcon(self, icon: QNdefNfcIconRecord) -> None: ...
    @typing.overload
    def addIcon(self, type: typing.Union[QtCore.QByteArray, bytes, bytearray], data: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def iconRecords(self) -> typing.List[QNdefNfcIconRecord]: ...
    def iconRecord(self, index: int) -> QNdefNfcIconRecord: ...
    def icon(self, mimetype: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> QtCore.QByteArray: ...
    def iconCount(self) -> int: ...
    def setAction(self, act: 'QNdefNfcSmartPosterRecord.Action') -> None: ...
    def action(self) -> 'QNdefNfcSmartPosterRecord.Action': ...
    @typing.overload
    def setUri(self, url: 'QNdefNfcUriRecord') -> None: ...
    @typing.overload
    def setUri(self, url: QtCore.QUrl) -> None: ...
    def uriRecord(self) -> 'QNdefNfcUriRecord': ...
    def uri(self) -> QtCore.QUrl: ...
    def setTitles(self, titles: typing.Iterable['QNdefNfcTextRecord']) -> None: ...
    @typing.overload
    def removeTitle(self, text: 'QNdefNfcTextRecord') -> bool: ...
    @typing.overload
    def removeTitle(self, locale: typing.Optional[str]) -> bool: ...
    @typing.overload
    def addTitle(self, text: 'QNdefNfcTextRecord') -> bool: ...
    @typing.overload
    def addTitle(self, text: typing.Optional[str], locale: typing.Optional[str], encoding: 'QNdefNfcTextRecord.Encoding') -> bool: ...
    def titleRecords(self) -> typing.List['QNdefNfcTextRecord']: ...
    def titleRecord(self, index: int) -> 'QNdefNfcTextRecord': ...
    def title(self, locale: typing.Optional[str] = ...) -> str: ...
    def titleCount(self) -> int: ...
    def hasTypeInfo(self) -> bool: ...
    def hasSize(self) -> bool: ...
    def hasIcon(self, mimetype: typing.Union[QtCore.QByteArray, bytes, bytearray] = ...) -> bool: ...
    def hasAction(self) -> bool: ...
    def hasTitle(self, locale: typing.Optional[str] = ...) -> bool: ...
    def setPayload(self, payload: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...


class QNdefNfcTextRecord(QNdefRecord):

    class Encoding(int):
        Utf8 = ... # type: QNdefNfcTextRecord.Encoding
        Utf16 = ... # type: QNdefNfcTextRecord.Encoding

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QNdefNfcTextRecord') -> None: ...

    def setEncoding(self, encoding: 'QNdefNfcTextRecord.Encoding') -> None: ...
    def encoding(self) -> 'QNdefNfcTextRecord.Encoding': ...
    def setText(self, text: typing.Optional[str]) -> None: ...
    def text(self) -> str: ...
    def setLocale(self, locale: typing.Optional[str]) -> None: ...
    def locale(self) -> str: ...


class QNdefNfcUriRecord(QNdefRecord):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: QNdefRecord) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QNdefNfcUriRecord') -> None: ...

    def setUri(self, uri: QtCore.QUrl) -> None: ...
    def uri(self) -> QtCore.QUrl: ...


class QNearFieldManager(QtCore.QObject):

    class AdapterState(int):
        Offline = ... # type: QNearFieldManager.AdapterState
        TurningOn = ... # type: QNearFieldManager.AdapterState
        Online = ... # type: QNearFieldManager.AdapterState
        TurningOff = ... # type: QNearFieldManager.AdapterState

    class TargetAccessMode(int):
        NoTargetAccess = ... # type: QNearFieldManager.TargetAccessMode
        NdefReadTargetAccess = ... # type: QNearFieldManager.TargetAccessMode
        NdefWriteTargetAccess = ... # type: QNearFieldManager.TargetAccessMode
        TagTypeSpecificTargetAccess = ... # type: QNearFieldManager.TargetAccessMode

    class TargetAccessModes(PyQt5.sipsimplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __ne__(self, other: object): ...
        def __eq__(self, other: object): ...
        def __ixor__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __xor__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __ior__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __or__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __iand__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __and__(self, f: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> 'QNearFieldManager.TargetAccessModes': ...
        def __invert__(self) -> 'QNearFieldManager.TargetAccessModes': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    adapterStateChanged: typing.ClassVar[QtCore.pyqtSignal]
    def isSupported(self) -> bool: ...
    targetLost: typing.ClassVar[QtCore.pyqtSignal]
    targetDetected: typing.ClassVar[QtCore.pyqtSignal]
    def unregisterNdefMessageHandler(self, handlerId: int) -> bool: ...
    @typing.overload
    def registerNdefMessageHandler(self, slot: PYQT_SLOT) -> int: ...
    @typing.overload
    def registerNdefMessageHandler(self, typeNameFormat: QNdefRecord.TypeNameFormat, type: typing.Union[QtCore.QByteArray, bytes, bytearray], slot: PYQT_SLOT) -> int: ...
    @typing.overload
    def registerNdefMessageHandler(self, filter: QNdefFilter, slot: PYQT_SLOT) -> int: ...
    def stopTargetDetection(self) -> None: ...
    def startTargetDetection(self) -> bool: ...
    def targetAccessModes(self) -> 'QNearFieldManager.TargetAccessModes': ...
    def setTargetAccessModes(self, accessModes: typing.Union['QNearFieldManager.TargetAccessModes', 'QNearFieldManager.TargetAccessMode']) -> None: ...
    def isAvailable(self) -> bool: ...


class QNearFieldShareManager(QtCore.QObject):

    class ShareMode(int):
        NoShare = ... # type: QNearFieldShareManager.ShareMode
        NdefShare = ... # type: QNearFieldShareManager.ShareMode
        FileShare = ... # type: QNearFieldShareManager.ShareMode

    class ShareError(int):
        NoError = ... # type: QNearFieldShareManager.ShareError
        UnknownError = ... # type: QNearFieldShareManager.ShareError
        InvalidShareContentError = ... # type: QNearFieldShareManager.ShareError
        ShareCanceledError = ... # type: QNearFieldShareManager.ShareError
        ShareInterruptedError = ... # type: QNearFieldShareManager.ShareError
        ShareRejectedError = ... # type: QNearFieldShareManager.ShareError
        UnsupportedShareModeError = ... # type: QNearFieldShareManager.ShareError
        ShareAlreadyInProgressError = ... # type: QNearFieldShareManager.ShareError
        SharePermissionDeniedError = ... # type: QNearFieldShareManager.ShareError

    class ShareModes(PyQt5.sipsimplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __ne__(self, other: object): ...
        def __eq__(self, other: object): ...
        def __ixor__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __xor__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __ior__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __or__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __iand__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __and__(self, f: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> 'QNearFieldShareManager.ShareModes': ...
        def __invert__(self) -> 'QNearFieldShareManager.ShareModes': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    error: typing.ClassVar[QtCore.pyqtSignal]
    shareModesChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetDetected: typing.ClassVar[QtCore.pyqtSignal]
    def shareError(self) -> 'QNearFieldShareManager.ShareError': ...
    def shareModes(self) -> 'QNearFieldShareManager.ShareModes': ...
    def setShareModes(self, modes: typing.Union['QNearFieldShareManager.ShareModes', 'QNearFieldShareManager.ShareMode']) -> None: ...
    @staticmethod
    def supportedShareModes() -> 'QNearFieldShareManager.ShareModes': ...


class QNearFieldShareTarget(QtCore.QObject):

    shareFinished: typing.ClassVar[QtCore.pyqtSignal]
    error: typing.ClassVar[QtCore.pyqtSignal]
    def shareError(self) -> QNearFieldShareManager.ShareError: ...
    def isShareInProgress(self) -> bool: ...
    def cancel(self) -> None: ...
    @typing.overload
    def share(self, message: QNdefMessage) -> bool: ...
    @typing.overload
    def share(self, files: typing.Iterable[QtCore.QFileInfo]) -> bool: ...
    def shareModes(self) -> QNearFieldShareManager.ShareModes: ...


class QNearFieldTarget(QtCore.QObject):

    class Error(int):
        NoError = ... # type: QNearFieldTarget.Error
        UnknownError = ... # type: QNearFieldTarget.Error
        UnsupportedError = ... # type: QNearFieldTarget.Error
        TargetOutOfRangeError = ... # type: QNearFieldTarget.Error
        NoResponseError = ... # type: QNearFieldTarget.Error
        ChecksumMismatchError = ... # type: QNearFieldTarget.Error
        InvalidParametersError = ... # type: QNearFieldTarget.Error
        NdefReadError = ... # type: QNearFieldTarget.Error
        NdefWriteError = ... # type: QNearFieldTarget.Error
        CommandError = ... # type: QNearFieldTarget.Error

    class AccessMethod(int):
        UnknownAccess = ... # type: QNearFieldTarget.AccessMethod
        NdefAccess = ... # type: QNearFieldTarget.AccessMethod
        TagTypeSpecificAccess = ... # type: QNearFieldTarget.AccessMethod
        LlcpAccess = ... # type: QNearFieldTarget.AccessMethod

    class Type(int):
        ProprietaryTag = ... # type: QNearFieldTarget.Type
        NfcTagType1 = ... # type: QNearFieldTarget.Type
        NfcTagType2 = ... # type: QNearFieldTarget.Type
        NfcTagType3 = ... # type: QNearFieldTarget.Type
        NfcTagType4 = ... # type: QNearFieldTarget.Type
        MifareTag = ... # type: QNearFieldTarget.Type

    class AccessMethods(PyQt5.sipsimplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __ne__(self, other: object): ...
        def __eq__(self, other: object): ...
        def __ixor__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __xor__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __ior__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __or__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __iand__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __and__(self, f: typing.Union['QNearFieldTarget.AccessMethods', 'QNearFieldTarget.AccessMethod']) -> 'QNearFieldTarget.AccessMethods': ...
        def __invert__(self) -> 'QNearFieldTarget.AccessMethods': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

    class RequestId(PyQt5.sipsimplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, other: 'QNearFieldTarget.RequestId') -> None: ...

        def __ge__(self, other: 'QNearFieldTarget.RequestId') -> bool: ...
        def __ne__(self, other: object): ...
        def __eq__(self, other: object): ...
        def __lt__(self, other: 'QNearFieldTarget.RequestId') -> bool: ...
        def refCount(self) -> int: ...
        def isValid(self) -> bool: ...

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def maxCommandLength(self) -> int: ...
    def disconnect(self) -> bool: ...
    def setKeepConnection(self, isPersistent: bool) -> bool: ...
    def keepConnection(self) -> bool: ...
    error: typing.ClassVar[QtCore.pyqtSignal]
    requestCompleted: typing.ClassVar[QtCore.pyqtSignal]
    ndefMessagesWritten: typing.ClassVar[QtCore.pyqtSignal]
    ndefMessageRead: typing.ClassVar[QtCore.pyqtSignal]
    disconnected: typing.ClassVar[QtCore.pyqtSignal]
    def reportError(self, error: 'QNearFieldTarget.Error', id: 'QNearFieldTarget.RequestId') -> None: ...
    def handleResponse(self, id: 'QNearFieldTarget.RequestId', response: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> bool: ...
    def setResponseForRequest(self, id: 'QNearFieldTarget.RequestId', response: typing.Any, emitRequestCompleted: bool = ...) -> None: ...
    def requestResponse(self, id: 'QNearFieldTarget.RequestId') -> typing.Any: ...
    def waitForRequestCompleted(self, id: 'QNearFieldTarget.RequestId', msecs: int = ...) -> bool: ...
    def sendCommands(self, commands: typing.Iterable[typing.Union[QtCore.QByteArray, bytes, bytearray]]) -> 'QNearFieldTarget.RequestId': ...
    def sendCommand(self, command: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> 'QNearFieldTarget.RequestId': ...
    def writeNdefMessages(self, messages: typing.Iterable[QNdefMessage]) -> 'QNearFieldTarget.RequestId': ...
    def readNdefMessages(self) -> 'QNearFieldTarget.RequestId': ...
    def hasNdefMessage(self) -> bool: ...
    def isProcessingCommand(self) -> bool: ...
    def accessMethods(self) -> 'QNearFieldTarget.AccessMethods': ...
    def type(self) -> 'QNearFieldTarget.Type': ...
    def url(self) -> QtCore.QUrl: ...
    def uid(self) -> QtCore.QByteArray: ...


class QQmlNdefRecord(QtCore.QObject):

    class TypeNameFormat(int):
        Empty = ... # type: QQmlNdefRecord.TypeNameFormat
        NfcRtd = ... # type: QQmlNdefRecord.TypeNameFormat
        Mime = ... # type: QQmlNdefRecord.TypeNameFormat
        Uri = ... # type: QQmlNdefRecord.TypeNameFormat
        ExternalRtd = ... # type: QQmlNdefRecord.TypeNameFormat
        Unknown = ... # type: QQmlNdefRecord.TypeNameFormat

    @typing.overload
    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...
    @typing.overload
    def __init__(self, record: QNdefRecord, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    recordChanged: typing.ClassVar[QtCore.pyqtSignal]
    typeNameFormatChanged: typing.ClassVar[QtCore.pyqtSignal]
    typeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setRecord(self, record: QNdefRecord) -> None: ...
    def record(self) -> QNdefRecord: ...
    def typeNameFormat(self) -> 'QQmlNdefRecord.TypeNameFormat': ...
    def setTypeNameFormat(self, typeNameFormat: 'QQmlNdefRecord.TypeNameFormat') -> None: ...
    def setType(self, t: typing.Optional[str]) -> None: ...
    def type(self) -> str: ...
