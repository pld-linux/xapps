#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	python2		# CPython 2.x binding
%bcond_without	python3		# CPython 3.x binding
%bcond_without	static_libs	# static library
#
Summary:	Components common to multiple desktop environments
Summary(pl.UTF-8):	Komponenty wspólne dla wielu środowisk graficznych
Name:		xapps
Version:	2.8.3
Release:	1
License:	LGPL v3+ (library), GPL v3+ (xfce4-set-wallpaper tool)
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/xapp/tags
Source0:	https://github.com/linuxmint/xapp/archive/%{version}/xapp-%{version}.tar.gz
# Source0-md5:	edd9ad7a643ebd118ea7d852668829f6
URL:		https://github.com/linuxmint/xapp
BuildRequires:	cairo-devel
BuildRequires:	cairo-gobject-devel
BuildRequires:	dbus-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.22.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	libgnomekbd-devel
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python >= 2
BuildRequires:	python-pygobject3-devel >= 3
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-pygobject3-devel >= 3
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	hicolor-icon-theme
# for xapp-gpu-offload
Requires:	python3-xapps-overrides = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project gathers the components which are common to multiple
desktop environments and required to implement cross-DE solutions.

This package contains a set of resources and tools.

%description -l pl.UTF-8
Ten projekt gromadzi komponenty wspólne dla wielu środowisk
graficznych, wymagane do implementowania rozwiązań działających w
wielu różnych środowiskach.

Ten pakiet zawiera zbiór zasobów i narzędzi.

%package libs
Summary:	X applications utility library
Summary(pl.UTF-8):	Biblioteka narzędziowa dla aplikacji X
License:	LGPL v3+
Group:		X11/Applications
Requires:	gdk-pixbuf2 >= 2.22.0
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+3 >= 3.22

%description libs
X applications utility library.

%description libs -l pl.UTF-8
Biblioteka narzędziowa dla aplikacji X.

%package devel
Summary:	Header files for xapp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki xapp
License:	LGPL v3+
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo-devel
Requires:	gdk-pixbuf2-devel >= 2.22.0
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.22
Requires:	libgnomekbd-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libxkbfile-devel

%description devel
Header files for xapp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki xapp.

%package static
Summary:	Static xapp library
Summary(pl.UTF-8):	Statyczna biblioteka xapp
License:	LGPL v3+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static xapp library.

%description static -l pl.UTF-8
Statyczna biblioteka xapp.

%package apidocs
Summary:	API documentation for xapp library
Summary(pl.UTF-8):	Dokumentacja API biblioteki xapp
License:	LGPL v3+
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for xapp library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki xapp.

%package glade
Summary:	Glade catalog file for xapp library
Summary(pl.UTF-8):	Plik katalogu Glade dla biblioteki xapp
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	glade >= 2
BuildArch:	noarch

%description glade
Glade catalog file for xapp library.

%description glade -l pl.UTF-8
Plik katalogu Glade dla biblioteki xapp.

%package -n vala-xapp
Summary:	Vala API for xapp library
Summary(pl.UTF-8):	API języka Vala do biblioteki xapp
License:	LGPL v3+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala
BuildArch:	noarch

%description -n vala-xapp
Vala API for xapp library.

%description -n vala-xapp -l pl.UTF-8
API języka Vala do biblioteki xapp.

%package -n python-xapps-overrides
Summary:	Python 2 binding for xapp library
Summary(pl.UTF-8):	Wiązanie Pythona 2 do biblioteki xapp
License:	LGPL v3+
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python-pygobject3 >= 3
Obsoletes:	python-xapp < 1.4.8

%description -n python-xapps-overrides
Python 2 binding for xapp library.

%description -n python-xapps-overrides -l pl.UTF-8
Wiązanie Pythona 2 do biblioteki xapp.

%package -n python3-xapps-overrides
Summary:	Python 3 binding for xapp library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki xapp
License:	LGPL v3+
Group:		Libraries/Python
Requires:	%{name}-libs = %{version}-%{release}
Requires:	python3-pygobject3 >= 3
Obsoletes:	python3-xapp < 1.4.8

%description -n python3-xapps-overrides
Python 3 binding for xapp library.

%description -n python3-xapps-overrides -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki xapp.

%package -n mate-applet-xapp-status
Summary:	XApp Status Applet for MATE
Summary(pl.UTF-8):	Applet stanu XApp dla MATE
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	mate-panel >= 1.18
Requires:	python3-xapps-overrides = %{version}-%{release}

%description -n mate-applet-xapp-status
XApp Status Applet for MATE - area where XApp status icons appear.

%description -n mate-applet-xapp-status -l pl.UTF-8
Applet stanu XApp dla MATE - miejsce, gdzie pojawiają się ikony stanu
XApp.

%prep
%setup -q -n xapp-%{version}

%build
%meson build \
	%{!?with_static_libs:--default-library=shared} \
	%{?with_apidocs:-Ddocs=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%if %{with python2}
# since 1.8.0 python 2 module is no longer installed
install -Dp pygobject/XApp.py $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides/XApp.py
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%endif

%if %{with python3}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%endif

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang xapp

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	-n mate-applet-xapp-status
%update_icon_cache hicolor

%postun	-n mate-applet-xapp-status
%update_icon_cache hicolor

%files -f xapp.lang
%defattr(644,root,root,755)
%doc AUTHORS README.md debian/changelog
# utility apps, not related to library
%attr(755,root,root) %{_bindir}/pastebin
%attr(755,root,root) %{_bindir}/upload-system-info
%attr(755,root,root) %{_bindir}/xapp-gpu-offload
%attr(755,root,root) %{_bindir}/xfce4-set-wallpaper
%attr(755,root,root) /etc/X11/xinit/xinitrc.d/80xapp-gtk3-module.sh
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libxapp-gtk3-module.so
# misc data, some for use with library, some independently
%{_datadir}/glib-2.0/schemas/org.x.apps.gschema.xml
%{_iconsdir}/hicolor/scalable/actions/add-files-to-archive-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/category-search-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/extract-archive-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/media-mount-symbolic.svg
%{_iconsdir}/hicolor/scalable/actions/view-*-symbolic*.svg
%{_iconsdir}/hicolor/scalable/actions/xapp-*-symbolic*.svg
%{_iconsdir}/hicolor/scalable/apps/xapp-favorites-app.svg
%{_iconsdir}/hicolor/scalable/apps/xapp-favorites-app-symbolic.svg
%{_iconsdir}/hicolor/scalable/categories/xapp-prefs-*-symbolic.svg
%{_iconsdir}/hicolor/scalable/emblems/emblem-xapp-favorite.svg
%{_iconsdir}/hicolor/scalable/places/xapp-user-favorites.svg
%{_iconsdir}/hicolor/scalable/places/xapp-user-favorites-symbolic.svg

# status notifier watcher
%dir %{_libdir}/xapps
%attr(755,root,root) %{_libdir}/xapps/xapp-sn-watcher
/etc/xdg/autostart/xapp-sn-watcher.desktop
%{_datadir}/dbus-1/services/org.x.StatusNotifierWatcher.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxapp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxapp.so.1
%{_libdir}/girepository-1.0/XApp-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxapp.so
%{_includedir}/xapp
%{_datadir}/gir-1.0/XApp-1.0.gir
%{_pkgconfigdir}/xapp.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxapp.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libxapp
%endif

%files glade
%defattr(644,root,root,755)
%{_datadir}/glade/catalogs/xapp-glade-catalog.xml

%files -n vala-xapp
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/xapp.deps
%{_datadir}/vala/vapi/xapp.vapi

%if %{with python2}
%files -n python-xapps-overrides
%defattr(644,root,root,755)
%{py_sitedir}/gi/overrides/XApp.py[co]
%endif

%if %{with python3}
%files -n python3-xapps-overrides
%defattr(644,root,root,755)
%{py3_sitedir}/gi/overrides/XApp.py
%{py3_sitedir}/gi/overrides/__pycache__/XApp.cpython-*.py[co]
%endif

%files -n mate-applet-xapp-status
%defattr(644,root,root,755)
%dir %{_libexecdir}/xapps
%attr(755,root,root) %{_libexecdir}/xapps/mate-xapp-status-applet.py
%{_libexecdir}/xapps/applet_constants.py
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%{_datadir}/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet
%{_iconsdir}/hicolor/scalable/apps/xapp-mate-status-applet.svg
