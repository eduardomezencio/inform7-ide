#
# Spec file for the Inform 7 IDE on OpenSUSE. Rename to inform7-ide.spec.
#
# Copyright (c) 2011 Malcolm J Lewis <malcolmlewis@opensuse.org>
# Copyright (c) 2014 Vincent Petry <pvince81@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define compiler_version 6M62

Name:           inform7-ide
Version:        2.0.0
Release:        0
License:        GPL-3.0
Summary:        The Inform 7 interactive fiction programming environment
Url:            http://inform7.com/
Group:          Development/Languages/Other
Source0:        https://github.com/ptomato/inform7-ide/releases/download/%{version}/inform7-ide-%{version}.tar.xz
Source1:        http://inform7.com/apps/%{compiler_version}/I7_%{compiler_version}_Linux_all.tar.gz
BuildRequires:  fdupes
BuildRequires:  libplist-devel
BuildRequires:  libgoocanvas3-devel
BuildRequires:  graphviz
BuildRequires:  gtksourceview4-devel
BuildRequires:  gspell-devel
BuildRequires:  libwebkit2gtk3-devel
BuildRequires:  lzma
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  gstreamer-devel >= 1.2
BuildRequires:  gstreamer-plugins-base >= 1.2
BuildRequires:  gstreamer-plugins-good >= 1.2
BuildRequires:  gstreamer-plugins-bad >= 1.2
# Required by autogen.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
#Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
Inform is a design system for interactive fiction based on natural
language, a new medium of writing which came out of the "text adventure"
games of the 1980s.
It has been used by many leading writers of IF over the last twenty
years, for projects ranging from historical reconstructions, through
games, to art pieces, which have won numerous awards and competitions.

%prep
%setup -q
%setup -T -D -a 1

cd inform7-%{compiler_version}
%ifarch x86_64
tar xvf inform7-compilers_%{compiler_version}_x86_64.tar.gz
cp share/inform7/Compilers/ni ../src/ni/
%else
tar xvf inform7-compilers_%{compiler_version}_i386.tar.gz
cp share/inform7/Compilers/ni ../src/ni/
%endif
cd ..

%build
# need to run autogen.sh to make it find gstreamer 1.2
./autogen.sh
%configure --prefix=%{_prefix} --enable-manuals --with-sound=gstreamer
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/com.inform7.IDE.desktop
%find_lang %{name}
%fdupes %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_post
%glib2_gsettings_schema_postun

%clean
%{?buildroot:rm -rf %{buildroot}}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_libdir}/%{name}
%ifarch x86_64
%{_prefix}/lib/%{name}
%endif
%{_datadir}/applications/com.inform7.IDE.desktop
%{_datadir}/metainfo/com.inform7.IDE.appdata.xml
%doc %{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/com.inform7.IDE.gschema.xml
%{_datadir}/icons/hicolor/*/*
%{_datadir}/mime/packages/inform7.xml

#%files lang -f %{name}.lang

%changelog
* Tue Apr 19 2022 Philip Chimento <philip.chimento@gmail.com> - 2.0.0
- Bumped version to new versioning scheme 2.0.0
* Sun Feb 7 2016 Vincent Petry <pvince81@opensuse.org>
- Updated Source0 URL
- Added patch for gettext version
* Sun Jan 10 2016 Philip Chimento <philip.chimento@gmail.com>
- Updated to version 6M62
* Sun Jun 1 2014 Vincent Petry <pvince81@opensuse.org>
- Updated spec for version 6L02
* Mon Oct 10 2011 Malcolm J Lewis <malcolmlewis@opensuse.org>
- Rewrote spec file.
* Mon Nov 1 2010 P.F. Chimento <philip.chimento@gmail.com>
- Updated OpenSUSE version of spec file.
* Tue Oct 26 2010 P.F. Chimento <philip.chimento@gmail.com>
- Added Quixe and Eric Eve directories to packing list.
* Sat Jul 3 2010 P.F. Chimento <philip.chimento@gmail.com>
- Fixed rpmlint warnings.
* Thu Jun 24 2010 P.F. Chimento <philip.chimento@gmail.com>
- Added Parchment directory to packing list.
* Fri Apr 10 2009 P.F. Chimento <philip.chimento@gmail.com>
- Overhauled build process.
* Mon Feb 23 2009 P.F. Chimento <philip.chimento@gmail.com>
- Added the gtkterp-git binary to the packing list.
* Sat Dec 6 2008 P.F. Chimento <philip.chimento@gmail.com>
- Repackaged to release .1 of Public Beta Build 5U92.
* Sun Sep 14 2008 P.F. Chimento <philip.chimento@gmail.com>
- Added scriptlets for GConf2 schemas processing.
* Fri Sep 12 2008 P.F. Chimento <philip.chimento@gmail.com>
- Updated to Public Beta Build 5U92.
* Sat May 3 2008 P.F. Chimento <philip.chimento@gmail.com>
- Fedora 8 release bumped to 2, replacing outdated Glulx Entry Points.
* Wed Apr 30 2008 P.F. Chimento <philip.chimento@gmail.com>
- Updated to Public Beta Build 5T18.
* Mon Dec 3 2007 P.F. Chimento <philip.chimento@gmail.com>
- Updated to Public Beta Build 5J39.
* Tue Nov 13 2007 P.F. Chimento <philip.chimento@gmail.com>
- Updated to Public Beta Build 5G67.
* Sat Aug 18 2007 P.F. Chimento <philip.chimento@gmail.com>
- Updated to version 0.4.
* Sat Jun 16 2007 P.F. Chimento <philip.chimento@gmail.com>
- Repackaged for Fedora 7.
* Sat Jun 2 2007 P.F. Chimento <philip.chimento@gmail.com>
- Repackaged to release 2.
* Sun May 27 2007 P.F. Chimento <philip.chimento@gmail.com>
- Updated to version 0.3.
* Mon Apr 9 2007 P.F. Chimento <philip.chimento@gmail.com>
- Updated to version 0.2.
