%define realname	archmage
%define debug_package %{nil}

Summary: CHM(Compiled HTML) Decompressor
Name:    python-%{realname}
Epoch:   1
Version: 0.2.4
Release: 4
Source0: %{realname}-%{version}.tar.bz2
License: GPL
Group:   Development/Python
Url:     http://archmage.sf.net/
BuildRequires:	python-devel

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
%config %{_sysconfdir}/archmage/arch.conf
%{_bindir}/*
%{python_sitelib}/*.egg-info
%{python_sitelib}/archmod
%{_datadir}/archmage
%{_mandir}/man1/*
