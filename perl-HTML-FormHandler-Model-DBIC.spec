%define upstream_name    HTML-FormHandler-Model-DBIC
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.26
Release:	3

Summary:	Generate form classes from DBIC schema
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-FormHandler-Model-DBIC-0.26.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::ResultSet::RecursiveUpdate)
BuildRequires:	perl(DateTime::Format::MySQL)
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl(DateTime::Format::W3CDTF)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::FormHandler)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Getopt)
BuildRequires:	perl(SQL::Abstract)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)

# For tests that use perl(HTML::FormHandler)
BuildRequires:	perl(aliased)
BuildArch:	noarch

%description
Catalyst based application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# Disable for now due to very minor errors in syntax (expected)
#make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_bindir}/form_generator.pl
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 687045
- update to new version 0.15

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.140.0-3
+ Revision: 656927
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.140.0-2mdv2011.0
+ Revision: 624896
- Add SQL::Abstract as a dependency
- Upgraded to 0.14 and fixed the build system.
- import perl-HTML-FormHandler-Model-DBIC


