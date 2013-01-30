#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("./configure.tcl --nodepcheck --quiet --libdir=usr/lib/tcl8.6 --bindir=usr/bin --prefix=usr/lib --bintarget=/usr/share/tv-viewer")


def install():
    shelltools.system("./install.tcl")

    pisitools.insinto("/usr/bin", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/bin/*")    
    pisitools.insinto("/usr/lib/tcl8.6", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/tcl8.6/*")
    pisitools.insinto("/usr/share/tv-viewer", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/share/tv-viewer/*")
    pisitools.insinto("/usr/share/man/man1", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/share/man/man1/*")
    pisitools.insinto("/usr/share/pixmaps", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/share/pixmaps/*")
    pisitools.insinto("/usr/share/applications", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/share/applications/*")   
    pisitools.insinto("/usr/share/doc", "/var/pisi/tv-viewer-0.8.2-1/work/tv-viewer-0.8.2b1/usr/lib/doc/*")
