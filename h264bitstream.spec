#
# spec file for package h264bitstream
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           h264bitstream
Version:        0.2.0
Release:        2.2
Summary:        Library for reading/writing of H.264 video
License:        LGPL-2.1
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            https://sourceforge.net/projects/h264bitstream/
Source0:        https://sourceforge.net/projects/h264bitstream/files/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libh264bitstream provides a complete set of functions to read and write video bitstreams
conforming to the ITU-T H.264 | ISO/IEC 14496-10 AVC video standard.

%package -n h264bitstream-devel
Summary:        Include files for h264bitstream
Group:          Development/Libraries/C and C++
BuildRequires:  libtool
BuildRequires:  pkgconfig
Requires:       h264bitstream = %{version}-%{release}
Obsoletes:      h264bitstream-devel < %{version}-%{release}
Provides:       h264bitstream-devel = %{version}-%{release}

%description -n h264bitstream-devel
This package provides the development header files for h264bitstream.

%prep
%setup -q
autoreconf -i

%build
%configure --prefix=%{_prefix} --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/*.la

%files -n h264bitstream-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/h264bitstream/*.h

%changelog
* Fri May 27 2022 ezequiel@vanguardiasur.com.ar
- Bump 0.2.0-2.2
- Package .la file
* Sun Feb 27 2022 ezequiel@vanguardiasur.com.ar
- Bump 0.2.0
* Fri Oct 21 2016 neutrino8@gmail.com
- Don't build static libs
* Fri Oct 21 2016 neutrino8@gmail.com
- Initial package
