Summary:	-
Summary(pl):	-
Name:		-
Version:	-
Release:	-
Epoch:		-
License:	- (enter GPL/LGPL/BSD/BSD-like/other license name here)
Group:		-
Vendor:		-
Icon:		-
Source0:	%{name}-%{version}.tar.gz
Source1:	-
Patch0:		-
URL:		-
BuildRequires:	-
PreReq:		-
Requires:	-
Requires(pre,post):	-
Requires(preun):	-
Requires(postun):	-
Provides:	-
Obsoletes:	-
Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%package subpackage
Summary:	-
Summary(pl):	-
Group:		-

%description subpackage

%description subpackage -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
aclocal
%{__autoconf}
autoheader
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%preun

%post

%postun

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files subpackage
%defattr(644,root,root,755)
%doc extras/*.gz
%{_datadir}/%{name}-ext
