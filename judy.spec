Summary:	exteremelly fast dynamic libraries in C
Summary(pl):	ekstremalnie szybkie dynamiczne tablice w C
Name:		judy
Version:	0initial
Release:	1
License:	LGPL
Group:		Libraries
Vendor:		Doug Baskins for Hewlett-Packard
Source0:	http://prdownloads.sourceforge.net/judy/Judy-initial_LGPL.src.tar.gz
URL:		http://www.sourcejudy.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

Judy is a library developed by HP for superfast dynamic arrays in C.

%description -l pl

Judy jest bibliotek± opracowan± przez HP implementuj±c± bardzo szybkie
dynamiczne tablice w C.

%package devel
Summary:	development files for Judy
Summary(pl):	pliki nag³ówkowe dla Judy
Group:		Development/Libraries

%description devel

Documentation and header files needed to compile programs using Judy

%description devel -l pl

Dokumentacja i pliki nag³ówkowe potrzebne do kompilacji programów w
Judy

%package static
Summary:	Judy static libraries
Summary(pl):	biblioteki statyczne Judy
Group:		Development/Libraries

%description static
Judy static libraries.

%description static -l pl

Biblioteki statyczne dla Judy

%prep
%setup -q -n Judy-initial_LGPL

%build

# this is not autoconfig; touch it and you're gonna die
./configure -f product
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

mv src/linux_ia32/product/deliver%{_datadir}/doc/Judy .
rm Judy/COPYRIGHT

cp -r src/linux_ia32/product/deliver/. $RPM_BUILD_ROOT/
install -d $RPM_BUILD_ROOT/%{_datadir}/judy/
mv Judy/demo $RPM_BUILD_ROOT/%{_datadir}/judy/

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
%attr(644,root,root) %{_mandir}/man3/*
%attr(644,root,root) %{_includedir}/Judy.h
%attr(755,root,root) %{_datadir}/judy

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.a
