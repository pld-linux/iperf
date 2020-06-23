Summary:	Network performance measurement tool
Summary(pl.UTF-8):	Narzędzie do szacowania wydajności sieci
Name:		iperf
Version:	2.0.13
Release:	1
License:	BSD-like
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/iperf2/%{name}-%{version}.tar.gz
# Source0-md5:	31ea1c6d5cbf80b16ff3abe4288dad5e
Patch0:		%{name}-2.0.5-tcpdual.patch
URL:		http://iperf2.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iperf is a network performance measurement tool.

While tools to measure network performance, such as ttcp, exist, most
are very old and have confusing options. Iperf was developed as a
modern alternative for measuring TCP and UDP bandwidth performance.

Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning
of various parameters and UDP characteristics. Iperf reports
bandwidth, delay jitter, datagram loss.

%description -l pl.UTF-8
Iperf to narzędzie do szacowania wydajności sieci.

O ile narzędzia do określania wydajności sieci, takie jak ttcp,
istnieją, to większość z nich jest bardzo stara i ma mylące opcje.
Iperf został stworzony jako współczesna alternatywa do szacowania
wydajności pasma TCP i UDP.

Iperf to narzędzie określające maksymalne pasmo TCP, umożliwiające
dostrajanie różnych parametrów i charakterystyk UDP. Iperf raportuje
pasmo, opóźnienia i straty datagramów.

%prep
%setup -q
#%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*.html doc/*.gif
%attr(755,root,root) %{_bindir}/iperf
%{_mandir}/man1/*
