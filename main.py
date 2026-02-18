import android
from android.runnable import run_on_ui_thread
from jnius import autoclass

@run_on_ui_thread
def create_webview():
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    activity = autoclass('org.kivy.android.PythonActivity').mActivity
    
    webview = WebView(activity)
    webview.getSettings().setJavaScriptEnabled(True)
    webview.setWebViewClient(WebViewClient())
    
    html = """
    <!DOCTYPE html>
    <html>
    <body>
        <script>
            window.location = 'http://10.0.0.203:58081/reech-core';
        </script>
    </body>
    </html>
    """
    
    webview.loadData(html, "text/html", "utf-8")
    activity.setContentView(webview)

create_webview()
