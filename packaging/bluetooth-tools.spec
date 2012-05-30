Name:       bluetooth-tools
Summary:    bluetooth-tools
Version:    0.1.0
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/bluetooth-tools.manifest 
BuildRequires:  cmake

%description
Tools fo bluetooth run/stop and set address


%prep
%setup -q

%build
cp %{SOURCE1001} .
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc3.d
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/rc5.d
ln -s %{_sysconfdir}/rc.d/init.d/bluetooth-address %{buildroot}%{_sysconfdir}/rc.d/rc3.d/S60bluetooth-address
ln -s %{_sysconfidr}/rc.d/init.d/bluetooth-address %{buildroot}%{_sysconfdir}/rc.d/rc5.d/S60bluetooth-address


%files
%manifest bluetooth-tools.manifest
%defattr(-,root,root,-)
%{_sysconfdir}/rc.d/init.d/bluetooth-address
%{_sysconfdir}/rc.d/rc3.d/S60bluetooth-address
%{_sysconfdir}/rc.d/rc5.d/S60bluetooth-address
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-stack-down.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-reset-env.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-dev-up.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-mode-on.sh
%attr(0755,-,-) %{_prefix}/etc/bluetooth/bt-edutm-off.sh
