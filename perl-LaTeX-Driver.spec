%define upstream_name    LaTeX-Driver
%define upstream_version 0.200.4

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Driver to run LaTeX, bibtex and makeindex

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LaTeX/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(File::pushd)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(Readonly)
BuildRequires:	tetex-latex
BuildRequires:	ghostscript-common
# Require whole set of texlive packages because it's hard
# to find what we really need to make tests pass
BuildRequires:	texlive
Requires:	tetex-latex
Requires:	ghostscript-common
Requires:	perl(Template)

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
yes | perl Makefile.PL INSTALLDIRS=vendor
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



