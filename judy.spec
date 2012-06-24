Summary:	Exteremelly fast dynamic libraries in C
Summary(pl):	Ekstremalnie szybkie dynamiczne tablice w C
Name:		judy
Version:	1.0.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/judy/Judy-%{version}.tar.gz
# Source0-md5:	7d1271b1122ddc067f94f0f35a321bd6
URL:		http://judy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Judy is a library developed by HP for superfast dynamic arrays in C.

%description -l pl
Judy jest bibliotek� opracowan� przez HP implementuj�c� bardzo szybkie
dynamiczne tablice w C.

%package devel
Summary:	Development files for Judy
Summary(pl):	Pliki nag��wkowe dla Judy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Documentation and header files needed to compile programs using Judy.

%description devel -l pl
Dokumentacja i pliki nag��wkowe potrzebne do kompilacji program�w w
Judy.

%package static
Summary:	Judy static libraries
Summary(pl):	Biblioteki statyczne Judy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Judy static libraries.

%description static -l pl
Biblioteki statyczne Judy.

%prep
%setup -q -n Judy-%{version}

%build
%configure
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
%doc doc/int/* AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/Judy.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
