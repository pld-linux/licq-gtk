Summary:	GTK+ interface plugin for licq
Summary(pl):	Wtyczka dla licq dostarczaj±ca interfejs GTK+
Name:		licq-gtk
Version:	0.50.1
Release:	1
License:	GPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://gtk.licq.org/download/gtk+licq-%{version}.tar.gz
Source1:	licq-gtk_gui.desktop
URL:		http://gtk.licq.org/
%{!?no_gnome:BuildRequires:	esound-devel}
%{!?no_gnome:BuildRequires:	db2-devel}
BuildRequires:	gettext-devel
%{!?no_gnome:BuildRequires:	gnome-core-devel}
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	licq-devel >= 1.0.2
BuildRequires:	pspell-devel
Requires:	licq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ interface plugin for licq.

%description -l pl
Wtyczka dla licq dostarczaj±ca interfejs GTK+.

%prep
%setup -n gtk+licq-%{version} -q

%build
gettextize --copy --force
%configure \
	%{?no_gnome:--without-gnome} \
	%{!?no_gnome:--with-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Network/Communications

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Network/Communications

gzip -9nf AUTHORS NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root)%{_libdir}/licq/*
%{_datadir}/licq/gtk-gui
%{_applnkdir}/Network/Communications/*
