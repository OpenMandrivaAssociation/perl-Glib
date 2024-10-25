%define modname Glib
%define modver 1.3293
%define _disable_rebuild_configure 1

Summary:	Perl module for the glib-2.x library
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		https://gtk2-perl.sf.net/
# https://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91217
Source0:	http://sourceforge.net/projects/gtk2-perl/files/%{modname}/%{modver}/%{modname}-%{modver}.tar.gz
Source1:	%{name}.rpmlintrc
# BUG:	we do not hanble exceptions out of Gtk2->main loop
# we should just horribly die in that case
Patch0:		Glib-1.280-exception-trapping.patch

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::More)
BuildRequires:	pkgconfig(glib-2.0)
Obsoletes:	perl-Glib-doc < 1.327
Conflicts:	perl-Gtk2 <= 1

# Do not export private modules and libraries
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(MY\\)

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

%prep
%autosetup -p1 -n %{modname}-%{modver}

# disable build dependency on perl-podlators
sed -i- '/MAN3PODS/d' Makefile.PL

%build
# fix build with modules from ./lib/:
export PERL_USE_UNSAFE_INC=1
%__perl -I ./lib/ Makefile.PL INSTALLDIRS=vendor
%define _disable_ld_no_undefined 1
%make_build OPTIMIZE="%{optflags}" OTHERLDFLAGS="%{build_ldflags}" PERL_ARCHIVE_AFTER="-lpthread -ldl"

%install
%make_install

# (tpg) get rid of docs
rm -rf %{buildroot}%{perl_vendorarch}/%{modname}/*.pod
rm -rf %{buildroot}%{_mandir}/man3

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

