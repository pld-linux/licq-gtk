Summary:	GTK+ interface plugin for licq
Summary(pl):	Wtyczka dla licq dostarczaj±ca interfejs GTK+
Name:		licq-gtk
Version:	0.51
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://gtk.licq.org/download/gtk+licq-%{version}.tar.gz
# Source0-md5:	be09ec38ef2c5f7b078ff31f81371a38
Source1:	%{name}_gui.desktop
URL:		http://gtk.licq.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_gnome:BuildRequires:	db3-devel}
%{!?_without_gnome:BuildRequires:	esound-devel}
BuildRequires:	gettext-devel
%{!?_without_gnome:BuildRequires:	gnome-core-devel}
BuildRequires:	gtk+-devel
BuildRequires:	licq-devel >= 1.0.2
BuildRequires:	libltdl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl
BuildRequires:	pspell-devel
Requires:	licq >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xdatadir	/usr/X11R6/share

%description
GTK+ interface plugin for licq.

%description -l pl
Wtyczka dla licq dostarczaj±ca interfejs GTK+.

%prep
%setup -n gtk+licq-%{version} -q

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?_without_gnome:--disable-gnome} \
	%{!?_without_gnome:--enable-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Network/Communications

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	gtklicq_helpdir=%{_xdatadir}/gnome/help/gtk+licq/C

install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Network/Communications

# gtk+licq is proper here! Don't add --all-name
%find_lang gtk+licq %{name}.lang  --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root)%{_libdir}/licq/*
%{_datadir}/licq/gtk-gui
%{_applnkdir}/Network/Communications/*
