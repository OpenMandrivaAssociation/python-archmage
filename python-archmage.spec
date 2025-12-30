%define realname	archmage
%define debug_package %{nil}

Summary: CHM(Compiled HTML) Decompressor
Name:    python-%{realname}
Epoch:   1
Version: 0.4.2.1
Release: 3
Source0: https://files.pythonhosted.org/packages/source/a/archmage/archmage-%{version}.tar.gz
License: GPL
Group:   Development/Python
Url:     https://github.com/dottedmag/archmage
BuildRequires:	python-devel
BuildRequires:  python3dist(setuptools)

%description
arCHMage - extensible reader/decompiler of files in CHM format 
(Microsoft HTML help, also known as Compiled HTML).
arCHMage is based on chmlib by Jed Wing and is written in python 

%prep
%setup -q -n %{realname}-%{version}

%build
env CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{_bindir}/*
%{python_sitelib}/*.egg-info
%{python3_sitelib}/archmage/
