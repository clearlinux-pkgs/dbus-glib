#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0xE05AE1478F814C4F (smcv@debian.org)
#
Name     : dbus-glib
Version  : 0.112
Release  : 28
URL      : https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.112.tar.gz
Source0  : https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.112.tar.gz
Source1  : https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.112.tar.gz.asc
Summary  : GLib integration for the free desktop message bus
Group    : Development/Tools
License  : AFL-2.1 GPL-2.0 GPL-2.0+
Requires: dbus-glib-bin = %{version}-%{release}
Requires: dbus-glib-data = %{version}-%{release}
Requires: dbus-glib-lib = %{version}-%{release}
Requires: dbus-glib-libexec = %{version}-%{release}
Requires: dbus-glib-license = %{version}-%{release}
Requires: dbus-glib-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : docbook-xml
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : glib-bin
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pypi-six
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
%setup -q -n dbus-glib-0.112
cd %{_builddir}/dbus-glib-0.112
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689367173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689367173
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dbus-glib
cp %{_builddir}/dbus-glib-%{version}/COPYING %{buildroot}/usr/share/package-licenses/dbus-glib/aa0b83447f95c9e4b144f51b7590c77ee5033c5c || :
cp %{_builddir}/dbus-glib-%{version}/dbus-gmain/COPYING %{buildroot}/usr/share/package-licenses/dbus-glib/b79a4d61264303b3341005eef4ce4015f178b1b8 || :
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
/usr/lib64/libdbus-glib-1.so.2.3.5

%files libexec
%defattr(-,root,root,-)
/usr/libexec/dbus-bash-completion-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dbus-glib/aa0b83447f95c9e4b144f51b7590c77ee5033c5c
/usr/share/package-licenses/dbus-glib/b79a4d61264303b3341005eef4ce4015f178b1b8

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dbus-binding-tool.1
