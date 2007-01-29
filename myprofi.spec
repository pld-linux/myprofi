Summary:	MySQL log analyzer and profiler
Name:		myprofi
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/myprofi/MyProfi_%{version}beta.zip
# Source0-md5:	08ae769dec4a2ba513c7f0cb3ffc4ea1
URL:		http://myprofi.sourceforge.net/
BuildRequires:	sed >= 4.0
Requires:	php(pcre)
Requires:	php-common >= 4:5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL log analyzer and profiler. Extracts the most popular queries
grouping them by their normalized form and shows the statistics for
each group. Helps developers to recognize most frequently run queries
to be able to optimize overall db performance.

%prep
%setup -qc
%{__sed} -i -e '1i#!/usr/bin/php' parser.php
%{__sed} -i -e 's,php parser.php,%{name},g' parser.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install parser.php $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/myprofi
