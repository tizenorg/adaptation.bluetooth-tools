Name:       bluetooth-tools
Summary:    bluetooth-tools
Version:    0.2.45
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake

%description
Tools fo bluetooth run/stop

%prep
%setup -q

%build
export CFLAGS+=" -fpie -fvisibility=hidden"
export LDFLAGS+=" -Wl,--rpath=/usr/lib -Wl,--as-needed -Wl,--unresolved-symbols=ignore-in-shared-libs -pie"

%if "%{?tizen_profile_name}" == "wearable"
export CFLAGS="$CFLAGS -DTIZEN_WEARABLE"
%endif

%cmake \
%if "%{?tizen_profile_name}" == "wearable"
        -DTIZEN_WEARABLE=YES \
%elseif "%{?tizen_profile_name}" == "mobile"
        -DTIZEN_WEARABLE=NO \
%endif

cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc3.d
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc5.d

install -D -m 0644 LICENSE %{buildroot}%{_datadir}/license/bluetooth-tools

%files
%manifest bluetooth-tools.manifest
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
