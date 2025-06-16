[app]

# Название приложения
title = FinanceApp

# Имя пакета (должно быть уникальным)
package.name = financeapp

# Домен приложения
package.domain = org.example

# Исходный код
source.dir = .

# Версия приложения (формат: 0.0.1)
version = 0.1

# Требуемые зависимости
requirements =
    python3,
    kivy==2.3.0,
    cython==0.29.19

# Ориентация экрана
orientation = portrait

# Полноэкранный режим (0 - выключен)
fullscreen = 0

# Разрешения Android
android.permissions = INTERNET

[android]

# Архитектуры (заменяет устаревший android.arch)
archs = armeabi-v7a, arm64-v8a

# Путь к Android NDK
ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r23b

# Путь к Android SDK
sdk_path = /usr/lib/android-sdk

# Минимальная версия Android API
minapi = 21

# Целевая версия Android API
targetapi = 33

# Версия python-for-android
p4a.branch = develop

# Разрешить доступ к хранилищу
android.allow_backup = True

# Разрешить отладку
android.debuggable = True

[buildozer]

# Уровень логгирования (0-2)
log_level = 2

# Копировать файлы с этими расширениями
source.include_exts = py,png,jpg,kv,atlas,ttf

# Дополнительные настройки сборки
android.accept_sdk_license = True
android.release_artifact = bin/{package.name}-{version}-release-unsigned.apk
android.debug_artifact = bin/{package.name}-{version}-debug.apk