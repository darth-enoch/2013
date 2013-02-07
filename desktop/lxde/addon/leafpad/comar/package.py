#!/usr/bin/python

import os
 
def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
 
def postRemove(fromVersion, fromRelease, toVersion, toRelease):
     os.system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
