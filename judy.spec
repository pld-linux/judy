Summary:	Exteremelly fast dynamic libraries in C
Summary(pl.UTF-8):	Ekstremalnie szybkie dynamiczne tablice w C
Name:		judy
Version:	1.0.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/judy/Judy-%{version}.tar.gz
# Source0-md5:	115a0d26302676e962ae2f70ec484a54
URL:		http://judy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Judy is a library developed by HP for superfast dynamic arrays in C.

%description -l pl.UTF-8
Judy jest biblioteką opracowaną przez HP implementującą bardzo szybkie
dynamiczne tablice w C.

%package devel
Summary:	Development files for Judy
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Judy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Documentation and header files needed to compile programs using Judy.

%description devel -l pl.UTF-8
Dokumentacja i pliki nagłówkowe potrzebne do kompilacji programów
wykorzystujących bibliotekę Judy.

%package static
Summary:	Judy static library
Summary(pl.UTF-8):	Biblioteka statyczna Judy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Judy static library.

%description static -l pl.UTF-8
Biblioteka statyczna Judy.

%prep
%setup -q

%build
%configure
%{__make} -C tool
%{__make} -C doc -j1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libJudy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libJudy.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/int/*
%attr(755,root,root) %{_libdir}/libJudy.so
%{_libdir}/libJudy.la
%{_includedir}/Judy.h
%{_mandir}/man3/J1*.3*
%{_mandir}/man3/JH*.3*
%{_mandir}/man3/JL*.3*
%{_mandir}/man3/JS*.3*
%{_mandir}/man3/Judy*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libJudy.a
