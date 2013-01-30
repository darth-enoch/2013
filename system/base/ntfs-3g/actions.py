#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--disable-static \
                         --disable-ldconfig \
                         --sbindir=/sbin \
                         --bindir=/bin \
                         --libdir=/usr/lib \
                         --docdir=/usr/share/doc/%s" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/pkgconfig", "libntfs-3g/*.pc")

    # Create some compat symlinks

    pisitools.dosym("mount.ntfs-3g", "/sbin/mount.ntfs-fuse")
    pisitools.dosym("mount.ntfs-3g", "/sbin/mount.ntfs")
    pisitools.dosym("ntfs-3g", "/bin/ntfsmount")

    pisitools.dosym("/bin/ntfs-3g", "/usr/bin/ntfs-3g")
    pisitools.dosym("/bin/ntfsmount", "/usr/bin/ntfsmount")

    pisitools.remove("/usr/share/man/man8/ntfsfix.8")
    pisitools.remove("/usr/share/man/man8/ntfsclone.8")
    pisitools.remove("/usr/share/man/man8/ntfscmp.8")
    pisitools.remove("/usr/share/man/man8/ntfsresize.8")
    pisitools.remove("/sbin/mkfs.ntfs")
    pisitools.remove("/usr/share/man/man8/ntfscluster.8")
    pisitools.remove("/usr/share/man/man8/ntfsinfo.8")
    pisitools.remove("/usr/share/man/man8/ntfslabel.8")
    pisitools.remove("/usr/share/man/man8/mkfs.ntfs.8")
    pisitools.remove("/usr/share/man/man8/ntfsundelete.8")
    pisitools.remove("/usr/share/man/man8/ntfscp.8")
    pisitools.remove("/usr/share/man/man8/ntfsls.8")
    pisitools.remove("/usr/share/man/man8/mkntfs.8")
    pisitools.remove("/usr/share/man/man8/ntfsprogs.8")
    pisitools.remove("/usr/share/man/man8/ntfscat.8")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "NEWS", "README")
