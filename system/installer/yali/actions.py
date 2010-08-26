#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ="yali4-%s" % get.srcVERSION()
def setup():
    if get.ARCH() == "i686":
        repo_uri = "http://packages.pardus.org.tr/pardus/2011/stable/i686/pisi-index.xml.bz2"
    else:
        repo_uri = "http://packages.pardus.org.tr/pardus/2011/stable/x86_64/pisi-index.xml.bz2"

    pisitools.dosed("yali4/constants.py", "@REPO_URI@", repo_uri)

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
