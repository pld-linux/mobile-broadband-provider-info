Summary:	Mobile broadband provider database
Summary(pl.UTF-8):	Baza danych dostawców szerokopasmowych łącz komórkowych
Name:		mobile-broadband-provider-info
Version:	20210805
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	https://download.gnome.org/sources/mobile-broadband-provider-info/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	c8c10bc5df814fd696476f2f570b80f1
URL:		https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
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
%doc COPYING README
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/apns-conf.xml
%{_datadir}/%{name}/serviceproviders.2.dtd
%{_datadir}/%{name}/serviceproviders.xml

%files devel
%defattr(644,root,root,755)
%{_npkgconfigdir}/mobile-broadband-provider-info.pc
