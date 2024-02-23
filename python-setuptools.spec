# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-setuptools
Epoch: 100
Version: 72.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Download, build, install, upgrade, and uninstall Python packages
License: MIT
URL: https://github.com/pypa/setuptools/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: glibc-static
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-wheel

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages, especially ones that
have dependencies on other packages.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .
rm -rf _distutils_system_mod.py

%build
%py3_build
mkdir -p build/$(python3 -c "import sys; print('scripts-%d.%d' % sys.version_info[:2])")
python3 setup.py bdist_wheel

%install
ln -s setuptools/_distutils distutils
PYTHONPATH=. %py3_install
unlink distutils
%if 0%{?suse_version} > 1500
install -Dpm755 -d %{buildroot}%{python3_sitelib}/../wheels
install -Dpm644 -t %{buildroot}%{python3_sitelib}/../wheels dist/*.whl
%endif
%if 0%{?rhel} >= 7
install -Dpm755 -d %{buildroot}%{_datarootdir}/%{python3_version}-wheels
install -Dpm644 -t %{buildroot}%{_datarootdir}/%{python3_version}-wheels dist/*.whl
%endif
%if !(0%{?suse_version} > 1500) && !(0%{?rhel} >= 7)
install -Dpm755 -d %{buildroot}%{_datarootdir}/python-wheels
install -Dpm644 -t %{buildroot}%{_datarootdir}/python-wheels dist/*.whl
%endif
rm -rf %{buildroot}%{python3_sitelib}/pkg_resources/tests
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python_version_nodots}-setuptools
Summary: Download, build, install, upgrade, and uninstall Python packages
Requires: python3
Provides: python3-setuptools = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools) = %{epoch}:%{version}-%{release}

%description -n python%{python_version_nodots}-setuptools
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages, especially ones that
have dependencies on other packages.

%package -n python%{python_version_nodots}-setuptools-wheel
Summary: The setuptools wheel

%description -n python%{python_version_nodots}-setuptools-wheel
A Python wheel of setuptools to use with venv.

%files -n python%{python_version_nodots}-setuptools
%license LICENSE
%{python3_sitelib}/*

%files -n python%{python_version_nodots}-setuptools-wheel
%dir %{python3_sitelib}/../wheels
%{python3_sitelib}/../wheels/*.whl
%endif

%if 0%{?rhel} >= 7
%package -n platform-python-setuptools
Summary: Download, build, install, upgrade, and uninstall Python packages
Requires: python3
Conflicts: platform-python-setuptools < %{epoch}:%{version}-%{release}
Conflicts: python3-setuptools < %{epoch}:%{version}-%{release}

%description -n platform-python-setuptools
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages, especially ones that
have dependencies on other packages.

%package -n python3-setuptools
Summary: Download, build, install, upgrade, and uninstall Python packages
Requires: platform-python-setuptools = %{epoch}:%{version}-%{release}
Provides: python3-setuptools = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools) = %{epoch}:%{version}-%{release}

%description -n python3-setuptools
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages, especially ones that
have dependencies on other packages.

%package -n python3-setuptools-wheel
Summary: The setuptools wheel

%description -n python3-setuptools-wheel
A Python wheel of setuptools to use with venv.

%files -n platform-python-setuptools
%license LICENSE
%{python3_sitelib}/*

%files -n python3-setuptools
%license LICENSE

%files -n python3-setuptools-wheel
%dir %{_datarootdir}/%{python3_version}-wheels
%{_datarootdir}/%{python3_version}-wheels/*.whl
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} >= 7)
%package -n python3-setuptools
Summary: Download, build, install, upgrade, and uninstall Python packages
Requires: python3
Provides: python3-setuptools = %{epoch}:%{version}-%{release}
Provides: python3dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(setuptools) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-setuptools = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(setuptools) = %{epoch}:%{version}-%{release}

%description -n python3-setuptools
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages, especially ones that
have dependencies on other packages.

%package -n python-setuptools-wheel
Summary: The setuptools wheel

%description -n python-setuptools-wheel
A Python wheel of setuptools to use with venv.

%files -n python3-setuptools
%license LICENSE
%{python3_sitelib}/*

%files -n python-setuptools-wheel
%dir %{_datarootdir}/python-wheels
%{_datarootdir}/python-wheels/*.whl
%endif

%changelog
