%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Bomberman game
Name:		granatier
Epoch:		1
Version:	20.04.2
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		http://www.kde.org/applications/games/granatier/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)

%description
Granatier is a clone of the classic Bomberman game, inspired by the work
of the Clanbomber clone.

%files -f granatier.lang
%{_datadir}/qlogging-categories5/granatier.categories
%{_bindir}/granatier
%{_datadir}/metainfo/org.kde.granatier.appdata.xml
%{_datadir}/applications/org.kde.granatier.desktop
%{_datadir}/granatier
%{_datadir}/config.kcfg/granatier.kcfg
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
%find_lang granatier --with-html
