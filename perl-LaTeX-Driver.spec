%define realname   LaTeX-Driver
%define version    0.08
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Driver to run LaTeX, bibtex and makeindex
Source:     http://www.cpan.org/modules/by-module/LaTeX/%{realname}-%{version}.tar.gz
Patch:      LaTeX-Driver.test.patch
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Cwd)
BuildRequires: perl(Exception::Class)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)

BuildArch: noarch

%description
The LaTeX::Driver module encapsulates the details of invoking the Latex
programs to format a LaTeX document. Formatting with LaTeX is complicated;
there are potentially many programs to run and the output of those programs
must be monitored to determine whether further processing is required.

This module runs the required commands in the directory specified, either
explicitly with the 'dirname' option or implicitly by the directory part of
'basename', or in the current directory. As a result of the processing up
to a dozen or more intermediate files are created. These can be removed
with the 'cleanup' method.



%prep
%setup -q -n %{realname}-%{version} 
%patch -b .fixtest

%build
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README README README Changes
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*

