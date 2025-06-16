[app]
title = FinanceApp
package.name = financeapp
package.domain = org.example
source.dir = .
version = 0.1
requirements = python3,kivy==2.3.0,cython==0.29.36

[android]
archs = armeabi-v7a
ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
sdk_path = /usr/lib/android-sdk
p4a.branch = master
minapi = 21
targetapi = 33
permissions = INTERNET

[buildozer]
log_level = 2