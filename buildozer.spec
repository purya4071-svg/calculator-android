[app]

# (str) Title of your application
title = ماشین حساب

# (str) Package name
package.name = calculator

# (str) Package domain
package.domain = org.purya

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (str) Main Python file
entrypoint = calculator_android.py

# (str) Application version
version = 1.0

# (list) Python requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


[buildozer]

# (str) Log level
log_level = 2

# (str) Warning for root permissions
warn_on_root = 1
