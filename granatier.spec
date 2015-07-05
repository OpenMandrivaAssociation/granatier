%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	KDE Bomberman game
Name:		granatier
Epoch:		1
Version:	15.04.3
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/granatier/
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(ECM)

%description
Granatier is a clone of the classic Bomberman game, inspired by the work
of the Clanbomber clone.

%files
%{_bindir}/granatier
%{_datadir}/appdata/granatier.appdata.xml
%{_datadir}/applications/org.kde.granatier.desktop
%{_datadir}/granatier
%{_datadir}/config.kcfg/granatier.kcfg
%{_docdir}/*/*/granatier
%{_iconsdir}/*/*/apps/granatier.*
%{_datadir}/kxmlgui5/granatier

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
