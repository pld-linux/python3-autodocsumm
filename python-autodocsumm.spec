#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Extended Sphinx autodoc including automatic autosummaries
Summary(pl.UTF-8):	Rozszerzone autodoc dla Sphinksa wraz z automatycznymi podsumowaniami
Name:		python-autodocsumm
# keep 0.1.x here for python2 support
Version:	0.1.13
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/autodocsumm/
Source0:	https://files.pythonhosted.org/packages/source/a/autodocsumm/autodocsumm-%{version}.tar.gz
# Source0-md5:	14154542b66b0a50a94d3c89ac023cb3
URL:		https://pypi.org/project/autodocsumm/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Sphinx extension provides some useful extensions to the Sphinx's
autodoc extension.

%description -l pl.UTF-8
To rozszerzenie Sphinksa dostarcza kilka przydatnych rozszerzeń do
rozszerzenia Sphinksa autodoc.

%package -n python3-autodocsumm
Summary:	Extended Sphinx autodoc including automatic autosummaries
Summary(pl.UTF-8):	Rozszerzone autodoc dla Sphinksa wraz z automatycznymi podsumowaniami
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-autodocsumm
This Sphinx extension provides some useful extensions to the Sphinx's
autodoc extension.

%description -n python3-autodocsumm -l pl.UTF-8
To rozszerzenie Sphinksa dostarcza kilka przydatnych rozszerzeń do
rozszerzenia Sphinksa autodoc.

%prep
%setup -q -n autodocsumm-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/autodocsumm
%{py_sitescriptdir}/autodocsumm-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-autodocsumm
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/autodocsumm
%{py3_sitescriptdir}/autodocsumm-%{version}-py*.egg-info
%endif
