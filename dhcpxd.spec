Summary:	DHCPXD Daemon
Name:		dhcpxd
Version:	1.0.3
Release:	28
License:	GPL
Group:		System/Servers
Source:		ftp://ftp.guido.yi.org:50021/dhcpxd-%{version}.tar.bz2
Patch2:		dhcpxd-1.0.3-gcc-3.3.patch
Patch3:		dhcpxd-1.0.3-64bit-fixes.patch
Patch4:		dhcpxd-1.0.3-varargs.patch
Patch5:		dhcpxd-1.0.3-extra.patch
Patch6:		dhcpxd-glibc28_fix.diff

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
perl -pi -e 's/-Wall/\$(RPM_OPT_FLAGS) -Wall/g;' Makefile
%make RPM_OPT_FLAGS="%optflags"

%install
mkdir -p %{buildroot}/sbin %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/dhcpxd

cp -f filter %{buildroot}%{_sysconfdir}/dhcpxd
cp -df install/* %{buildroot}%{_sysconfdir}/dhcpxd

ln -sf /dev/log %{buildroot}%{_sysconfdir}/dhcpxd/out

install -m 700 dhcpxd %{buildroot}/sbin/dhcpxd
install -m 644 dhcpxd.8 %{buildroot}%{_mandir}/man8/dhcpxd.8

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/dhcpxd
%attr (0500,root,root) /sbin/dhcpxd
%{_mandir}/man8/dhcpxd.8*




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-27mdv2011.0
+ Revision: 663770
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-26mdv2011.0
+ Revision: 604787
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-25mdv2010.1
+ Revision: 521076
- bump release
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-23mdv2010.0
+ Revision: 413352
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.3-22mdv2009.1
+ Revision: 350778
- rebuild

* Wed Jul 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-21mdv2009.0
+ Revision: 230715
- added P6 to make it compile
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Apr 03 2008 Olivier Blin <oblin@mandriva.com> 1.0.3-19mdv2008.1
+ Revision: 192015
- remove update-resolvdrv patch, it is useless and the patch backup file breaks dhcpxd (#39427)

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-18mdv2008.1
+ Revision: 149174
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Mar 17 2007 Olivier Blin <oblin@mandriva.com> 1.0.3-17mdv2007.1
+ Revision: 145443
- fix build (remove extra qualification)
- Import dhcpxd

* Wed Aug 24 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.3-16mdk
- 64-bit & varargs fixes

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0.3-15mdk
- Rebuild

