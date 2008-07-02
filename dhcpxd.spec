Summary:	DHCPXD Daemon
Name:		dhcpxd
Version:	1.0.3
Release:	%mkrel 21
License:	GPL
Group:		System/Servers
Source:		ftp://ftp.guido.yi.org:50021/dhcpxd-%{version}.tar.bz2
Patch2:		dhcpxd-1.0.3-gcc-3.3.patch
Patch3:		dhcpxd-1.0.3-64bit-fixes.patch
Patch4:		dhcpxd-1.0.3-varargs.patch
Patch5:		dhcpxd-1.0.3-extra.patch
Patch6:		dhcpxd-glibc28_fix.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch2 -p1 -b .gcc3.3
%patch3 -p1 -b .64bit-fixes
%patch4 -p1 -b .varargs
%patch5 -p1 -b .extra
%patch6 -p0 -b .glibc28_fix

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
rm -rf %{buildroot}

mkdir -p %{buildroot}/sbin %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/dhcpxd

cp -f filter %{buildroot}%{_sysconfdir}/dhcpxd
cp -df install/* %{buildroot}%{_sysconfdir}/dhcpxd

ln -sf /dev/log %{buildroot}%{_sysconfdir}/dhcpxd/out

install -m 500 dhcpxd %{buildroot}/sbin/dhcpxd
install -m 644 dhcpxd.8 %{buildroot}%{_mandir}/man8/dhcpxd.8

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/dhcpxd
/sbin/dhcpxd
%{_mandir}/man8/dhcpxd.8*


