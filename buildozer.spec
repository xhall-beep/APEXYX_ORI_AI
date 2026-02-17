[app]
title = Apexyx
package.name = apexyx
package.domain = org.apexyx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Added core dependencies for stability
requirements = python3,kivy==2.3.0,kivymd,pillow
orientation = portrait
android.archs = arm64-v8a
android.api = 33
android.ndk = 25c
android.ndk_path = ${{ github.workspace }}/android-ndk-r25c
android.skip_update = False
android.accept_sdk_license = True
# RE-ASSERTING 16KB ALIGNMENT
android.ldflags = -Wl,-z,max-page-size=16384 -fuse-ld=lld
