%global debug_package %{nil}

Name: python-setuptools
Epoch: 100
Version: 60.9.2
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

%install
%py3_install
rm -rf %{buildroot}%{python3_sitelib}/pkg_resources/tests
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

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

%files -n python%{python_version_nodots}-setuptools
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?centos_version} == 800
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

%files -n platform-python-setuptools
%license LICENSE
%{python3_sitelib}/*

%files -n python3-setuptools
%license LICENSE
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?centos_version} == 800)
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

%files -n python3-setuptools
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
