%define	modname	Glib
%define	modver	1.290

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1

Summary:	Perl module for the glib-2.x library
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# https://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91217
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{modver}.tar.gz
# BUG: we do not hanble exceptions out of Gtk2->main loop
# we should just horribly die in that case
Patch0:		Glib-1.280-exception-trapping.patch

BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl-devel

Conflicts:	perl-Gtk2 <= 1

%description
This module provides perl access to Glib and GLib's GObject libraries.
It is mainly used by perl-GTK2 applications.

Glib is a handy library of portability and utility functions. This C library
is designed to solve some portability problems and provide other useful
functionality which most programs require.

GObject provides a generic type system with inheritance and a powerful signal
system.

Together these libraries are used as the foundation for many of the libraries
that make up the Gnome environment, and are used in many unrelated
projects.

%package doc
Summary:	Glib documentation
Group:		Books/Computer books
Obsoletes:	%{name}-doc < 1.230.0-9

%description	doc
This package contains documentation of the Glib module.

%prep
%setup -q -n %{modname}-%{modver}
%patch0 -p0 -b .ex~

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# disabled due to long time faillures
#%make test

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%{modname}/
%{perl_vendorarch}/%{modname}.pm
%{perl_vendorarch}/%{modname}/*.pm
%dir %{perl_vendorarch}/%{modname}/Install
%{perl_vendorarch}/%{modname}/Install/Files.pm
%{perl_vendorarch}/%{modname}/Install/doctypes
%{perl_vendorarch}/%{modname}/Install/gperl.h
%{perl_vendorarch}/%{modname}/Install/gperl_marshal.h
%{perl_vendorarch}/%{modname}/Install/typemap
%dir %{perl_vendorarch}/%{modname}/Object
%{perl_vendorarch}/%{modname}/Object/Subclass.pm
%{perl_vendorarch}/auto/*

%files doc
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}/*.pod
%dir %{perl_vendorarch}/%{modname}/Param
%{perl_vendorarch}/%{modname}/Param/*.pod

%changelog
* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.241.0-4
- rebuild for perl-5.16.2
- fix unpackaged directories
- cleanups

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.241.0-1
+ Revision: 765382
- 1.241
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

  + Zé <ze@mandriva.org>
    - 1.241
    - own missing dirs
    - rpm isnt able to handle = i conflicts
    - fix file list

* Fri Dec 02 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.233.0-2
+ Revision: 737308
- rebuild
- removed dup requires
- cleaned up spec
- removed mkrel, BuildRoot, clean section & defatrr

* Tue Oct 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.233.0-1
+ Revision: 702791
- 1.233

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.230.0-9
+ Revision: 657344
- doc is not a non-arch package

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.230.0-8
+ Revision: 653885
- rebuild

* Tue Aug 31 2010 Thierry Vignaud <tv@mandriva.org> 1.230.0-7mdv2011.0
+ Revision: 574925
- let the doc subpackage be noarch

* Wed Aug 04 2010 Thierry Vignaud <tv@mandriva.org> 1.230.0-6mdv2011.0
+ Revision: 565899
- patch 1: fix build without perl-GLib

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.230.0-5mdv2011.0
+ Revision: 564475
- rebuild for perl 5.12.1

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-4mdv2011.0
+ Revision: 556325
- do not require pkg perl-Glib during its own build!
- rebuild for perl 5.12

  + Thierry Vignaud <tv@mandriva.org>
    - temporary BuildRequires perl-Glib in order to fix build
    - new release

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.223.0-1mdv2011.0
+ Revision: 553129
- update to 1.223

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.222-1mdv2010.1
+ Revision: 392986
- update to new version 1.222

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.221-1mdv2010.0
+ Revision: 370126
- update to new version 1.221

* Wed Mar 18 2009 Thierry Vignaud <tv@mandriva.org> 1.220-1mdv2009.1
+ Revision: 357186
- new release (no change, just tagged as stable)

* Wed Mar 11 2009 Thierry Vignaud <tv@mandriva.org> 1.214-1mdv2009.1
+ Revision: 353612
- new release

* Mon Feb 16 2009 Thierry Vignaud <tv@mandriva.org> 1.213-1mdv2009.1
+ Revision: 340886
- new release

* Sun Feb 08 2009 Thierry Vignaud <tv@mandriva.org> 1.212-1mdv2009.1
+ Revision: 338629
- new release

* Fri Jan 16 2009 Thierry Vignaud <tv@mandriva.org> 1.211-1mdv2009.1
+ Revision: 330286
- temporary disable Werror_cflags
- rediff patches for new rpm
- new release
- new release

* Sat Sep 20 2008 Thierry Vignaud <tv@mandriva.org> 1.200-1mdv2009.0
+ Revision: 286092
- new release (no changes, just tagged as stable)

* Mon Sep 08 2008 Thierry Vignaud <tv@mandriva.org> 1.193-1mdv2009.0
+ Revision: 282631
- new release
- new release
- new release

* Sat Jul 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.190-1mdv2009.0
+ Revision: 231999
- update to new version 1.190

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.183-1mdv2009.0
+ Revision: 214512
- update to new version 1.183

* Tue Apr 15 2008 Thierry Vignaud <tv@mandriva.org> 1.182-2mdv2009.0
+ Revision: 194017
- bump require on ExtUtils::Depends
- new release

* Mon Mar 10 2008 Thierry Vignaud <tv@mandriva.org> 1.180-1mdv2008.1
+ Revision: 183823
- new release

* Tue Feb 26 2008 Thierry Vignaud <tv@mandriva.org> 1.174-1mdv2008.1
+ Revision: 175186
- new release

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.173-1mdv2008.1
+ Revision: 166533
- new release

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.172-2mdv2008.1
+ Revision: 151254
- rebuild for perl-5.10.0

* Thu Jan 10 2008 Thierry Vignaud <tv@mandriva.org> 1.172-1mdv2008.1
+ Revision: 147562
- new release (perl 5.10.0 ready)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1.171-1mdv2008.1
+ Revision: 132391
- new release
- kill re-definition of %%buildroot on Pixel's request

* Wed Oct 31 2007 Thierry Vignaud <tv@mandriva.org> 1.170-1mdv2008.1
+ Revision: 104186
- new release

* Mon Oct 15 2007 Thierry Vignaud <tv@mandriva.org> 1.161-1mdv2008.1
+ Revision: 98586
- new release

* Tue Sep 25 2007 Thierry Vignaud <tv@mandriva.org> 1.160-1mdv2008.0
+ Revision: 92702
- new release (no change, just tagged as stable)

* Mon Aug 13 2007 Thierry Vignaud <tv@mandriva.org> 1.153-1mdv2008.0
+ Revision: 62751
- new release

* Mon Jul 30 2007 Thierry Vignaud <tv@mandriva.org> 1.152-1mdv2008.0
+ Revision: 56551
- new release

* Mon Jun 25 2007 Thierry Vignaud <tv@mandriva.org> 1.151-1mdv2008.0
+ Revision: 44012
- new release


* Tue Mar 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.144-2mdv2007.1
+ Revision: 146880
- split out doc

* Tue Feb 27 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.144-1mdv2007.1
+ Revision: 126590
- new release

* Mon Feb 19 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.143-1mdv2007.1
+ Revision: 122773
- new release

* Tue Dec 05 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.142-1mdv2007.1
+ Revision: 91066
- new release

* Thu Nov 23 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.141-1mdv2007.1
+ Revision: 86820
- Import perl-Glib

* Thu Nov 23 2006 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.141-1mdv2007.1
- new release

* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.140-1mdv2007.0
- new release

* Fri Aug 11 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.132-1mdv2007.0
- new release

* Wed Jul 26 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.131-1mdv2007.0
- new release

* Thu Mar 16 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.120-1mdk
- new release

* Wed Mar 01 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.117-1mdk
- new release

* Tue Feb 14 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.116-1mdk
- new release

* Tue Jan 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.115-1mdk
- new release

* Tue Jan 17 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.114-1mdk
- new release
- drop patch 0 (merged upstream)

* Wed Jan 11 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.113-2mdk
- Patch1: avoid nasty pointer to int cast on x86_64

* Tue Jan 03 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.113-1mdk
- new release

* Tue Nov 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.111-1mdk
- new release

* Thu Oct 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.101-1mdk
- New release 1.101

* Sun Oct 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 1.100-1mdk
- new release

* Fri Jun 24 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.082-1mdk
- new release

* Sat Apr 16 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.081-1mdk
- new release

* Tue Mar 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.080-1mdk
- new stable release

* Tue Mar 01 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.074-1mdk
- new release

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.073-1mdk
- new release

* Mon Jan 10 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.072-1mdk
- new release

* Thu Dec 16 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.071-2mdk
- rebuild for new glib

* Tue Nov 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.071-1mdk
- new release

* Fri Nov 12 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.070-2mdk
- Rebuild for new perl

* Wed Nov 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.070-1mdk
- new release

* Tue Aug 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.054-1mdk
- new release

* Tue Aug 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.053-1mdk
- new release

* Tue Jul 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.052-1mdk
- new release

* Wed Jun 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.051-1mdk
- new release

* Fri Jun 04 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.050-1mdk
- new release

* Thu May 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.042-2mdk
- bump requires

* Wed Apr 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.042-1mdk
- new release

* Sat Apr 10 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.041-1mdk
- new release

* Sat Apr 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.040-2mdk
- link with glib-2.4.x

* Wed Mar 24 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.040-1mdk
- new release

