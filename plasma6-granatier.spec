#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Bomberman game
Name:		plasma6-granatier
Version:	24.08.2
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
Url:		https://www.kde.org/applications/games/granatier/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/granatier/-/archive/%{gitbranch}/granatier-%{gitbranchd}.tar.bz2#/granatier-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/granatier-%{version}.tar.xz
%endif
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KDEGames6)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Svg)

%description
Granatier is a clone of the classic Bomberman game, inspired by the work
of the Clanbomber clone.

%files -f granatier.lang
%{_datadir}/qlogging-categories6/granatier.categories
%{_datadir}/qlogging-categories6/granatier.renamecategories
%{_bindir}/granatier
%{_datadir}/metainfo/org.kde.granatier.appdata.xml
%{_datadir}/applications/org.kde.granatier.desktop
%{_datadir}/granatier
%{_datadir}/config.kcfg/granatier.kcfg
%{_iconsdir}/*/*/apps/granatier.*

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n granatier-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang granatier --with-html
