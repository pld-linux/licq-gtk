Summary:	GTK+ interface plugin for licq
Summary(pl):	Wtyczka dla licq dostarczaj±ca interfejs GTK+
Name:		licq-gtk
Version:	0.39
Release:	1
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
License:	GPL
Source0:	http://gtk.licq.org/download/gtk+licq-%{version}.tar.gz
Patch0:		%{name}-_PC_NAME_MAX.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://gtk.licq.org/
BuildRequires:	libstdc++-devel
BuildRequires:	gtk+-devel
BuildRequires:	licq-devel
BuildRequires:	gettext-devel
BuildRequires:	glibc-db2-devel
Requires:	licq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ interface plugin for licq

%description -l pl
Wtyczka dla licq dostarczaj±ca interfejs GTK+

%prep
%setup -n gtk+licq-%{version} -q
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
autoheader;autoconf;automake; 

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf AUTHORS BUGS NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/licq/*
%{_datadir}/licq/gtk-gui

%doc *.gz
