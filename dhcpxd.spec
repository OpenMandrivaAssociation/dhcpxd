Summary:	DHCPXD Daemon
Name:		dhcpxd
Version:	1.0.3
Release:	%mkrel 17
License:	GPL
Group:		System/Servers

Source:		ftp://ftp.guido.yi.org:50021/dhcpxd-%{version}.tar.bz2
Patch1:		dhcpxd-1.0.3-resolvrdv.patch
Patch2:		dhcpxd-1.0.3-gcc-3.3.patch
Patch3:		dhcpxd-1.0.3-64bit-fixes.patch
Patch4:		dhcpxd-1.0.3-varargs.patch
Patch5:		dhcpxd-1.0.3-extra.patch

%description
The primary goal of this DHCP client is to conform to the DHCP specification
defined in RFC2131 which is now the draft standard. However, the client can
be told how to behave. Additionally, the client supports all-in-one-process
session managment as well as a process per session. It may also be used to
masquerade IP leases and has the capability of running on interface aliases.
Finally, perhaps the most advanced feature of the client is that all the
configuration that is required for setting up interfaces is in scripts that
are run at the appropriate times. 

%prep

%setup -q
%patch1 -p1 -b .resolvrdv
%patch2 -p1 -b .gcc3.3
%patch3 -p1 -b .64bit-fixes
%patch4 -p1 -b .varargs
%patch5 -p1 -b .extra

%build
%configure
%ifnarch alpha
perl -pi -e 's/-Wall/\$(RPM_OPT_FLAGS) -Wall/g;' Makefile
%endif

%ifnarch alpha
%make RPM_OPT_FLAGS="%optflags"
%endif

%ifarch alpha
%make
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dhcpxd
cp -f filter $RPM_BUILD_ROOT%{_sysconfdir}/dhcpxd
cp -df install/* $RPM_BUILD_ROOT%{_sysconfdir}/dhcpxd

ln -sf /dev/log $RPM_BUILD_ROOT%{_sysconfdir}/dhcpxd/out

install -m 500 dhcpxd $RPM_BUILD_ROOT/sbin/dhcpxd
install -m 644 dhcpxd.8 $RPM_BUILD_ROOT%{_mandir}/man8/dhcpxd.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/dhcpxd
/sbin/dhcpxd
%{_mandir}/man8/dhcpxd.8*


