Name:           oscal-cli
Version:        1.0.3
Release:        1%{?dist}
Summary:        Command-line utility for processing OSCAL documents

License:        CC0
URL:            https://github.com/usnistgov/oscal-cli
Source0:        %{name}.tar.gz

BuildArch:      noarch
BuildRequires:  maven
BuildRequires:  java-11-openjdk-devel

Requires:       java-11-openjdk

%description
The OSCAL CLI tool enables command-line processing, transformation,
and validation of OSCAL (Open Security Controls Assessment Language) documents.
Supports formats like XML, JSON, and YAML, and works with SSPs, catalogs, profiles,
assessment plans, and more.

%prep
%setup -q

%build
mvn clean install

%install
mkdir -p %{buildroot}/opt/%{name}
cp -r target/cli-core-%{version}-oscal-cli/* %{buildroot}/opt/%{name}/

# Symlink the CLI to /usr/bin
mkdir -p %{buildroot}/usr/bin
ln -s /opt/%{name}/bin/oscal-cli %{buildroot}/usr/bin/oscal-cli

%files
%license LICENSE
%doc README.md
/opt/%{name}
/usr/bin/oscal-cli

%changelog
* Tue May 14 2025 Erik Cass <erik@go-palladium.com> - 1.0.3-1
- Initial RPM packaging of OSCAL CLI
