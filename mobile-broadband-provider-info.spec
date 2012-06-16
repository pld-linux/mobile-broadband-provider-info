Summary:	Mobile broadband provider database
Name:		mobile-broadband-provider-info
Version:	20120614
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mobile-broadband-provider-info/20120614/%{name}-%{version}.tar.xz
# Source0-md5:	dfa66a77ce27071b0882e2f822eecde5
URL:		http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
