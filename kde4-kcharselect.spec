#
%define		_state		stable
%define		orgname		kcharselect
%define		qtver		4.8.0

Summary:	K Desktop Environment - KDE Character Selector
Name:		kde4-kcharselect
Version:	4.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	4150d41fe47882c9a3f994dba15283eb
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
Requires:	kde4-kdebase-workspace >= %{version}
Obsoletes:	kde4-kdeutils-kcharselect
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application for selecting characters.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kcharselect
%{_datadir}/apps/kcharselect
%{_datadir}/apps/kconf_update/kcharselect.upd
%{_desktopdir}/kde4/KCharSelect.desktop
