%global goipath         github.com/pebbe/zmq4
Version:                1.0.0

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go interface to ZeroMQ version 4
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: zeromq-devel >= 4.0.1
Requires:      zeromq-devel >= 4.0.1

%description devel
%{summary}

This package contains library source intended for building other packages which
use import path with %{goipath} prefix.


%prep
%gosetup -q


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE.txt
%doc README.md


%changelog
* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to tagged version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git5b443b6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.20180610git5b443b6
- Add explicit zeromq Req

* Sun Jun 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180610git5b443b6
- First package for Fedora
