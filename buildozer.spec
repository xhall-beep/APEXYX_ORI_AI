[app]
title = REECH Shell
package.name = reech_sovereign_v80
package.domain = org.svontz
source.dir = .
source.include_exts = py
version = 0.8.0
requirements = python3,hostpython3,kivy==2.3.0,kivymd,pillow,requests,urllib3,certifi,chaquopy,openssl
p4a.bootstrap = webview
android.api = 33
android.minapi = 24
android.ndk = 25c
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,FOREGROUND_SERVICE,QUERY_ALL_PACKAGES
android.archs = arm64-v8a
p4a.branch = master
