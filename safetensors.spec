Name:     safetensors
Version:  0.4.4
Release:  3%{?dist}
Summary:  A fast and safe tensor serialization library
Summary(zh_CN):  一个快速且安全的张量序列化库
License:  Apache-2.0
URL:      https://github.com/huggingface/safetensors
Source0:  safetensors-%{version}.tar.gz
Source1:	vendor.tar.gz
Source2:	config

BuildRequires: rust, cargo, make, gcc, openssl-devel pkgconfig

%description
Safetensors is a fast and safe tensor serialization library. It aims to provide a more efficient and secure way to serialize tensors compared to other existing solutions.

%description -l zh_CN
Safetensors 是一个快速且安全的张量序列化库。与其他现有解决方案相比，它旨在提供一种更高效、更安全的张量序列化方式。

%prep
%setup -q -n safetensors-%{version}

%build
cd bindings/python
mkdir .cargo
cp %{SOURCE2} .cargo/
tar zxvf %{SOURCE1}
cargo vendor > $CARGO_HOME/config
cargo build --release --offline

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/safetensors %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a ../README.md ../LICENSE ../AUTHORS ../CHANGELOG.md %{buildroot}%{_docdir}/%{name}

%files
%doc %{_docdir}/%{name}/README.md
%doc %{_docdir}/%{name}/CHANGELOG.md
%doc %{_docdir}/%{name}/AUTHORS
%license %{_docdir}/%{name}/LICENSE
%{_bindir}/safetensors

%changelog
* Thu Mar 13 2025 Yihang Feng <fengyihang1@huawei.com> - 0.4.4-1
- 更新到 0.4.4 版本
- 添加离线构建支持
- 规范文件安装路径
