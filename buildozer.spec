[app]
title = REECH Shell
package.name = reechshell
package.domain = org.reech
source.dir = .
source.include_exts = py
version = 0.1.0
requirements = python3
android.bootstrap = webview
android.api = 34
android.minapi = 24
android.ndk = 25b
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# CRITICAL: Explicitly exclude Kivy components
p4a.bootstrap = webview
p4a.ignore_setup_py = True
p4a.bootstrap_dir = .buildozer/android/platform/bootstrap_builds/webview-python3
