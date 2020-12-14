#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openshot-qt
Version  : 2.5.1
Release  : 3
URL      : https://github.com/OpenShot/openshot-qt/archive/v2.5.1.tar.gz
Source0  : https://github.com/OpenShot/openshot-qt/archive/v2.5.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: openshot-qt-bin = %{version}-%{release}
Requires: openshot-qt-data = %{version}-%{release}
Requires: openshot-qt-license = %{version}-%{release}
Requires: openshot-qt-python = %{version}-%{release}
Requires: openshot-qt-python3 = %{version}-%{release}
BuildRequires : PyQt5
BuildRequires : buildreq-distutils3
BuildRequires : pyside2-setup
BuildRequires : qscintilla
BuildRequires : sip

%description
To compile a Qt resource file with new icons, follow these steps:
1) Edit the resource file, and add files to it (the *.qrc files) using QtCreator
2) Compile this into a Python file, either:
$ make
or, if make is unavailable:
$ pyrcc5 openshot.qrc -o openshot_rc.py

%package bin
Summary: bin components for the openshot-qt package.
Group: Binaries
Requires: openshot-qt-data = %{version}-%{release}
Requires: openshot-qt-license = %{version}-%{release}

%description bin
bin components for the openshot-qt package.


%package data
Summary: data components for the openshot-qt package.
Group: Data

%description data
data components for the openshot-qt package.


%package license
Summary: license components for the openshot-qt package.
Group: Default

%description license
license components for the openshot-qt package.


%package python
Summary: python components for the openshot-qt package.
Group: Default
Requires: openshot-qt-python3 = %{version}-%{release}

%description python
python components for the openshot-qt package.


%package python3
Summary: python3 components for the openshot-qt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openshot-qt package.


%prep
%setup -q -n openshot-qt-2.5.1
cd %{_builddir}/openshot-qt-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583293425
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openshot-qt
cp %{_builddir}/openshot-qt-2.5.1/COPYING %{buildroot}/usr/share/package-licenses/openshot-qt/c1d5663b31d3742b9487146938059a539e4b4b29
cp %{_builddir}/openshot-qt-2.5.1/src/images/Humanity/COPYING %{buildroot}/usr/share/package-licenses/openshot-qt/dfac199a7539a404407098a2541b9482279f690d
cp %{_builddir}/openshot-qt-2.5.1/src/resources/license.txt %{buildroot}/usr/share/package-licenses/openshot-qt/c1d5663b31d3742b9487146938059a539e4b4b29
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)
/usr/lib/mime/packages/openshot-qt

%files bin
%defattr(-,root,root,-)
/usr/bin/openshot-qt

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.openshot.OpenShot.desktop
/usr/share/icons/hicolor/256x256/apps/openshot-qt.png
/usr/share/icons/hicolor/512x512/apps/openshot-qt.png
/usr/share/icons/hicolor/64x64/apps/openshot-qt.png
/usr/share/icons/hicolor/scalable/apps/openshot-qt.svg
/usr/share/metainfo/org.openshot.OpenShot.appdata.xml
/usr/share/mime-packages/org.openshot.OpenShot.xml
/usr/share/pixmaps/openshot-qt.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openshot-qt/c1d5663b31d3742b9487146938059a539e4b4b29
/usr/share/package-licenses/openshot-qt/dfac199a7539a404407098a2541b9482279f690d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
