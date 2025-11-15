#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (some files missing in sdist?)

Summary:	Extended Sphinx autodoc including automatic autosummaries
Summary(pl.UTF-8):	Rozszerzone autodoc dla Sphinksa wraz z automatycznymi podsumowaniami
Name:		python3-autodocsumm
Version:	0.2.14
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/autodocsumm/
Source0:	https://files.pythonhosted.org/packages/source/a/autodocsumm/autodocsumm-%{version}.tar.gz
# Source0-md5:	10ac01d944bf1a66684813e9fc869e83
URL:		https://pypi.org/project/autodocsumm/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:61.0
BuildRequires:	python3-versioneer >= 0.26
%if %{with tests}
BuildRequires:	python3-Sphinx >= 4.0
BuildRequires:	python3-packaging
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	python3-bs4
BuildRequires:	sphinx-pdg-3 >= 4.0
%endif
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Sphinx extension provides some useful extensions to the Sphinx's
autodoc extension.

%description -l pl.UTF-8
To rozszerzenie Sphinksa dostarcza kilka przydatnych rozszerzeń do
rozszerzenia Sphinksa autodoc.

%package apidocs
Summary:	API documentation for Python autodocsumm module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona autodocsumm
Group:		Documentation

%description apidocs
API documentation for Python autodocsumm module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona autodocsumm.

%prep
%setup -q -n autodocsumm-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/autodocsumm
%{py3_sitescriptdir}/autodocsumm-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,api,*.html,*.js}
%endif
