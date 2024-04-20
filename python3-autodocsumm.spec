Summary:	Extended Sphinx autodoc including automatic autosummaries
Summary(pl.UTF-8):	Rozszerzone autodoc dla Sphinksa wraz z automatycznymi podsumowaniami
Name:		python3-autodocsumm
Version:	0.2.12
Release:	1
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/autodocsumm/
Source0:	https://files.pythonhosted.org/packages/source/a/autodocsumm/autodocsumm-%{version}.tar.gz
# Source0-md5:	c6e84a11db27f1d82374ea4b278a3089
URL:		https://pypi.org/project/autodocsumm/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
BuildRequires:	python3-versioneer >= 0.26
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Sphinx extension provides some useful extensions to the Sphinx's
autodoc extension.

%description -l pl.UTF-8
To rozszerzenie Sphinksa dostarcza kilka przydatnych rozszerzeń do
rozszerzenia Sphinksa autodoc.

%prep
%setup -q -n autodocsumm-%{version}

%build
%py3_build

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
