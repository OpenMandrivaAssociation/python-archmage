%define realname	archmage
%define name		python-%{realname}
%define version 0.2.4
%define release %mkrel 2

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


%changelog
* Fri Nov 19 2010 Funda Wang <fwang@mandriva.org> 1:0.2.4-2mdv2011.0
+ Revision: 598915
- rebuild for py2.7

* Wed Aug 05 2009 Frederik Himpe <fhimpe@mandriva.org> 1:0.2.4-1mdv2010.0
+ Revision: 410341
- update to new version 0.2.4

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 1:0.1.9-3mdv2009.1
+ Revision: 323538
- add epoch
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Stefan van der Eijk <stefan@mandriva.org>
    - 0.1.9

* Sun Jun 17 2007 Stefan van der Eijk <stefan@mandriva.org> 0.1.9beta1-1mdv2008.0
+ Revision: 40517
- 0.1.9beta1


* Thu Jan 18 2007 Stefan van der Eijk <stefan@mandriva.org> 0.0.8-1mdv2007.0
+ Revision: 110420
- 0.0.8

* Wed Jan 03 2007 Stefan van der Eijk <stefan@mandriva.org> 0.0.7-1mdv2007.1
+ Revision: 103843
- Import python-archmage

* Wed Mar 08 2006 Stefan van der Eijk <stefan@eijk.nu> 0.0.7-1mdk
- 0.0.7

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.0.6-3mdk
- Rebuild
- %%mkrel

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.0.6-2mdk
- Rebuild for new python

* Sun May 02 2004 Stefan van der Eijk <stefan@mandrake.org> 0.0.6-1mdk
- initial MDK package

