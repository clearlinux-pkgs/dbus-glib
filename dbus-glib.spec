#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-glib
Version  : 0.110
Release  : 22
URL      : http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.110.tar.gz
Source0  : http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.110.tar.gz
Source99 : http://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.110.tar.gz.asc
Summary  : GLib bindings for DBUS
Group    : Development/Tools
License  : AFL-2.1 GPL-2.0 GPL-2.0+
Requires: dbus-glib-bin = %{version}-%{release}
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-lib = %{version}-%{release}
Requires: dbus-glib-libexec = %{version}-%{release}
Requires: dbus-glib-license = %{version}-%{release}
Requires: dbus-glib-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : docbook-xml
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glib-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : six
Patch1: 0001-Use-system-location-of-bash-completions.patch

%description
dbus-glib is a deprecated D-Bus binding for GLib.
dbus-glib receives minimal maintenance and security fixes for the benefit
of projects like Telepathy and NetworkManager that still rely on it, but
should not be used in new projects (and existing projects should try
to move away from it, too). Please use GDBus, part of GLib since 2.26.

%package bin
Summary: bin components for the dbus-glib package.
Group: Binaries
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-libexec = %{version}-%{release}
Requires: dbus-glib-license = %{version}-%{release}

%description bin
bin components for the dbus-glib package.


%package data
Summary: data components for the dbus-glib package.
Group: Data

%description data
data components for the dbus-glib package.


%package dev
Summary: dev components for the dbus-glib package.
Group: Development
Requires: dbus-glib-lib = %{version}-%{release}
Requires: dbus-glib-bin = %{version}-%{release}
Requires: dbus-glib-data = %{version}-%{release}
Provides: dbus-glib-devel = %{version}-%{release}
Requires: dbus-glib = %{version}-%{release}

%description dev
dev components for the dbus-glib package.


%package dev32
Summary: dev32 components for the dbus-glib package.
Group: Default
Requires: dbus-glib-lib32 = %{version}-%{release}
Requires: dbus-glib-bin = %{version}-%{release}
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-dev = %{version}-%{release}

%description dev32
dev32 components for the dbus-glib package.


%package doc
Summary: doc components for the dbus-glib package.
Group: Documentation
Requires: dbus-glib-man = %{version}-%{release}

%description doc
doc components for the dbus-glib package.


%package lib
Summary: lib components for the dbus-glib package.
Group: Libraries
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-libexec = %{version}-%{release}
Requires: dbus-glib-license = %{version}-%{release}

%description lib
lib components for the dbus-glib package.


%package lib32
Summary: lib32 components for the dbus-glib package.
Group: Default
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-license = %{version}-%{release}

%description lib32
lib32 components for the dbus-glib package.


%package libexec
Summary: libexec components for the dbus-glib package.
Group: Default
Requires: dbus-glib-license = %{version}-%{release}

%description libexec
libexec components for the dbus-glib package.


%package license
Summary: license components for the dbus-glib package.
Group: Default

%description license
license components for the dbus-glib package.


%package man
Summary: man components for the dbus-glib package.
Group: Default

%description man
man components for the dbus-glib package.


%prep
%setup -q -n dbus-glib-0.110
%patch1 -p1
pushd ..
cp -a dbus-glib-0.110 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557083490
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1557083490
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-glib
cp COPYING %{buildroot}/usr/share/package-licenses/dbus-glib/COPYING
cp dbus-gmain/COPYING %{buildroot}/usr/share/package-licenses/dbus-glib/dbus-gmain_COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dbus-binding-tool

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/dbus-bash-completion.sh

%files dev
%defattr(-,root,root,-)
/usr/include/dbus-1.0/dbus/dbus-glib-bindings.h
/usr/include/dbus-1.0/dbus/dbus-glib-lowlevel.h
/usr/include/dbus-1.0/dbus/dbus-glib.h
/usr/include/dbus-1.0/dbus/dbus-gtype-specialized.h
/usr/include/dbus-1.0/dbus/dbus-gvalue-parse-variant.h
/usr/lib64/libdbus-glib-1.so
/usr/lib64/pkgconfig/dbus-glib-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdbus-glib-1.so
/usr/lib32/pkgconfig/32dbus-glib-1.pc
/usr/lib32/pkgconfig/dbus-glib-1.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/dbus-glib/api-index-full.html
/usr/share/gtk-doc/html/dbus-glib/ch01.html
/usr/share/gtk-doc/html/dbus-glib/ch02.html
/usr/share/gtk-doc/html/dbus-glib/ch03.html
/usr/share/gtk-doc/html/dbus-glib/dbus-binding-tool.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBus-GLib-low-level.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBus-GObject-related-functions.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGConnection.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGError.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGMessage.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGMethod.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-DBusGProxy.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib-Specializable-GType-System.html
/usr/share/gtk-doc/html/dbus-glib/dbus-glib.devhelp2
/usr/share/gtk-doc/html/dbus-glib/home.png
/usr/share/gtk-doc/html/dbus-glib/index.html
/usr/share/gtk-doc/html/dbus-glib/left-insensitive.png
/usr/share/gtk-doc/html/dbus-glib/left.png
/usr/share/gtk-doc/html/dbus-glib/right-insensitive.png
/usr/share/gtk-doc/html/dbus-glib/right.png
/usr/share/gtk-doc/html/dbus-glib/style.css
/usr/share/gtk-doc/html/dbus-glib/up-insensitive.png
/usr/share/gtk-doc/html/dbus-glib/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdbus-glib-1.so.2
/usr/lib64/libdbus-glib-1.so.2.3.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libdbus-glib-1.so.2
/usr/lib32/libdbus-glib-1.so.2.3.4

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dbus-bash-completion-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-glib/COPYING
/usr/share/package-licenses/dbus-glib/dbus-gmain_COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dbus-binding-tool.1
