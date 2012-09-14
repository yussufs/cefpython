# This file contains full API of "cefpython.pyd" module, all functions are dummy.
# Use it as a quick reference.
# Use it for code completion in your IDE.
# This file does NOT need to be distribitued along with binaries.

"""
Detailed documentation with examples can be found on wiki pages:
http://code.google.com/p/cefpython/w/list
"""

def CreateBrowser(windowID, browserSettings, navigateURL, clientHandlers=None, javascriptBindings=None):
	return Browser()

def ExceptHook(type, value, traceObject):
	return None

def GetBrowserByWindowID(windowID):
	return Browser()

def GetRealPath(file=None, encodeURL=False):
	return ""

def Initialize(applicationSettings={}):
	return None

def IsKeyModifier(key, modifiers):
	return False

def MessageLoop():
	return None

def SingleMessageLoop():
	return None

def QuitMessageLoop():
	return None

def Shutdown():
	return None

# ApplicationSettings["log_severity"]
LOGSEVERITY_VERBOSE = 0
LOGSEVERITY_INFO = 0
LOGSEVERITY_WARNING = 0
LOGSEVERITY_ERROR = 0
LOGSEVERITY_ERROR_REPORT = 0
LOGSEVERITY_DISABLE = 0

# ApplicationSettings["graphics_implementation"]
ANGLE_IN_PROCESS = 0
ANGLE_IN_PROCESS_COMMAND_BUFFER = 0
DESKTOP_IN_PROCESS = 0
DESKTOP_IN_PROCESS_COMMAND_BUFFER = 0

# Values are dummy, these are NOT the defaults.
ApplicationSettings = {
	"multi_threaded_message_loop": False,
	"cache_path": "",
	"user_agent": "",
	"product_version": "",
	"locale": "",
	"extra_plugin_paths": [""],
	"log_file": "",
	"log_severity": LOGSEVERITY_VERBOSE,
	"graphics_implementation": ANGLE_IN_PROCESS,
	"local_storage_quota": 5*1024*1024,
	"session_storage_quota": 5*1024*1024,
	"javascript_flags": "",
	"auto_detect_proxy_settings_enabled": False,
	"pack_file_path": "",
	"locales_dir_path": "",
	"pack_loading_disabled": False,
	"unicode_to_bytes_encoding": "utf-8",
}

# Values are dummy, these are NOT the defaults.
BrowserSettings = {
	"animation_frame_rate": 0,
	"drag_drop_disabled": False,
	"load_drops_disabled": False,
	"history_disabled": False,
	"standard_font_family": "",
	"fixed_font_family": "",
	"serif_font_family": "",
	"sans_serif_font_family": "",
	"cursive_font_family": "",
	"fantasy_font_family": "",
	"default_font_size": 0,
	"default_fixed_font_size": 0,
	"minimum_font_size": 0,
	"minimum_logical_font_size": 0,
	"remote_fonts_disabled": False,
	"default_encoding": "iso-8859-1",
	"encoding_detector_enabled": False,
	"javascript_disabled": False,
	"javascript_open_windows_disallowed": False,
	"javascript_close_windows_disallowed": False,
	"javascript_access_clipboard_disallowed": False,
	"dom_paste_disabled": False,
	"caret_browsing_enabled": False,
	"java_disabled": False,
	"plugins_disabled": False,
	"universal_access_from_file_urls_allowed": False,
	"file_access_from_file_urls_allowed": False,
	"web_security_disabled": False,
	"xss_auditor_enabled": False,
	"image_load_disabled": False,
	"shrink_standalone_images_to_fit": False,
	"site_specific_quirks_disabled": False,
	"text_area_resize_disabled": False,
	"page_cache_disabled": False,
	"tab_to_links_disabled": False,
	"hyperlink_auditing_disabled": False,
	"user_style_sheet_enabled": False,
	"user_style_sheet_location": "",
	"author_and_user_styles_disabled": False,
	"local_storage_disabled": False,
	"databases_disabled": False,
	"application_cache_disabled": False,
	"webgl_disabled": False,
	"accelerated_compositing_enabled": False,
	"accelerated_layers_disabled": False,
	"accelerated_video_disabled": False,
	"accelerated_2d_canvas_disabled": False,
	"accelerated_painting_disabled": False,
	"accelerated_filters_disabled": False,
	"accelerated_plugins_disabled": False,
	"developer_tools_disabled": False,
	"fullscreen_enabled": False,
}

#
# DisplayHandler.
#

# statusType constants (OnStatusMessage).
STATUSTYPE_TEXT = 0
STATUSTYPE_MOUSEOVER_URL = 0
STATUSTYPE_KEYBOARD_FOCUS_URL = 0

def DisplayHandler_OnAddressChange(browser, frame, url): 
	return None

def DisplayHandler_OnConsoleMessage(browser, message, source, line): 
	return False

def DisplayHandler_OnContentsSizeChange(browser, frame, width, height): 
	return None

def DisplayHandler_OnNavStateChange(browser, canGoBack, canGoForward):
	return None

def DisplayHandler_OnStatusMessage(browser, text, statusType):
	return None

def DisplayHandler_OnTitleChange(browser, title):
	return None

def DisplayHandler_OnTooltip(browser, text_out=[""]):
	return False

#
# KeyboardHandler.
#

# eventType constants (OnKeyEvent).
KEYEVENT_RAWKEYDOWN = 0
KEYEVENT_KEYDOWN = 0
KEYEVENT_KEYUP = 0
KEYEVENT_CHAR = 0

# Constants for checking modifiers param (OnKeyEvent), for use with IsKeyModifier() function.
KEY_NONE = 0
KEY_SHIFT = 0
KEY_CTRL = 0
KEY_ALT = 0
KEY_META = 0
KEY_KEYPAD = 0

# keyCode constants (OnKeyEvent).
VK_0=0x30
VK_1=0x31
VK_2=0x32
VK_3=0x33
VK_4=0x34
VK_5=0x35
VK_6=0x36
VK_7=0x37
VK_8=0x38
VK_9=0x39
VK_A=0x041
VK_B=0x042
VK_C=0x043
VK_D=0x044
VK_E=0x045
VK_F=0x046
VK_G=0x047
VK_H=0x048
VK_I=0x049
VK_J=0x04A
VK_K=0x04B
VK_L=0x04C
VK_M=0x04D
VK_N=0x04E
VK_O=0x04F
VK_P=0x050
VK_Q=0x051
VK_R=0x052
VK_S=0x053
VK_T=0x054
VK_U=0x055
VK_V=0x056
VK_W=0x057
VK_X=0x058
VK_Y=0x059
VK_Z=0x05A
VK_F1=0x70
VK_F2=0x71
VK_F3=0x72
VK_F4=0x73
VK_F5=0x74
VK_F6=0x75
VK_F7=0x76
VK_F8=0x77
VK_F9=0x78
VK_F10=0x79
VK_F11=0x7A
VK_F12=0x7B
VK_F13=0x7C
VK_F14=0x7D
VK_F15=0x7E
VK_F16=0x7F
VK_F17=0x80
VK_F18=0x81
VK_F19=0x82
VK_F20=0x83
VK_F21=0x84
VK_F22=0x85
VK_F23=0x86
VK_F24=0x87
VK_LSHIFT=0xA0
VK_RSHIFT=0xA1
VK_LCONTROL=0xA2
VK_RCONTROL=0xA3
VK_LMENU=0xA4
VK_RMENU=0xA5
VK_BACK=0x08
VK_TAB=0x09
VK_SPACE=0x20
VK_PRIOR=0x21
VK_NEXT=0x22
VK_END=0x23
VK_HOME=0x24
VK_LEFT=0x25
VK_UP=0x26
VK_RIGHT=0x27
VK_DOWN=0x28
VK_SELECT=0x29
VK_PRINT=0x2A
VK_EXECUTE=0x2B
VK_SNAPSHOT=0x2C
VK_INSERT=0x2D
VK_DELETE=0x2E
VK_HELP=0x2F
VK_SHIFT=0x10
VK_CONTROL=0x11
VK_MENU=0x12
VK_PAUSE=0x13
VK_CAPITAL=0x14
VK_CLEAR=0x0C
VK_RETURN=0x0D
VK_ESCAPE=0x1B
VK_LWIN=0x5B
VK_RWIN=0x5C
VK_APPS=0x5D
VK_SLEEP=0x5F
VK_NUMPAD0=0x60
VK_NUMPAD1=0x61
VK_NUMPAD2=0x62
VK_NUMPAD3=0x63
VK_NUMPAD4=0x64
VK_NUMPAD5=0x65
VK_NUMPAD6=0x66
VK_NUMPAD7=0x67
VK_NUMPAD8=0x68
VK_NUMPAD9=0x69
VK_BROWSER_BACK=0xA6
VK_BROWSER_FORWARD=0xA7
VK_BROWSER_REFRESH=0xA8
VK_BROWSER_STOP=0xA9
VK_BROWSER_SEARCH=0xAA
VK_BROWSER_FAVORITES=0xAB
VK_BROWSER_HOME=0xAC
VK_VOLUME_MUTE=0xAD
VK_VOLUME_DOWN=0xAE
VK_VOLUME_UP=0xAF
VK_MEDIA_NEXT_TRACK=0xB0
VK_MEDIA_PREV_TRACK=0xB1
VK_MEDIA_STOP=0xB2
VK_MEDIA_PLAY_PAUSE=0xB3
VK_LAUNCH_MAIL=0xB4
VK_LAUNCH_MEDIA_SELECT=0xB5
VK_LAUNCH_APP1=0xB6
VK_LAUNCH_APP2=0xB7
VK_MULTIPLY=0x6A
VK_ADD=0x6B
VK_SEPARATOR=0x6C
VK_SUBTRACT=0x6D
VK_DECIMAL=0x6E
VK_DIVIDE=0x6F
VK_NUMLOCK=0x90
VK_SCROLL=0x91
VK_LBUTTON=0x01
VK_RBUTTON=0x02
VK_CANCEL=0x03
VK_MBUTTON=0x04
VK_XBUTTON1=0x05
VK_XBUTTON2=0x06
VK_KANA=0x15
VK_HANGEUL=0x15
VK_HANGUL=0x15
VK_JUNJA=0x17
VK_FINAL=0x18
VK_HANJA=0x19
VK_KANJI=0x19
VK_CONVERT=0x1C
VK_NONCONVERT=0x1D
VK_ACCEPT=0x1E
VK_MODECHANGE=0x1F
VK_PROCESSKEY=0xE5
VK_PACKET=0xE7
VK_ICO_HELP=0xE3
VK_ICO_00=0xE4
VK_ICO_CLEAR=0xE6

def KeyboardHandler_OnKeyEvent(browser, eventType, keyCode, modifiers, isSystemKey, isAfterJavascript):
	return False

#
# LoadHandler.
#

# errorCode constants (OnLoadError).
ERR_FAILED = 0
ERR_ABORTED = 0
ERR_INVALID_ARGUMENT = 0
ERR_INVALID_HANDLE = 0
ERR_FILE_NOT_FOUND = 0
ERR_TIMED_OUT = 0
ERR_FILE_TOO_BIG = 0
ERR_UNEXPECTED = 0
ERR_ACCESS_DENIED = 0
ERR_NOT_IMPLEMENTED = 0
ERR_CONNECTION_CLOSED = 0
ERR_CONNECTION_RESET = 0
ERR_CONNECTION_REFUSED = 0
ERR_CONNECTION_ABORTED = 0
ERR_CONNECTION_FAILED = 0
ERR_NAME_NOT_RESOLVED = 0
ERR_INTERNET_DISCONNECTED = 0
ERR_SSL_PROTOCOL_ERROR = 0
ERR_ADDRESS_INVALID = 0
ERR_ADDRESS_UNREACHABLE = 0
ERR_SSL_CLIENT_AUTH_CERT_NEEDED = 0
ERR_TUNNEL_CONNECTION_FAILED = 0
ERR_NO_SSL_VERSIONS_ENABLED = 0
ERR_SSL_VERSION_OR_CIPHER_MISMATCH = 0
ERR_SSL_RENEGOTIATION_REQUESTED = 0
ERR_CERT_COMMON_NAME_INVALID = 0
ERR_CERT_DATE_INVALID = 0
ERR_CERT_AUTHORITY_INVALID = 0
ERR_CERT_CONTAINS_ERRORS = 0
ERR_CERT_NO_REVOCATION_MECHANISM = 0
ERR_CERT_UNABLE_TO_CHECK_REVOCATION = 0
ERR_CERT_REVOKED = 0
ERR_CERT_INVALID = 0
ERR_CERT_END = 0
ERR_INVALID_URL = 0
ERR_DISALLOWED_URL_SCHEME = 0
ERR_UNKNOWN_URL_SCHEME = 0
ERR_TOO_MANY_REDIRECTS = 0
ERR_UNSAFE_REDIRECT = 0
ERR_UNSAFE_PORT = 0
ERR_INVALID_RESPONSE = 0
ERR_INVALID_CHUNKED_ENCODING = 0
ERR_METHOD_NOT_SUPPORTED = 0
ERR_UNEXPECTED_PROXY_AUTH = 0
ERR_EMPTY_RESPONSE = 0
ERR_RESPONSE_HEADERS_TOO_BIG = 0
ERR_CACHE_MISS = 0
ERR_INSECURE_RESPONSE = 0

def OnLoadEnd(browser, frame, httpStatusCode): 
	return None

def OnLoadError(browser, frame, errorCode, failedURL, errorText_out=[""]): 
	return False

def OnLoadStart(browser, frame): 
	return None

#
# RequestHandler.
#

# navType constants (OnBeforeBrowse).
NAVTYPE_LINKCLICKED = 0
NAVTYPE_FORMSUBMITTED = 0
NAVTYPE_BACKFORWARD = 0
NAVTYPE_RELOAD = 0
NAVTYPE_FORMRESUBMITTED = 0
NAVTYPE_OTHER = 0
NAVTYPE_LINKDROPPED = 0

"""
def RequestHandler_OnBeforeBrowse(browser, frame, request, navType, isRedirect): 
	return False

def RequestHandler_OnBeforeResourceLoad(browser, request, redirectURL_out, resourceStream, response, loadFlags): 
	return False
"""

def RequestHandler_OnResourceRedirect(browser, oldURL, newURL_out=[""]): 
	return None

"""
def RequestHandler_OnResourceResponse(browser, url, response, filter_out=[None]): 
	return None
"""

def RequestHandler_OnProtocolExecution(browser, url, allowOSExecution_out=[False]): 
	return False

"""
def RequestHandler_GetDownloadHandler(browser, mimeType, filename, contentLength, downloadHandler_out=[None]): 
	return False
"""

def RequestHandler_GetAuthCredentials(browser, isProxy, host, port, realm, scheme, username_out=[""], password_out=[""]): 
	return False

"""
def RequestHandler_GetCookieManager(browser, mainURL):
	return cookieManager
"""

#
# JavascriptBindings class.
#

class JavascriptBindings:
	
	def __init__(self, bindToFrames=False, bindToPopups=False):
		return None

	def IsValueAllowed(self, value):
		return False

	def Rebind(self):
		return None
	
	def SetFunction(self, name, func):
		return None

	def SetObject(self, name, obj):
		return None

	def SetProperty(self, name, value):
		return None

#
# JavascriptCallback object.
#

class JavascriptCallback:

	def Call(self, param1, param2, param3_etc):
		return mixed

	def GetName(self):
		return name

#
# Browser object.
#

class Browser:

	def CanGoBack(self):
		return False

	def CanGoForward(self):
		return False

	def ClearHistory(self):
		return None

	def CloseBrowser(self):
		return None

	def CloseDevTools(self):
		return None

	def Find(self, searchID, searchText, forward, matchCase, findNext):
		return None

	def GetClientHandler(self, name):
		return clientHandlers[name]

	def GetClientHandlers(self):
		return clientHandlers

	def GetFocusedFrame(self):
		return Frame()

	def GetFrame(self):
		return Frame()

	def GetFrameNames(self):
		return ["", ""]

	def GetJavascriptBindings(self):
		return JavascriptBindings()

	def GetMainFrame(self):
		return Frame()

	def GetOpenerWindowID(self):
		return windowID
	
	def GetWindowID(self):
		return windowID

	def GetInnerWindowID(self):
		return windowID

	def GetZoomLevel(self):
		return 0.0

	def GoBack(self):
		return None

	def GoForward(self):
		return None

	def HasDocument(self):
		return False

	def HidePopup(self):
		return None

	def IsPopup(self):
		return False

	def IsPopupVisible(self):
		return False

	def IsWindowRenderingDisabled(self):
		return False

	def Reload(self):
		return None

	def ReloadIgnoreCache(self):
		return None

	"""
	def SendKeyEvent(self, keyType, keyInfo, modifiers):
		return None

	def SendMouseClickEvent(self, x, y, buttonType, mouseUp, clickCount):
		return None

	def SendMouseMoveEvent(self, x, y, mouseLeave):
		return None

	def SendMouseWheelEvent(self, x, y, deltaX, deltaY):
		return None

	def SendFocusEvent(self, setFocus):
		return None

	def SendCaptureLostEvent(self):
		return None
	"""

	def SetFocus(self, enable):
		return None

	def SetZoomLevel(self, zoomLevel):
		return None

	def ShowDevTools(self):
		return None

	def StopLoad(self):
		return None

	def StopFinding(self, clearSelection):
		return None

#
# Frame object.
#

class Frame:

	"""
	def CallFunction(self, funcName, param1, param2, param3_etc):
		return None
	"""

	def Copy(self):
		return None

	def Cut(self):
		return None

	def Delete(self):
		return None

	def ExecuteJavascript(self, jsCode, scriptURL=None, startLine=None):
		return None

	"""
	def EvalJavascript(self, code, retval, exception):
		return None

	def GetBrowser(self):
		return Browser()
	"""

	def GetIdentifier(self):
		return 0

	def GetName(self):
		return ""

	"""
	def GetParent(self):
		return Frame()
	"""

	def GetProperty(self, name):
		return mixed

	def GetSource(self):
		return ""

	def GetText(self):
		return ""

	def GetURL(self):
		return ""

	def IsFocused(self):
		return False

	def IsMain(self):
		return False

	"""
	def LoadRequest(self, request):
		return None

	def LoadStream(self, stream, url):
		return None
	"""

	def LoadString(self, value, url):
		return None

	def LoadURL(self, url):
		return None

	def Paste(self):
		return None

	def Print(self):
		return None

	def Redo(self):
		return None

	def SelectAll(self):
		return None

	def SetProperty(self, name, value):
		return None

	def Undo(self):
		return None

	def ViewSource(self):
		return None

	"""
	def VisitDOM(visitor):
		return None
	"""

