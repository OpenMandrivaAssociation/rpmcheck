%define name	rpmcheck
%define version	0.0.2368
%define release	%mkrel 1

Summary:	A tool to check consistency of rpm repositories
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Configuration/Packaging
# No website yet
URL:		http://www.edos-project.org/xwiki/bin/Main/Wp2
# There is no released version yet. Sources are from the svn depot at
# https://protactinium.pps.jussieu.fr:12345/svn/edos/users/vouillon
Source:		%name-%version.tar.bz2
Buildroot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	ocaml
Patch0: rpmcheck-0.0.2368-handle-suggests.patch

%description
rpmcheck is a tool to check consistency of Mandriva Linux rpm repositories
(that is, of hdlist files.)

%prep
%setup -q
%patch0 -p1

%build
%__make rpmcheck

%install
%__rm -rf %buildroot
%__install -d %buildroot%_bindir
%__install -m 0755 rpmcheck %buildroot%_bindir

%clean
%__rm -rf %buildroot

%files
%doc COPYING README
%_bindir/%name


