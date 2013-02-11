#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#NoStrip = ["%s/lib/libreoffice/basis-link/share" % AppDir, "%s/lib/libreoffice/share" % AppDir]

shelltools.export("HOME", get.workDIR())
shelltools.export("LDFLAGS", "%s -L/usr/lib/nss" % get.LDFLAGS())
shelltools.export("ARCH_FLAGS", get.CXXFLAGS())
shelltools.export("LINKFLAGSOPTIMIZE", get.LDFLAGS())
shelltools.export("PYTHON", get.curPYTHON())

def setup():
    shelltools.system('./autogen.sh \
                       --with-vendor="Pardus Anka" \
                       --with-unix-wrapper="libreoffice" \
                       --with-ant-home="/usr/share/ant" \
                       --with-jdk-home="/opt/sun-jdk" \
                       --prefix=/usr --exec-prefix=/usr --sysconfdir=/etc \
                       --libdir=/usr/lib --mandir=/usr/share/man \
                       --enable-dependency-tracking \
                       --disable-verbose \
                       --disable-rpath \
                       --disable-crashdump \
                       --disable-ccache \
                       --disable-epm \
                       --disable-online-update \
                       --disable-pch \
                       --with-system-jars \
                       --with-system-libs \
                       --with-system-mythes \
                       --with-system-headers \
                       --with-lang="ALL" \
                       --enable-graphite \
                       --enable-cups \
                       --enable-dbus \
                       --enable-evolution2 \
                       --enable-gio \
                       --disable-gnome-vfs \
                       --disable-kde \
                       --enable-kde4 \
                       --enable-gtk3 \
                       --enable-largefile \
                       --enable-lockdown \
                       --enable-mergelibs \
                       --enable-opengl \
                       --enable-odk \
                       --enable-randr \
                       --enable-randr-link \
                       --enable-extension-integration \
                       --enable-scripting-beanshell \
                       --enable-scripting-javascript \
                       --enable-ext-wiki-publisher \
                       --enable-ext-nlpsolver \
                       --disable-ext-report-builder \
                       --disable-ext-mysql-connector \
                       --with-system-mysql \
                       --enable-python=system \
                       --enable-cairo-canvas \
                       --with-system-cairo \
                       --without-fonts \
                       --without-afms \
                       --without-ppds \
                       --with-system-libexttextcat \
                       --without-system-jfreereport \
                       --without-system-apache-commons \
                       --with-helppack-integration \
                       --with-system-beanshell \
                       --with-system-clucene \
                       --with-system-cppunit \
                       --with-system-graphite \
                       --with-system-libcmis \
                       --with-system-libwpg \
                       --with-system-libwps \
                       --with-system-libvisio \
                       --with-system-mdds \
                       --with-system-redland \
                       --with-system-ucpp \
                       --with-system-dicts \
                       --with-system-libexttextcat \
                       --with-system-nss \
                       --without-system-hsqldb \
                       --without-system-mozilla \
                       --without-myspell-dicts \
                       --without-system-npapi-headers \
                       --with-external-dict-dir=/usr/share/hunspell \
                       --with-external-hyph-dir=/usr/share/hyphen \
                       --with-external-thes-dir=/usr/share/mythes \
                       --with-alloc=system \
                       --with-system-sane \
                       --without-system-servlet-api \
                       --without-system-vigra \
                       --without-sun-templates \
                       --disable-fetch-external \
                       --with-parallelism=%s \
                       --with-external-tar="%s"' % (get.makeJOBS().replace("-j", ""), get.workDIR()))
        
def build():
    autotools.make()

def check():
    autotools.make("unitcheck")
    autotools.make("slowcheck")

def install():
    autotools.rawInstall("DESTDIR=%s distro-pack-install -o build -o check" % get.installDIR())
    
    for i in ["readmes/README_*", "CREDITS*", "LICENSE*", "NOTICE*"]:
        pisitools.domove("/usr/lib/libreoffice/%s" % i, "/usr/share/doc/libreoffice")
    pisitools.removeDir("/usr/lib/libreoffice/readmes")
