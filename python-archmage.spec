%define realname	archmage
%define name		python-%{realname}
%define version 0.1.9
%define release %mkrel 3

Summary: CHM(Compiled HTML) Decompressor
Name: %{name}
Epoch: 1
Version: %{version}
Release: %{release}
Source0: %{realname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRequires:	python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Url: http://archmage.sf.net/

%description
arCHMage - extensible reader/decompiler of files in CHM format 
(Microsoft HTML help, also known as Compiled HTML).
arCHMage is based on chmlib by Jed Wing and is written in python 

%prep
%setup -q -n %{realname}-%{version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config %{_sysconfdir}/archmage/arch.conf
%{_bindir}/*
%{python_sitelib}/*.egg-info
%{python_sitelib}/archmod
%{_datadir}/archmage
%{_mandir}/man1/*
