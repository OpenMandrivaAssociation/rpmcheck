%define name	rpmcheck
%define version	0.0.2368
%define release	%mkrel 9

%if %mdkversion > 200900
%define camlzip_inc +camlzip
%else
%define camlzip_inc +site-lib/camlzip
%endif

Summary:	A tool to check consistency of rpm repositories
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Configuration/Packaging
# No website yet
URL:		https://www.edos-project.org/xwiki/bin/Main/Wp2
# There is no released version yet. Sources are from the svn depot at
# https://protactinium.pps.jussieu.fr:12345/svn/edos/users/vouillon
Source:		%name-%version.tar.bz2
Patch0:     rpmcheck-0.0.2368-handle-suggests.patch
Patch1:     rpmcheck-0.0.2368-no-doc-conflict.patch
Patch2:     rpmcheck-0.0.2368-allow-uncompressed-hdlists.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-camlzip-devel
Buildroot:	%_tmppath/%name-%version

%description
rpmcheck is a tool to check consistency of Mandriva Linux rpm repositories
(that is, of hdlist files.)

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build
%__make rpmcheck \
    COMPFLAGS="-I %{camlzip_inc}" \
    OPTLINKFLAGS="unix.cmxa str.cmxa zip.cmxa -I %{camlzip_inc}"

%install
%__rm -rf %buildroot
%__install -d %buildroot%_bindir
%__install -m 0755 rpmcheck %buildroot%_bindir

%clean
%__rm -rf %buildroot

%files
%doc COPYING README
%_bindir/%name


