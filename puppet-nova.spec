%{!?upstream_version: %global upstream_version %{commit}}
%if 0%{?dlrn}
%define upstream_name openstack-nova
%else
%define upstream_name puppet-nova
%endif
%global commit 0618e74260e4d45ed167800bdee370b531a8c62a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-nova
Version:        17.4.0
Release:        4%{?alphatag}%{?dist}
Summary:        Puppet module for OpenStack Nova
License:        ASL 2.0

URL:            https://launchpad.net/puppet-nova

Source0:        https://github.com/openstack/%{name}/archive/%{commit}.tar.gz

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
* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-4.0618e74git
- Set upstream_version based on commit

* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-3.0618e74git
- Update to post 17.4.0 (0618e74260e4d45ed167800bdee370b531a8c62a)

* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-2.e2daa4egit
- Update to post 17.4.0 (e2daa4e2c83d061b496ebea6a373fa40ba6d48ab)

* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 17.4.0-1
- Update to 17.4.0


