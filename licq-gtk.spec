Summary:	GTK+ interface plugin for licq
Summary(pl):	Wtyczka dla licq dostarczająca interfejs GTK+
Name:		licq-gtk
Version:	0.51
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://gtk.licq.org/download/gtk+licq-%{version}.tar.gz
Source1:	%{name}_gui.desktop
URL:		http://gtk.licq.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{!?_without_gnome:BuildRequires:	esound-devel}
%{!?_without_gnome:BuildRequires:	db3-devel}
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

%define         _x11_datadir	/usr/X11R6/share/data

%description
GTK+ interface plugin for licq.

%description -l pl
Wtyczka dla licq dostarczająca interfejs GTK+.

%prep
%setup -n gtk+licq-%{version} -q

%build
rm missing
gettextize --copy --force
libtoolize --copy --force
aclocal
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
	gtklicq_helpdir=%{_x11_datadir}/gnome/help/gtk+licq/C

install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Network/Communications

# gtk+licq is proper here! Don't add --all-name
%find_lang gtk+licq %{name}.lang  --with-gnome

gzip -9nf AUTHORS NEWS README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root)%{_libdir}/licq/*
%{_datadir}/licq/gtk-gui
%{_applnkdir}/Network/Communications/*
