%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		hitori
Version:	3.16.1
Release:	2
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
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING-DOCS MAINTAINERS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}-symbolic.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml


%changelog
* Mon Dec 22 2014 ovitters <ovitters> 3.14.2.1-1.mga5
+ Revision: 804794
- new version 3.14.2.1

* Mon Oct 27 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 793819
- new version 3.14.1

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0.1-2.mga5
+ Revision: 749406
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0.1-1.mga5
+ Revision: 719213
- new version 3.14.0.1

* Wed Sep 17 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 691345
- new version 3.13.92

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665316
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655349
- new version 3.13.4

* Wed Jul 09 2014 ovitters <ovitters> 0.4.5-1.mga5
+ Revision: 650873
- new version 0.4.5

* Thu Jun 19 2014 ovitters <ovitters> 0.4.4-1.mga5
+ Revision: 638123
- new version 0.4.4

* Sun May 04 2014 ovitters <ovitters> 0.4.3-1.mga5
+ Revision: 620063
- new version 0.4.3

* Sat Nov 09 2013 ovitters <ovitters> 0.4.2-2.mga4
+ Revision: 550176
- fix url

* Fri Nov 08 2013 ovitters <ovitters> 0.4.2-1.mga4
+ Revision: 549991
- new version 0.4.2

* Sat Oct 19 2013 umeabot <umeabot> 0.4.1-2.mga4
+ Revision: 531247
- Mageia 4 Mass Rebuild

* Fri Aug 02 2013 ovitters <ovitters> 0.4.1-1.mga4
+ Revision: 462651
- new version 0.4.1

* Sat Jan 12 2013 umeabot <umeabot> 0.4.0-2.mga3
+ Revision: 353272
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

  + fwang <fwang>
    - add more br
    - cleanup spec

* Sun Sep 30 2012 ovitters <ovitters> 0.4.0-1.mga3
+ Revision: 300892
- br yelp-tools,itstool
- new version 0.4.0

* Sun Sep 30 2012 ovitters <ovitters> 0.3.2-1.mga3
+ Revision: 300883
- change group to  Games/Puzzles
- Import modified Fedora package

