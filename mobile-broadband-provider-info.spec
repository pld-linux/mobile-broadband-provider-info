Summary:	Mobile broadband provider database
Name:		mobile-broadband-provider-info
Version:	20100510
Release:	1
License:	Public Domain
Group:		Base
# git clone git://git.gnome.org/mobile-broadband-provider-info
# git archive --format=tar --prefix=mobile-broadband-provider-info-%{version}/ %{version} | bzip2 > mobile-broadband-provider-info-%{version}.tar.bz2
Source0:	%{name}-%{version}.tar.bz2
URL:		http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary:	Development files for mobile-broadband-provider-info
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%{_datadir}/%{name}/serviceproviders.2.dtd
%{_datadir}/%{name}/serviceproviders.xml

%files devel
%defattr(644,root,root,755)
%{_datadir}/pkgconfig/%{name}.pc
