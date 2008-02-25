%define module Glib

Summary: Perl module for the glib-2.x library
Name:    perl-%module
Version: 1.174
Release: %mkrel 1
License: GPL or Artistic
Group:   Development/GNOME and GTK+
# https://sourceforge.net/project/showfiles.php?group_id=64773&package_id=91217
Source:  http://prdownloads.sourceforge.net/gtk2-perl/%module-%version.tar.bz2
# BUG: we do not hanble exceptions out of Gtk2->main loop
# we should just horribly die in that case
Patch0: Glib-1.021-exception-trapping.patch
URL: http://gtk2-perl.sf.net/
BuildRequires: glib2-devel >= 2.6.0
BuildRequires: perl-devel
BuildRequires: perl-ExtUtils-Depends >= 0.202 perl-ExtUtils-PkgConfig
Conflicts: perl-Gtk2 <= 1
Requires: glib2 => 2.6.3
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%description doc
This package contains documentation of the Glib module.


%prep
%setup -q -n %module-%version
%patch0 -p0 -b .ex
find -type d -name CVS | rm -rf 


%build

perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
#%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%module/
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/%{module}/*.pm
%{perl_vendorarch}/%{module}/*/*.pm
%{perl_vendorarch}/%{module}/Install
%{perl_vendorarch}/auto/*

%files doc
%defattr(-, root, root)
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}/*.pod
%{perl_vendorarch}/%{module}/*/*.pod


