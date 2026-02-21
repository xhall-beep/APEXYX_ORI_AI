from android.runnable import run_on_ui_thread
from jnius import autoclass

# Sovereign Bridge: Pointing to your live Termux Server
TARGET_URL = "http://127.0.0.1:58080"

PythonActivity = autoclass('org.kivy.android.PythonActivity')
WebView = autoclass('android.webkit.WebView')
WebViewClient = autoclass('android.webkit.WebViewClient')

@run_on_ui_thread
def create_webview():
    activity = PythonActivity.mActivity
    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    webview.setWebViewClient(WebViewClient())
    activity.setContentView(webview)
    webview.loadUrl(TARGET_URL)

if __name__ == "__main__":
    create_webview()
