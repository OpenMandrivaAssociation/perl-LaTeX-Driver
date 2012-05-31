%define	module	LaTeX-Driver
%define	modver	0.10

Name:		perl-%{module}
Version:	%perl_convert_version %{modver}
Release:	1

Summary:	Driver to run LaTeX, bibtex and makeindex
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/LaTeX/%{module}-%{modver}.tar.gz

BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File)
BuildRequires:	tetex-latex ghostscript-common
Requires:	tetex-latex ghostscript-common

BuildArch:	noarch

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
%setup -q -n %{module}-%{modver}

%build
yes | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
TMPDIR=/tmp %make test

%install
%makeinstall_std

%files
%doc README Changes
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*
