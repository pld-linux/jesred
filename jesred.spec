# $Revision: 1.1 $
Summary:	Filter, redirector and access controller plugin for Squid. 
Name:		jesred
Version:	1.2pl1
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://ivs.cs.uni-magdeburg.de/~elkner/webtools/src/%{name}-%{version}.tar.gz
Source1:	%{name}.conf
URL:		http://ivs.cs.uni-magdeburg.de/~elkner/webtools/jesred/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	squid

%define		_sysconfdir	/etc/%{name}

%description
Redirector for squid proxy

%prep
%setup -q
%build
%{__make} CFLAGS="%{rpmcflags} -I." DEFS="-DUSE_ACCEL -DDEFAULT_PATH=\"%{_sysconfdir}\"" XTRA_LIBS=""

%install
rm -rf $RPM_BUILD_ROOT


install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install jesred		$RPM_BUILD_ROOT%{_bindir}
install etc/redirect.*	$RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README

%post
echo "WARNING !!! WARNING !!! WARNING !!! WARNING !!!"
echo ""
echo "Modify the following line in the /etc/squid/squid.conf file:"
echo "redirect_program /usr/bin/jesred"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(750,root,squid) %dir %{_sysconfdir}
%attr(640,root,squid) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
