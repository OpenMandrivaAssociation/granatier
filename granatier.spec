Name:		granatier
Version:	4.10.1
Release:	1
Epoch:		1
Summary:	KDE Bomberman game
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/granatier/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Granatier is a clone of the classic Bomberman game, inspired by the work
of the Clanbomber clone.

%files
%{_kde_bindir}/granatier
%{_kde_applicationsdir}/granatier.desktop
%{_kde_appsdir}/granatier
%{_kde_datadir}/config.kcfg/granatier.kcfg
%{_kde_docdir}/*/*/granatier
%{_kde_iconsdir}/*/*/apps/granatier.*

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

