#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	JavaScript interpreter
Summary(pl.UTF-8):	Interpreter JavaScriptu
Name:		seed
Version:	3.8.1
Release:	1
License:	LGPL v2+
Group:		Development/Languages
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seed/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	f5afeb04343e0cb56d2396f0d0458988
URL:		http://live.gnome.org/Seed
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	cairo-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-js-common
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtk-webkit3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mpfr-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seed is a library and interpreter, dynamically bridging (through
GObjectIntrospection) the WebKit JavaScriptCore engine, with the GNOME
platform. Seed serves as something which enables you to write
standalone applications in JavaScript, or easily enable your
application to be extensible in JavaScript.

%description -l pl.UTF-8
Seed jest biblioteką i interpreterem, dynamicznie łączącym (poprzez
GObjectIntrospection) silnik WebKit JavaScriptCore z GNOME. Seed
umożliwia pisanie samodzielnych aplikacji w JavaScripcie, jak również
łatwe ich rozszerzanie w JavaScripcie.

%package devel
Summary:	Header files for seed library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki seed
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	gobject-introspection-devel >= 0.10.0
Requires:	gtk-webkit3-devel

%description devel
Header files for seed library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki seed.

%package static
Summary:	Static seed library
Summary(pl.UTF-8):	Statyczna biblioteka seed
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static seed library.

%description static -l pl.UTF-8
Statyczna biblioteka seed.

%package apidocs
Summary:	seed library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki seed
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
API documentation for seed library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki seed.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{__enable_disable apidocs gtk-doc} \
	--disable-silent-rules \
	--enable-xorg-module \
	--with-html-dir=%{_gtkdocdir} \
	--with-webkit=3.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/seed{,-%{version}}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/seed-gtk3/libseed*.{a,la} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%if %{without apidocs}
rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc %{_docdir}/seed-%{version}
%attr(755,root,root) %{_bindir}/seed
%attr(755,root,root) %{_libdir}/libseed-gtk3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libseed-gtk3.so.0
%dir %{_libdir}/seed-gtk3
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_DynamicObject.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_cairo.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_canvas.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_dbusnative.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_example.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_ffi.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_gettext.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_gtkbuilder.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_libxml.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_mpfr.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_multiprocessing.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_os.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_readline.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_sandbox.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_sqlite.so
%attr(755,root,root) %{_libdir}/seed-gtk3/libseed_xorg.so
%{_datadir}/seed-gtk3
%{_mandir}/man1/seed.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libseed-gtk3.so
%{_includedir}/seed-gtk3
%{_pkgconfigdir}/seed.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libseed-gtk3.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/seed
%endif
