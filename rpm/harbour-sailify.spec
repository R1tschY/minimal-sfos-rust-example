Name:       minimal-rust-example
Summary:    Minimal Rust example
Version:    0.1
Release:    0
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  rust
BuildRequires:  cargo


%description
Just a minimal example to compile a Rust binary in Sailfish OS.

# - PREP -----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}

# - BUILD ----------------------------------------------------------------------
%build

export CARGO_INCREMENTAL=0
cargo build --release --target-dir=target --manifest-path %{_sourcedir}/../Cargo.toml

# - INSTALL --------------------------------------------------------------------
%install

rm -rf %{buildroot}

install -Dm 755 target/release/%{name} -t %{buildroot}%{_bindir}

# - FILES ----------------------------------------------------------------------
%files

%defattr(-,root,root,-)
%{_bindir}


