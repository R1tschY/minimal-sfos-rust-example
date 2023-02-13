Name:       minimal-rust-example
Summary:    Minimal Rust example
Version:    0.1
Release:    0
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  rust
BuildRequires:  cargo


%description
Just a minimal example to (cross-)compile a Rust binary in Sailfish OS.


%define BUILD_DIR "$PWD"/target

# - PREP -----------------------------------------------------------------------
%prep
%setup -q -n %{name}-%{version}
mkdir -p "%{BUILD_DIR}"

%ifarch %arm32
%define SB2_TARGET armv7-unknown-linux-gnueabihf
%endif
%ifarch %arm64
%define SB2_TARGET aarch64-unknown-linux-gnu
%endif
%ifarch %ix86
%define SB2_TARGET i686-unknown-linux-gnu
%endif

# - BUILD ----------------------------------------------------------------------
%build

# Adopted from https://github.com/sailfishos/gecko-dev/blob/master/rpm/xulrunner-qt5.spec

export CARGO_HOME="%{BUILD_DIR}/cargo"
export CARGO_BUILD_TARGET=%SB2_TARGET

# When cross-compiling under SB2 rust needs to know what arch to emit
# when nothing is specified on the command line. That usually defaults
# to "whatever rust was built as" but in SB2 rust is accelerated and
# would produce x86 so this is how it knows differently. Not needed
# for native x86 builds
export SB2_RUST_TARGET_TRIPLE=%SB2_TARGET
export RUST_HOST_TARGET=%SB2_TARGET

export RUST_TARGET=%SB2_TARGET
export TARGET=%SB2_TARGET
export HOST=%SB2_TARGET
export SB2_TARGET=%SB2_TARGET

%ifarch %arm32 %arm64
export CROSS_COMPILE=%SB2_TARGET

# This avoids a malloc hang in sb2 gated calls to execvp/dup2/chdir
# during fork/exec. It has no effect outside sb2 so doesn't hurt
# native builds.
export SB2_RUST_EXECVP_SHIM="/usr/bin/env LD_PRELOAD=/usr/lib/libsb2/libsb2.so.1 /usr/bin/env"
export SB2_RUST_USE_REAL_EXECVP=Yes
export SB2_RUST_USE_REAL_FN=Yes
%endif

export CC=gcc
export CXX=g++
export AR="ar"
export NM="gcc-nm"
export RANLIB="gcc-ranlib"
export PKG_CONFIG="pkg-config"

export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now -Ccodegen-units=1 %{?rustflags}"
export CARGO_INCREMENTAL=0

export CRATE_CC_NO_DEFAULTS=1
cargo build --release --target-dir=%{BUILD_DIR} --manifest-path %{_sourcedir}/../Cargo.toml

# - INSTALL --------------------------------------------------------------------
%install

install -Dm 755 target/%{SB2_TARGET}/release/%{name} -t %{buildroot}%{_bindir}

# - FILES ----------------------------------------------------------------------
%files

%defattr(-,root,root,-)
%{_bindir}


