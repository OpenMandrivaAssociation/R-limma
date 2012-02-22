%bcond_with bootstrap
%global packname  limma
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.10.2
Release:          2
Summary:          Linear Models for Microarray Data
Group:            Sciences/Mathematics
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/limma.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/limma_3.10.2.tar.gz
Requires:         R-methods R-affy R-MASS R-org.Hs.eg.db R-splines R-statmod
%if %{without bootstrap}
Requires:         R-vsn
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-affy R-MASS R-org.Hs.eg.db R-splines R-statmod
%if %{without bootstrap}
BuildRequires:    R-vsn
%endif

%description
Data analysis, linear models and differential expression for microarray

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
