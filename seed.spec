#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	JavaScript interpreter
Summary(pl.UTF-8):	Interpreter JavaScript
Name:		seed
Version:	2.30.0
Release:	1
License:	LGPL v3
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seed/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	dd09d22c6a06b4bbef7320bb6a715c0f
URL:		http://live.gnome.org/Seed
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.7
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-js-common
BuildRequires:	gobject-introspection-devel >= 0.6.3
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gtk-webkit-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libffi-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	mpfr-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel
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
umożliwia pisanie samodzielnych aplikacji w JavaScript, jak również
łatwe ich rozszerzanie w JavaScript.

%package devel
Summary:	Header files for seed library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki seed
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	gobject-introspection-devel
Requires:	gtk-webkit-devel

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
	--disable-silent-rules \
	%{__enable_disable apidocs gtk-doc} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/seed{,-%{version}}

rm -f $RPM_BUILD_ROOT%{_libdir}/seed/libseed*.{a,la}

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
%attr(755,root,root) %{_libdir}/libseed.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libseed.so.0
%dir %{_libdir}/seed
%attr(755,root,root) %{_libdir}/seed/libseed_cairo.so
%attr(755,root,root) %{_libdir}/seed/libseed_canvas.so
%attr(755,root,root) %{_libdir}/seed/libseed_dbusnative.so
%attr(755,root,root) %{_libdir}/seed/libseed_example.so
%attr(755,root,root) %{_libdir}/seed/libseed_ffi.so
%attr(755,root,root) %{_libdir}/seed/libseed_gettext.so
%attr(755,root,root) %{_libdir}/seed/libseed_gtkbuilder.so
%attr(755,root,root) %{_libdir}/seed/libseed_libxml.so
%attr(755,root,root) %{_libdir}/seed/libseed_mpfr.so
%attr(755,root,root) %{_libdir}/seed/libseed_multiprocessing.so
%attr(755,root,root) %{_libdir}/seed/libseed_os.so
%attr(755,root,root) %{_libdir}/seed/libseed_readline.so
%attr(755,root,root) %{_libdir}/seed/libseed_sandbox.so
%attr(755,root,root) %{_libdir}/seed/libseed_sqlite.so
%{_datadir}/seed
%{_mandir}/man1/seed.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libseed.so
%{_libdir}/libseed.la
%{_includedir}/seed
%{_pkgconfigdir}/seed.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libseed.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/seed
%endif
