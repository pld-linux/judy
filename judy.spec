Summary:	Exteremelly fast dynamic libraries in C
Summary(pl):	Ekstremalnie szybkie dynamiczne tablice w C
Name:		judy
Version:	0initial
Release:	1
License:	LGPL
Group:		Libraries
Vendor:		Doug Baskins for Hewlett-Packard
Source0:	http://dl.sourceforge.net/judy/Judy-initial_LGPL.src.tar.gz
# Source0-md5:	7ca6ca87a8fca531a0a4b505f51296d4
Patch0:		%{name}-gcc3.patch
URL:		http://judy.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Judy is a library developed by HP for superfast dynamic arrays in C.

%description -l pl
Judy jest bibliotek± opracowan± przez HP implementuj±c± bardzo szybkie
dynamiczne tablice w C.

%package devel
Summary:	Development files for Judy
Summary(pl):	Pliki nag³ówkowe dla Judy
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Documentation and header files needed to compile programs using Judy.

%description devel -l pl
Dokumentacja i pliki nag³ówkowe potrzebne do kompilacji programów w
Judy.

%package static
Summary:	Judy static libraries
Summary(pl):	biblioteki statyczne Judy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Judy static libraries.

%description static -l pl
Biblioteki statyczne Judy.

%prep
%setup -q -n Judy-initial_LGPL
%patch0 -p1

%build
# this is not autoconf; touch it and you're gonna die
./configure -f product
%{__make} \
	EXTCCOPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

mv src/linux_ia32/product/deliver%{_datadir}/doc/Judy .
rm Judy/COPYRIGHT

cp -r src/linux_ia32/product/deliver/. $RPM_BUILD_ROOT/

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install Judy/demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc Judy/*
%{_mandir}/man3/*
%{_includedir}/Judy.h
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/[^r]*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/run_demo

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.a
