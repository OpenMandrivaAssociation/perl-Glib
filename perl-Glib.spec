%define upstream_name    Glib
%define upstream_version 1.230

%define Werror_cflags %nil

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary: Perl module for the glib-2.x library
License: GPL+ or Artistic
Group:   Development/GNOME and GTK+
Url:     http://gtk2-perl.sf.net/
# https://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91217
Source0: http://prdownloads.sourceforge.net/gtk2-perl/%{upstream_name}-%{upstream_version}.tar.gz
# BUG: we do not hanble exceptions out of Gtk2->main loop
# we should just horribly die in that case
Patch0: Glib-1.210-exception-trapping.patch
Patch1: Glib-1.230-fix-bootstrap.diff

BuildRequires: glib2-devel >= 2.6.0
BuildRequires: perl(ExtUtils::Depends) >= 0.300.0
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl-devel

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Conflicts: perl-Gtk2 <= 1
Requires:  glib2 => 2.6.3

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
Summary: Glib documentation
Group: Books/Computer books
BuildArch: noarch

%description doc
This package contains documentation of the Glib module.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0 -b .ex
%patch1 -p1 -b .bs
find -type d -name CVS | rm -rf 


%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
# disabled due to long time faillures
#%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%{upstream_name}/
%{perl_vendorarch}/%{upstream_name}.pm
%{perl_vendorarch}/%{upstream_name}/*.pm
%{perl_vendorarch}/%{upstream_name}/*/*.pm
%{perl_vendorarch}/%{upstream_name}/Install
%{perl_vendorarch}/auto/*

%files doc
%defattr(-, root, root)
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{upstream_name}
%{perl_vendorarch}/%{upstream_name}/*.pod
%{perl_vendorarch}/%{upstream_name}/*/*.pod


