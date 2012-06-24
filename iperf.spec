Summary:	Network performance measurement tool
Summary(pl):	Narz�dzie do szacowania wydajno�ci sieci
Name:		iperf
Version:	1.7.0
Release:	0.1
License:	BSD-like
Group:		Networking
Source0:	http://dast.nlanr.net/Projects/Iperf/%{name}-%{version}-source.tar.gz
# Source0-md5:	3e4aea85822bcf10ed14040f4b26bd26
URL:		http://dast.nlanr.net/Projects/Iperf/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iperf is a network performance measurement tool.

While tools to measure network performance, such as ttcp, exist, most
are very old and have confusing options. Iperf was developed as a
modern alternative for measuring TCP and UDP bandwidth performance.

Iperf is a tool to measure maximum TCP bandwidth, allowing the tuning
of various parameters and UDP characteristics. Iperf reports
bandwidth, delay jitter, datagram loss.

%description -l pl
Iperf to narz�dzie do szacowania wydajno�ci sieci.

O ile narz�dzia do okre�lania wydajno�ci sieci, takie jak ttcp,
istniej�, to wi�kszo�� z nich jest bardzo stara i ma myl�ce opcje.
Iperf zosta� stworzony jako wsp�czesna alternatywa do szacowania
wydajno�ci pasma TCP i UDP.

Iperf to narz�dzie okre�laj�ce maksymalne pasmo TCP, umo�liwiaj�ce
dostrajanie r�nych parametr�w i charakterystyk UDP. Iperf raportuje
pasmo, op�nienia i straty datagram�w.

%prep
%setup -q

%build
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
