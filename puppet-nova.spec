%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-nova
Version:        17.6.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for OpenStack Nova
License:        ASL 2.0

URL:            https://launchpad.net/puppet-nova

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

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
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%setup -q -n openstack-nova-%{upstream_version}

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
* Mon Feb 08 2021 RDO <dev@lists.rdoproject.org> 17.6.0-1
- Update to 17.6.0

* Tue Oct 20 2020 Joel Capitao <jcapitao@redhat.com> 17.5.0-2
- Enable sources tarball validation using GPG signature.

* Thu Oct 08 2020 RDO <dev@lists.rdoproject.org> 17.5.0-1
- Update to 17.5.0

* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-4.0618e74git
- Set upstream_version based on commit

* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-3.0618e74git
- Update to post 17.4.0 (0618e74260e4d45ed167800bdee370b531a8c62a)

* Mon Oct 05 2020 Joel Capitao <jcapitao@redhat.com> 17.4.0-2.e2daa4egit
- Update to post 17.4.0 (e2daa4e2c83d061b496ebea6a373fa40ba6d48ab)

* Tue Sep 29 2020 RDO <dev@lists.rdoproject.org> 17.4.0-1
- Update to 17.4.0


