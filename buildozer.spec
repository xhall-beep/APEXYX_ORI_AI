[app]
title = REECH Shell
package.name = reechshell
package.domain = org.reech
source.dir = .
source.include_exts = py
version = 0.1.3
requirements = python3
android.bootstrap = webview
android.api = 34
android.minapi = 24
android.ndk = 25b
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.archs = arm64-v8a
# This line is critical to bypass the C-compiler errors
p4a.local_recipes = 
