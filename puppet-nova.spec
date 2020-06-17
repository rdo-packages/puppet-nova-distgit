%{!?upstream_version: %global upstream_version %{commit}}
%global commit 655027005c95b4146ab4e6cb5a70290a9e6881db
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

%if 0%{?dlrn}
%define upstream_name openstack-nova
%else
%define upstream_name puppet-nova
%endif

Name:           puppet-nova
Version:        15.6.0
Release:        0.1%{?alphatag}%{?dist}
Summary:        Puppet module for OpenStack Nova
License:        ASL 2.0

URL:            https://launchpad.net/puppet-nova

Source0:        https://github.com/openstack/%{name}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

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
* Wed Jun 17 2020 Alfredo Moralejo <amoralej@redhat.com> - 15.6.0-0.1.6550270git
- Update to 15.6.0 (commit 655027005c95b4146ab4e6cb5a70290a9e6881db)

* Wed Apr 15 2020 RDO <dev@lists.rdoproject.org> 15.5.0-1
- Update to 15.5.0

* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0

