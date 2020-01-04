Name:       harbour-themepack-vaidroid

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    harbour-themepack-vaidroid
Version:    2.7
Release:    1
Group:      System/Tools
Vendor:     molan
License:    GPLv3
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qmake
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   sailfish-version >= 2.0.1
Requires:   harbour-themepacksupport >= 0.8.8-1

%description
VaiDroid icon pack for Sailfish OS.

%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake5
%qtc_make %{?_smp_mflags}

%posttrans
# >> posttrans
mv /usr/share/harbour-themepack-vaidroid/theme/* /usr/share/harbour-themepack-vaidroid/
rm -r mv /usr/share/harbour-themepack-vaidroid/theme/
# << posttrans

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_datadir}/harbour-themepack-vaidroid/*
%{_datadir}/harbour-themepack-vaidroid/apk/192x192/*
%{_datadir}/harbour-themepack-vaidroid/overlay/*
%{_datadir}/harbour-themepack-vaidroid/theme/*


%post
systemctl-user restart maliit-server.service
