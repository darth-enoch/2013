#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "iwlwifi-6050-ucode-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/lib/firmware", "*.ucode")
    pisitools.dodoc("LICENSE*", "README*")
