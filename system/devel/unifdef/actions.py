#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "unifdef-%s/Debian" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make('CC="%s" CFLAGS="%s"' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.dobin("src/unifdefall.sh")

