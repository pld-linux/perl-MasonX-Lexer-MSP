#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Lexer-MSP
Summary:	MasonX::Lexer::MSP - give Mason a more ASP/JSP compatible syntax
Summary(pl):	MasonX::Lexer::MSP - nadanie Masonowi sk³adni bardziej kompatybilnej z ASP/JSP
Name:		perl-MasonX-Lexer-MSP
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22495b4a47997544bb249c22fcfa4631
BuildRequires:	perl-devel >= 1:5.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason >= 1.1
BuildRequires:	perl-Params-Validate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This lexer makes changes to the Mason syntax to make it closer to the
syntax used by ASP and JSP. These changes are incompatible with the
default Mason syntax, unfortunately.

%description -l pl
Ten lekser modyfikuje sk³adniê Masona, aby uczyniæ j± bli¿sz± sk³adni
u¿ywanej przez ASP czy JSP. Zmiany te s± niestety niekompatybilne z
domy¶ln± sk³adni± Masona.

%prep
%setup -q -n %{pdir}-%{pnam}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{_mandir}/man3/*
