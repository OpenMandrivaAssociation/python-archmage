%define realname	archmage
%define debug_package %{nil}

Summary: CHM(Compiled HTML) Decompressor
Name:    python-%{realname}
Epoch:   1
Version: 0.4.0
Release: 1
Source0: https://files.pythonhosted.org/packages/99/3f/df684120dbe7c5a1c0ec8201c51d9e8424c570f019ed7c0f5a6ea418ebff/archmage-%{version}.tar.gz
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
