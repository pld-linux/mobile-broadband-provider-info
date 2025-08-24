Summary:	Mobile broadband provider database
Summary(pl.UTF-8):	Baza danych dostawców szerokopasmowych łącz komórkowych
Name:		mobile-broadband-provider-info
Version:	20240407
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	https://download.gnome.org/sources/mobile-broadband-provider-info/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	4768203b47c8125c82739a41de57b8d8
URL:		https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
BuildRequires:	meson >= 1.0.0
BuildRequires:	ninja >= 1.5
BuildRequires:	libxslt-progs
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%description -l pl.UTF-8
Pakiet mobile-broadband-provider-info zawiera listę dostawców
szerokopasmowych (3G) łącz komórkowych oraz związanych z nimi
informacji o sieciach i planach.

%package devel
Summary:	Development files for mobile-broadband-provider-info
Summary(pl.UTF-8):	Pliki programistyczne pakietu mobile-broadband-provider-info
Group:		Development/Libraries

%description devel
Development files for mobile-broadband-provider-info.

%description devel -l pl.UTF-8
Pliki programistyczne pakietu mobile-broadband-provider-info.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING MAINTAINERS NEWS README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/apns-conf.xml
%{_datadir}/%{name}/serviceproviders.2.dtd
%{_datadir}/%{name}/serviceproviders.xml

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mobile-broadband-provider-info.pc
