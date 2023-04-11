%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define _disable_rebuild_configure 1

Name:		hitori
Version:	44.0
Release:	1
Summary:	Logic puzzle game for GNOME

Group:		Games/Puzzles
# The executable is licensed under GPLv3+, while the user manual is CC-BY-SA.
License:	GPLv3+ and CC-BY-SA
URL:		https://wiki.gnome.org/Hitori
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gettext-devel
BuildRequires:	itstool
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(cairo) >= 1.4
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	intltool >= 0.35.0
BuildRequires:  meson
Requires:	hicolor-icon-theme

%description
A small application written to allow one to play the Hitori puzzle game,
which is similar in theme to more popular puzzles such as Sudoku.

It has full support for playing the game (i.e. it checks all three rules are
satisfied). It has undo/redo support, can give hints, and allows for cells
to be tagged with one of two different tags, to aid in solving the puzzle.
It has support for anything from 5×5 to 10×10 grids.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS MAINTAINERS NEWS README.md
%license COPYING COPYING-DOCS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.*.desktop
%{_iconsdir}/hicolor/*/apps/org.gnome.*
%{_datadir}/metainfo/org.gnome.*.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml
