%{!?upstream_version: %global upstream_version %{version}}

%if 0%{?dlrn}
%define upstream_name openstack-nova
%else
%define upstream_name puppet-nova
%endif

Name:           puppet-nova
Version:        16.5.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for OpenStack Nova
License:        ASL 2.0

URL:            https://launchpad.net/puppet-nova

Source0:        https://github.com/openstack/%{name}/archive/%{version}.tar.gz#/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-cinder
Requires:       puppet-glance
Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-rabbitmq
Requires:       puppet-stdlib
Requires:       puppet-sysctl
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Nova

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/
rm -f %{buildroot}/%{_datadir}/openstack-puppet/modules/nova/files/nova-novncproxy.init

%files
%{_datadir}/openstack-puppet/modules/nova/


%changelog
* Thu Feb 11 2021 RDO <dev@lists.rdoproject.org> 16.5.0-1.0d7f13fgit
- Update to 16.5.0

* Wed Jun 17 2020 Alfredo Moralejo <amoralej@redhat.com> - 16.4.0-0.1.0d7f13fgit
- Update to 16.4.0 (commit 0d7f13ff9b60952cd19fee0ce40bf5ea007f2137)

* Wed May 06 2020 RDO <dev@lists.rdoproject.org> 16.3.0-1
- Update to 16.3.0


