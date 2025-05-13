Name:           oscal-cli
Version:        1.0.3
Release:        1%{?dist}
Summary:        Command-line utility for processing OSCAL documents

License:        Apache-2.0
URL:            https://github.com/usnistgov/oscal-cli
Source0:        %{name}.tar.gz

BuildArch:      noarch
BuildRequires:  java-21-openjdk-devel
BuildRequires:  maven

Requires:       java-21-openjdk

%description
The OSCAL CLI tool enables command-line processing, transformation,
and validation of OSCAL (Open Security Controls Assessment Language) documents.
Supports formats like XML, JSON, and YAML, and works with SSPs, catalogs, profiles,
assessment plans, and more.

%prep
%setup -q -n cli-core-1.0.3-oscal-cli

%build
mvn clean install -Dgit.commit.id.skip=true

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
* Mon May 12 2025 Erik Cass <erik@go-palladium.com> - 1.0.3-1
- Initial RPM packaging of OSCAL CLI
