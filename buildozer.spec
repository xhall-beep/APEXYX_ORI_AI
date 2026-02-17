[app]
title = Apexyx ORI AI
package.name = apexyx_ori
package.domain = org.svontz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.api = 33
android.minapi = 21
android.ndk = 27b
android.ndk_path = 
android.sdk_path = 
# PHYSICAL 16KB ALIGNMENT LOCK
android.ant_flags = -Wl,-z,max-page-size=16384
p4a.branch = master
[buildozer]
log_level = 2
warn_on_root = 1
