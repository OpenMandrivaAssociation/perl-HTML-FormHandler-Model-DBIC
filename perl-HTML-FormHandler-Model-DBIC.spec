%define upstream_name    HTML-FormHandler-Model-DBIC
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Generate form classes from DBIC schema
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DBIx::Class::ResultSet::RecursiveUpdate)
BuildRequires: perl(DateTime::Format::MySQL)
BuildRequires: perl(DateTime::Format::SQLite)
BuildRequires: perl(DateTime::Format::W3CDTF)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::FormHandler)
BuildRequires: perl(Module::Find)
BuildRequires: perl(Moose)
BuildRequires: perl(SQL::Abstract)
BuildRequires: perl(Test::More)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Catalyst based application.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_bindir}/form_generator.pl
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/form_generator.pl

