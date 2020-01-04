Name:           lavg
Version:	0.1        
Release:        1%{?dist}
Summary:        Shows load average and the number of processors with coloring depending on the load.

License:        GPLv3+
URL:		https://github.com/maxstarkov/%{name}            
Source0:	https://github.com/maxstarkov/%{name}/releases/%{name}-%{version}.tar.gz        

BuildRequires:  python
Requires:       python
Requires:	bash

BuildArch:	noarch

%description
A simple python script that shows the average load and the number of processors with coloring depending on the load.

%prep
%setup -q

%build
python -m compileall lavg.py

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/usr/lib/%{name}

cat > %{buildroot}/%{_bindir}/%{name} <<-EOF
#!/bin/bash
/usr/bin/python /usr/lib/%{name}/%{name}.pyc
EOF

chmod 0755 %{buildroot}/%{_bindir}/%{name}

install -m 0644 %{name}.py* %{buildroot}/usr/lib/%{name}/

%files
%license LICENSE
%dir /usr/lib/%{name}/
%{_bindir}/%{name}
/usr/lib/%{name}/%{name}.py*
