#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	MasonX
%define		pnam	Lexer-MSP
Summary:	MasonX::Lexer::MSP - give Mason a more ASP/JSP compatible syntax
Summary(pl.UTF-8):	MasonX::Lexer::MSP - nadanie Masonowi składni bardziej kompatybilnej z ASP/JSP
Name:		perl-MasonX-Lexer-MSP
Version:	0.11
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MasonX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5d2109e620addb5c53e78c6a3a5a07b8
URL:		http://search.cpan.org/dist/MasonX-Lexer-MSP/
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

%description -l pl.UTF-8
Ten lekser modyfikuje składnię Masona, aby uczynić ją bliższą składni
używanej przez ASP czy JSP. Zmiany te są niestety niekompatybilne z
domyślną składnią Masona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
%dir %{perl_vendorlib}/MasonX/Lexer
%{perl_vendorlib}/MasonX/Lexer/MSP.pm
%{_mandir}/man3/*
