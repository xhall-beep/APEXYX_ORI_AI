[app]
title = APEXYX_ORI
package.name = apexyxori
package.domain = org.svontz
source.dir = .
version = 1.0.0
requirements = python3,kivy
orientation = portrait
android.archs = arm64-v8a
# 16KB Alignment Fix
android.gradle_dependencies = "com.android.tools.build:gradle:8.2.2"
android.accept_sdk_license = True
android.api = 33
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 0
