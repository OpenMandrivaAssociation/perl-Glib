%define	modname	Glib
%define modver 1.305

Summary:	Perl module for the glib-2.x library

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPL+ or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
# https://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91217
Source0:	http://sourceforge.net/projects/gtk2-perl/files/%{modname}/%{modver}/%{modname}-%{modver}.tar.gz
Source1:	%{name}.rpmlintrc
# BUG:	we do not hanble exceptions out of Gtk2->main loop
# we should just horribly die in that case
Patch0:		Glib-1.280-exception-trapping.patch
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends) >= 0.300.0
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	pkgconfig(glib-2.0)
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
%setup -qn %{modname}-%{modver}
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

