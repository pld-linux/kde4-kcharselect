#
%define		_state		stable
%define		orgname		kcharselect
%define		qtver		4.8.3

Summary:	K Desktop Environment - KDE Character Selector
Name:		kde4-kcharselect
Version:	4.14.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	41c582837e2a29588713d6627c4fb48e
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
Requires:	kde4-kdebase-workspace >= 4.11.4
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
%{_desktopdir}/kde4/KCharSelect.desktop
