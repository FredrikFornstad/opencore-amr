%lib_package opencore-amrnb 0
%lib_package opencore-amrwb 0

Summary: Adaptive Multi-Rate Floating-point (AMR) Speech Codec
Name: opencore-amr
Version: 0.1.3
Release: 2%{?dist}
License: Distributable
Group: System Environment/Libraries
URL: http://opencore-amr.sourceforge.net
Source0: http://sourceforge.net/projects/opencore-amr/files/opencore-amr/opencore-amr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%lib_dependencies

%description
3GPP released reference implementations 3GPP Adaptive Multi-Rate
Floating-point (AMR) Speech Codec (3GPP TS 26.104 V 7.0.0) and 3GPP
AMR Adaptive Multi-Rate - Wideband (AMR-WB) Speech Codec (3GPP TS
26.204 V7.0.0).

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS ChangeLog NEWS

%changelog
* Fri May 1 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.3-2
- Corrected Source0 download path

* Sat Mar 17 2012 Paulo Roma <roma@lcg.ufrj.br> - 0.1.3-1
- Update to 0.1.3

* Sat Feb 14 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.1.2-1
- Initial build.

