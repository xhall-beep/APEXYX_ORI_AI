[app]
title = ApexyxShell
package.name = apexyx.shell
package.domain = org.svontz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.api = 35
android.minapi = 21
android.ndk = 27b
# android.ndk_path =
android.ant_flags = -Wl,-z,max-page-size=16384
p4a.branch = master
[buildozer]
log_level = 2
warn_on_root = 1
