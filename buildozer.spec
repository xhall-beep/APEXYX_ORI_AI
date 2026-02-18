[app]
title = Apexyx
package.name = apexyx
package.domain = org.apexyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,kivymd,pillow,hostpython3
orientation = portrait
android.archs = arm64-v8a
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.ldflags = -Wl,-z,max-page-size=16384 -fuse-ld=lld
android.ndk_api = 21
