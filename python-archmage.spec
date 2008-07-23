%define realname	archmage
%define name		python-%{realname}
%define version 0.1.9
%define release %mkrel 3

Summary: CHM(Compiled HTML) Decompressor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{realname}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRequires:	python-devel
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
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
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

# compressing manpages in bz2 changes the name
perl -pi -e "s#1.gz#1.bz2#g" INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
