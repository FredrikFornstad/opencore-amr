%global libver 0.0.3

Summary: Adaptive Multi-Rate Floating-point (AMR) Speech Codec
Name: opencore-amr
Version: 0.1.5
Release: 1%{?dist}
License: Distributable
Group: System Environment/Libraries
URL: http://opencore-amr.sourceforge.net
Source0: http://sourceforge.net/projects/opencore-amr/files/opencore-amr/opencore-amr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
Requires: %{name}-libs_nb_%{libver}, %{name}-libs_wb_%{libver}

%description
3GPP released reference implementations 3GPP Adaptive Multi-Rate
Floating-point (AMR) Speech Codec (3GPP TS 26.104 V 7.0.0) and 3GPP
AMR Adaptive Multi-Rate - Wideband (AMR-WB) Speech Codec (3GPP TS
26.204 V7.0.0).

%package libs_nb_%{libver}
Summary: Opencore-amr-nb codec shared library
Group: Development/Libraries
Obsoletes: libopencore-amrnb*

%description libs_nb_%{libver}
This package contain the opencore-amr-nb shared library.

%package libs_wb_%{libver}
Summary: Opencore-amr-wb codec shared library
Group: Development/Libraries
Obsoletes: libopencore-amrwb*

%description libs_wb_%{libver}
This package contain the opencore-amr-wb shared library.

%package devel
Summary: Opencore-amr codec development files
Group: Development/Libraries
Requires: %{name}-libs_nb_%{libver}, %{name}-libs_wb_%{libver}

%description devel
This package contains the opencore-amr codec development files

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE ChangeLog README

%files libs_nb_%{libver}
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrnb.so.%{libver}

%files libs_wb_%{libver}
%defattr(-,root,root,-)
%{_libdir}/libopencore-amrwb.so.%{libver}

%files devel
%defattr(-,root,root,-)
%{_includedir}/opencore-amrnb/*.h
%{_includedir}/opencore-amrwb/*.h
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/*.la
%{_libdir}/pkgconfig/*

%changelog
* Tue Apr 4 2017 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.5-1
- Updated upstream
- Adjusted post and postun scripts
- Adjusted doc files according to upstream package

* Sat Jun 13 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.3-4
- Removed dependency on atrpms scripts to comply with ClearOS policy

* Wed May 6 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.3-3
- Added buildrequirement atrpms-rpm-config

* Fri May 1 2015 Fredrik Fornstad <fredrik.fornstad@gmail.com> - 0.1.3-2
- Corrected Source0 download path

* Sat Mar 17 2012 Paulo Roma <roma@lcg.ufrj.br> - 0.1.3-1
- Update to 0.1.3

* Sat Feb 14 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 0.1.2-1
- Initial build.

