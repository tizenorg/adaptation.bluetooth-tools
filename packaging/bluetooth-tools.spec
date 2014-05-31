Name:       bluetooth-tools
Summary:    bluetooth-tools
Version:    0.3.0
Release:    1
Group:      TO_BE/FILLED_IN
License:    Apache License, Version 2.0
Source0:    %{name}-%{version}.tar.gz
%if %{_repository}=="mobile"
Source1001:     bluetooth-address.service
%endif
BuildRequires:  cmake

%description
Tools fo bluetooth run/stop

%prep
%setup -q

%build
export CFLAGS+=" -fpie -fvisibility=hidden"
export LDFLAGS+=" -Wl,--rpath=/usr/lib -Wl,--as-needed -Wl,--unresolved-symbols=ignore-in-shared-libs -pie"

%if %{_repository}=="wearable"
cd wearable
%elseif %{_repository}=="mobile"
cd mobile
%endif

cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}

%if %{_repository}=="wearable"
cd wearable
%elseif %{_repository}=="mobile"
cd mobile
%endif

%make_install

mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc3.d
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc5.d

%if %{_repository}=="wearable"
install -D -m 0644 LICENSE.APLv2 %{buildroot}%{_datadir}/license/bluetooth-tools
%elseif %{_repository}=="mobile"
mkdir -p %{buildroot}%{_libdir}/systemd/system/multi-user.target.wants
install -m 0644 %{SOURCE1001} %{buildroot}%{_libdir}/systemd/system/
ln -s ../bluetooth-address.service %{buildroot}%{_libdir}/systemd/system/multi-user.target.wants/bluetooth-address.service
mkdir -p %{buildroot}/usr/share/license
cp LICENSE.APLv2 %{buildroot}/usr/share/license/%{name}
%endif

%files
%if %{_repository}=="wearable"
%defattr(-,root,root,-)
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-down.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-reset-env.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-dev-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-mode-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-off.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-hci-logdump.sh
%{_datadir}/license/bluetooth-tools
%elseif %{_repository}=="mobile"
%manifest mobile/bluetooth-tools.manifest
%defattr(-,root,root,-)
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-down.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-reset-env.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-dev-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-mode-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-off.sh
%{_libdir}/systemd/system/multi-user.target.wants/bluetooth-address.service
%{_libdir}/systemd/system/bluetooth-address.service
/usr/share/license/%{name}
%endif

