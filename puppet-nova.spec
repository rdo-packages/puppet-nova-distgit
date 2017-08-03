%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-nova
Version:        9.6.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Nova
License:        Apache-2.0

URL:            https://launchpad.net/puppet-nova

Source0:        https://github.com/openstack/%{name}/archive/%{upstream_version}.tar.gz

Patch0001: 0001-Test-change-DO-NOT-MERGE.patch

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
%setup -q -n puppet-nova-%{upstream_version}

%patch0001 -p1

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
* Thu Aug 03 2017 rdo-trunk <javier.pena@redhat.com> 9.6.0-1
- Update to 9.6.0

* Thu Jun 01 2017 rdo-trunk <javier.pena@redhat.com> 9.5.4-1
- Update to 9.5.4

* Tue May 30 2017 rdo-trunk <javier.pena@redhat.com> 9.5.2-1
- Update to 9.5.2

* Mon May 22 2017 rdo-trunk <javier.pena@redhat.com> 9.5.1-1
- Update to 9.5.1

* Thu Feb 02 2017 Alfredo Moralejo <amoralej@redhat.com> 9.5.0-1
- Update to 9.5.0

* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0

