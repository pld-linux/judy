Summary:	exteremelly fast dynamic libraries in C
Summary(pl):	ekstremalnie szybkie dynamiczne tablice w C
Name:		judy
Version:	0initial
Release:	0.1
License:	LGPL
Group:		Libraries
Vendor:		Doug Baskins for Hewlett-Packard
Source0:	http://prdownloads.sourceforge.net/judy/Judy-initial_LGPL.src.tar.gz
Patch0:		-
URL:		http://www.sourcejudy.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package devel
Summary:	-
Summary(pl):	-
Group:		-

%description devel

%description devel -l pl

%prep
%setup -q -n Judy-initial_LGPL
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
