#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Set
%define	pnam	String
Summary:	Set::String - Strings as objects with lots of handy methods
#Summary(pl):	
Name:		perl-Set-String
Version:	0.01
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Want >= 0.05
BuildRequires:	perl-Set-Array >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set::String allows you to create strings as objects and use OO-style
methods on them.  Many convenient methods are provided here that appear
in the FAQ's, the Perl Cookbook or posts from comp.lang.perl.misc.
In addition, there are Set methods with corresponding (overloaded)
operators for the purpose of Set comparison, i.e. B<+>, B<==>, etc.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
