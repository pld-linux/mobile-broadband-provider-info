Summary:	Mobile broadband provider database
Name:		mobile-broadband-provider-info
Version:	20110511
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mobile-broadband-provider-info/20110511/%{name}-%{version}.tar.bz2
# Source0-md5:	b73cc0c58bb1a97f6befa777fc2fd576
URL:		http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
BuildRequires:	autoconf
BuildRequires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary:	Development files for mobile-broadband-provider-info
Group:		Development/Libraries

%description devel
Development files for mobile-broadband-provider-info.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/serviceproviders.2.dtd
%{_datadir}/%{name}/serviceproviders.xml

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/%{name}.pc
