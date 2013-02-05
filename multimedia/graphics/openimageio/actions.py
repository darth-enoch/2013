#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    cmaketools.make()

def install():
    pisitools.insinto("/usr/bin", "/var/pisi/openimageio*/work/dist/*/bin/*")
    pisitools.insinto("/usr/include", "/var/pisi/openimageio*/work/dist/*/include/*")
    pisitools.insinto("/usr/lib", "/var/pisi/openimageio*/work/dist/*/lib/*")
    pisitools.insinto("/usr/lib", "/var/pisi/openimageio*/work/dist/*/python/*")
    pisitools.insinto("/usr/share/doc", "/var/pisi/openimageio*/work/dist/*/doc*")
    
    pisitools.dodoc("CREDITS", "LICENSE", "README.*")
