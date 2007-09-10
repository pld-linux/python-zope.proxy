Summary:	zope.proxy package used in Zope 3
Name:		Zope-Proxy
Version:	3.4.0
Release:	0.1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://download.zope.org/distribution/zope.proxy-%{version}.tar.gz
# Source0-md5:	a9e234e90bc4a16bb62b967d4a0412c6
URL:		http://pypi.python.org/pypi/zope.proxy/3.5.1
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zope.proxy package used in Zope 3.

%prep
%setup -q -n zope.proxy-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/zope/proxy
%{py_sitedir}/zope*egg*
%{py_sitedir}/zope*pth
