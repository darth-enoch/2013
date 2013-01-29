#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -lm" % get.LDFLAGS())
    autotools.autoreconf("-fi")
    autotools.configure("--with-libwrap \
                         --enable-static=no \
                         --enable-alsa \
                         --enable-ipv6 \
                         --enable-oss \
                         --disable-arts \
                         --disable-dependency-tracking \
                         --sysconfdir=/etc/esd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Delete the esound library
    pisitools.remove("/usr/bin/esd")
    pisitools.remove("/usr/share/man/man1/esd.1*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "MAINTAINERS", "NEWS", "README", "TIPS", "TODO")

