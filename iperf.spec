Summary:	Network performance measurement tool
Summary(pl.UTF-8):   Narzędzie do szacowania wydajności sieci
Name:		iperf
Version:	1.7.0
Release:	2
License:	BSD-like
Group:		Networking
Source0:	http://dast.nlanr.net/Projects/Iperf/%{name}-%{version}-source.tar.gz
# Source0-md5:	3e4aea85822bcf10ed14040f4b26bd26
URL:		http://dast.nlanr.net/Projects/Iperf/
BuildRequires:	automake
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

%build
cd cfg
cp -f /usr/share/automake/config.* .
%configure
cd ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install iperf $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README KNOWN_PROBLEMS
%attr(755,root,root) %{_bindir}/iperf
