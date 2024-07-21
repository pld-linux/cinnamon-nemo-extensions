%define		nemo_ver	6.2.0
%define		translations_version	6.2.2
Summary:	Extensions for Nemo file manager
Summary(pl.UTF-8):	Rozszerzenia zarządcy plików Nemo
Name:		cinnamon-nemo-extensions
Version:	6.2.0
Release:	1
License:	GPL v2+, GPL v3+, LGPL v2
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/nemo-extensions/releases
Source0:	https://github.com/linuxmint/nemo-extensions/archive/%{version}/nemo-extensions-%{version}.tar.gz
# Source0-md5:	6a082de626d2ab1fb5cb07e5fe859f2a
#Source1Download: https://github.com/linuxmint/cinnamon-translations/releases
Source1:	https://github.com/linuxmint/cinnamon-translations/archive/%{translations_version}/cinnamon-translations-%{translations_version}.tar.gz
# Source1-md5:	ca66b0eadc9416ef66384b3b278554ad
Patch0:		%{name}-pc.patch
URL:		https://github.com/linuxmint/nemo-extensions
BuildRequires:	avahi-glib-devel
BuildRequires:	cinnamon-desktop-devel >= 3.0.0
BuildRequires:	cinnamon-nemo-devel >= %{nemo_ver}
BuildRequires:	cjs-devel >= 4.6.0
BuildRequires:	clutter-devel >= 1.11.4
BuildRequires:	clutter-gst-devel >= 3.0
BuildRequires:	clutter-gtk-devel >= 1.0.1
BuildRequires:	dbus-glib-devel >= 0.78
BuildRequires:	freetype-devel >= 2
BuildRequires:	gcr-ui-devel >= 3.4.0
BuildRequires:	gdk-pixbuf2-devel >= 2.23.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 0.9.2
BuildRequires:	gpgme-devel >= 1.2.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.6
BuildRequires:	gtk-doc
BuildRequires:	gtk-webkit4.1-devel >= 2.34
BuildRequires:	gtksourceview4-devel >= 4.0.3
BuildRequires:	libcryptui-devel
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libmusicbrainz5-devel
BuildRequires:	libnotify-devel >= 0.7.0
BuildRequires:	linux-libc-headers >= 7:2.6.38
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python-pygobject3-common-devel
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0
BuildRequires:	python3-setuptools
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
# gtk-webkit4.1 based
BuildRequires:	xreader-devel >= 3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensions for Nemo file manager (used in Cinnamon desktop
environment).

%description -l pl.UTF-8
Rozszerzenia zarządcy plików Nemo (używanego w środowisku graficznym
Cinnamon).

%package common
Summary:	Common files for Nemo file manager extensions
Summary(pl.UTF-8):	Wspólne pliki rozszerzeń zarządcy plików Nemo
Group:		X11/Applications

%description common
Common files for Nemo file manager extensions.

%description common -l pl.UTF-8
Wspólne pliki rozszerzeń zarządcy plików Nemo.

%package -n cinnamon-nemo-python
Summary:	Python scripting extension for Nemo
Summary(pl.UTF-8):	Rozszerzenie Nemo o obsługę skryptów Pythona
License:	GPL v2+
Group:		X11/Libraries
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	python3-pygobject3 >= 3

%description -n cinnamon-nemo-python
Python scripting extension for Nemo.

%description -n cinnamon-nemo-python -l pl.UTF-8
Rozszerzenie Nemo o obsługę skryptów Pythona.

%package -n cinnamon-nemo-python-devel
Summary:	Development files for Python scripting extension for Nemo
Summary(pl.UTF-8):	Pliki programistyczne dla rozszerzenia Nemo o obsługę skryptów w Pythonie
License:	GPL v2+
Group:		X11/Development/Libraries
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	pkgconfig

%description -n cinnamon-nemo-python-devel
Development files for Python scripting extension for Nemo.

%description -n cinnamon-nemo-python-devel -l pl.UTF-8
Pliki programistyczne dla rozszerzenia Nemo o obsługę skryptów w
Pythonie.

%package -n cinnamon-nemo-python-apidocs
Summary:	API documentation for Nemo Python scripting extension
Summary(pl.UTF-8):	Dokumentacja API rozszerzenia Nemo do obsługi skryptów Pythona
Group:		Documentation

%description -n cinnamon-nemo-python-apidocs
API documentation for Nemo Python scripting extension.

%description -n cinnamon-nemo-python-apidocs -l pl.UTF-8
Dokumentacja API rozszerzenia Nemo do obsługi skryptów Pythona.

%package -n cinnamon-nemo-extension-audio-tab
Summary:	Audio tag information extension for Nemo
Summary(pl.UTF-8):	Rozszerzenie Nemo z informacjami o znacznikach w plikach dźwiękowych
License:	GPL v3+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	python3-mutagen
Requires:	python3-pygobject3 >= 3.0
BuildArch:	noarch

%description -n cinnamon-nemo-extension-audio-tab
audio-tab is Nemo extension to view audio tag information from the
properties tab.

%description -n cinnamon-nemo-extension-audio-tab -l pl.UTF-8
audio-tab to rozszerzenie Nemo do oglądania informacji o znacznikach w
plikach dźwiękowych z poziomu zakładki właściwości.

%package -n cinnamon-nemo-extension-compare
Summary:	Context menu comparison extension for Nemo file manager
Summary(pl.UTF-8):	Rozszerzenie zarządcy plików Nemo o porównywanie z menu kontekstowego
License:	GPL v3+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	meld
Requires:	python3-pygobject3 >= 3.0
BuildArch:	noarch

%description -n cinnamon-nemo-extension-compare
Simple Nemo file manager extension, inspired by the discontinued
diff-ext extension. It extends context menu by providing "Compare ..."
actions. Compare tool for different situations (one-on-one, three-way,
multi-compare) can be chosen by configurator tool.

%description -n cinnamon-nemo-extension-compare -l pl.UTF-8
Proste rozszerzenie zarządcy plików Nemo, zainspirowane porzuconym już
rozszerzeniem diff-ext. Rozszerza menu kontekstowe udostępniając akcje
"Porównaj ...". Narzędzie do porównywania w różnych sytuacjach (jeden
do jednego, trzech wersji, wielokrotnego) można wybrać w
konfiguratorze.

%package -n cinnamon-nemo-extension-dropbox
Summary:	Dropbox extension for Nemo file manager
Summary(pl.UTF-8):	Rozszerzenie Dropbox do zarządcy plików Nemo
License:	GPL v3+
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	glib2 >= 1:2.38
Requires:	hicolor-icon-theme

%description -n cinnamon-nemo-extension-dropbox
Dropbox extension for Nemo file manager.

%description -n cinnamon-nemo-extension-dropbox -l pl.UTF-8
Rozszerzenie Dropbox do zarządcy plików Nemo.

%package -n cinnamon-nemo-extension-emblems
Summary:	Emblem support for Nemo
Summary(pl.UTF-8):	Obsługa emblematów dla Nemo
License:	GPL v3+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	python3-pygobject3 >= 3.0
BuildArch:	noarch

%description -n cinnamon-nemo-extension-emblems
Restores the emblems functionality that used to be in GNOME 2.

%description -n cinnamon-nemo-extension-emblems -l pl.UTF-8
To rozszerzenie przywraca funkcjonalność emblematów, obecną w GNOME 2.

%package -n cinnamon-nemo-extension-fileroller
Summary:	File Roller extension for Nemo
Summary(pl.UTF-8):	Rozszerzenie File Roller dla Nemo
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	file-roller

%description -n cinnamon-nemo-extension-fileroller
This extension adds entries to the context menu in Nemo, which allow
you to make use of the compress and extract functions of the File
Roller archive manager.

%description -n cinnamon-nemo-extension-fileroller -l pl.UTF-8
To rozszerzenie dodane do menu kontekstowego w Nemo pozycje
pozwalające na wykorzystanie funkcji kompresji i rozpakowywania
zarządcy archiwów File Roller.

%package -n cinnamon-nemo-extension-image-converter
Summary:	Nemo extension to mass resize images
Summary(pl.UTF-8):	Rozszerzenie Nemo do masowej zmiany rozmiarów obrazów
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	ImageMagick

%description -n cinnamon-nemo-extension-image-converter
Adds a "Resize Images..." menu item to the context menu. This opens a
dialog where you set the desired image size and file name.

%description -n cinnamon-nemo-extension-image-converter -l pl.UTF-8
To rozszerzenie dodaje element menu kontekstowego "Zmień rozmiar
zdjęć...", otwierający okno dialogowe, gdzie można ustawić pożądany
rozmiar obrazu i nazwę pliku.

%package -n cinnamon-nemo-extension-media-columns
Summary:	Nemo Media Columns extension
Summary(pl.UTF-8):	Rozszerzenie Nemo Media Columns
License:	GPL v3
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	gdk-pixbuf2 >= 2
Requires:	gexiv2 >= 0.10
Requires:	python3-PyPDF2
Requires:	python3-pygobject3 >= 3.0
Requires:	python3-mutagen
Requires:	python3-pillow
Requires:	python3-pymediainfo

%description -n cinnamon-nemo-extension-media-columns
This Nemo File Manager extension provides additional columns for the
List View related to media-type files.

%description -n cinnamon-nemo-extension-media-columns -l pl.UTF-8
To rozszerzenie zarządcy plików Nemo zapewnia na widoku listy
dodatkowe kolumny związane z plikami multimedialnymi.

%package -n cinnamon-nemo-extension-pastebin
Summary:	Pastebin extension for Nemo
Summary(pl.UTF-8):	Rozszerzenie Pastebin dla Nemo
License:	GPL v2+
Group:		X11/Applications
Requires(post,postun):	glib2 >= 1:2.38
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	hicolor-icon-theme
Requires:	libnotify >= 0.7
Requires:	pastebinit
Requires:	python3-pygobject3 >= 3.0
BuildArch:	noarch

%description -n cinnamon-nemo-extension-pastebin
nemo-pastebin is an extension for the Nemo file manager, which allows
users to send files to pastebins just a right-click away.

%description -n cinnamon-nemo-extension-pastebin -l pl.UTF-8
nemo-pastebin to rozszerzenie zarządcy plików Nemo, pozwalające
użytkownikom wysyłać pliki do pastebinów zwykłym kliknięciem prawym
przyciskiem.

%package -n cinnamon-nemo-extension-preview
Summary:	A quick previewer for Nemo
Summary(pl.UTF-8):	Szybki podgląd dla Nemo
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	gtk-webkit4.1 >= 2.34
Requires:	gtksourceview4 >= 4.0.3
Requires:	xreader-libs >= 3

%description -n cinnamon-nemo-extension-preview
Nemo Preview is a GtkClutter and Javascript-based quick previewer for
Nemo. It is capable of previewing documents, PDFs, sound and video
files, some text files, and possibly others in the future.

%description -n cinnamon-nemo-extension-preview -l pl.UTF-8
Nemo Preview to oparty na bibliotece GtkClutter i JavaScripcie szybki
podgląd dla Nemo. Potrafi podglądać dokumenty, pliki PDF, dźwiękowe i
filmowe, niektóre pliki tekstowe, a w przyszłości inne.

%package -n cinnamon-nemo-extension-repairer
Summary:	Nemo extension for filename encoding repair
Summary(pl.UTF-8):	Rozszerzenie Nemo do naprawy kodowania nazw plików
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo >= %{nemo_ver}

%description -n cinnamon-nemo-extension-repairer
nemo-filename-repairer is a Nemo extension which repairs filename
which uses wrong encoding in Nemo. This extension provides the context
menu for any file whose filename uses wrong encoding, so that you
cannot read the filename in Nemo. You can find a candidate for
filename in context menu or submenu. This extension also provides a
decoded name for URL encoded filename.

%description -n cinnamon-nemo-extension-repairer -l pl.UTF-8
nemo-filename-repairer to rozszerzenie Nemo służące do naprawiania
nazw plików, które w Nemo używają złego kodowania. Rozszerzenie
udostępnia menu kontekstowe dla każdego pliku ze złym kodowaniem,
pozwalając wybrać kandydata dla właściwej nazwy. Rozszerzenie
pozwala także dekodować nazwy z kodowania URL.

%package -n cinnamon-nemo-extension-seahorse
Summary:	PGP encryption and signing for Nemo
Summary(pl.UTF-8):	Szyfrowanie i podpisy PGP dla Nemo
License:	GPL v2+
Group:		X11/Applications
Requires(post,postun):	glib2 >= 1:2.38
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	dbus-glib >= 0.78
Requires:	gcr >= 3.4.0
Requires:	glib2 >= 1:2.38
Requires:	gnupg2 >= 2.2
Requires:	gpgme >= 1.2.0
Requires:	libnotify >= 0.7.0
Requires:	seahorse

%description -n cinnamon-nemo-extension-seahorse
Seahorse Nemo is an extension for Nemo which allows encryption and
decryption of OpenPGP files using GnuPG.

%description -n cinnamon-nemo-extension-seahorse -l pl.UTF-8
Seahorse Nemo to rozszerzenie Nemo pozwalające na szyfrowanie i
odszyfrowywanie plików OpenPGP przy użyciu GnuPG.

%package -n cinnamon-nemo-extension-share
Summary:	Nemo extension to share folder using Samba
Summary(pl.UTF-8):	Rozszerzenie Nemo do współdzielenia folderów przy użyciu Samby
License:	GPL v2+
Group:		X11/Applications
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-desktop >= 3.0.0
Requires:	cinnamon-nemo >= %{nemo_ver}
Requires:	glib2 >= 1:2.38
Requires:	samba-client

%description -n cinnamon-nemo-extension-share
Nemo Share allows you to quickly share a folder from the Nemo file
manager without requiring root access.

%description -n cinnamon-nemo-extension-share -l pl.UTF-8
Nemo Share pozwala na szybkie udostępnienie folderu z zarządcy plików
Nemo bez wymagania dostępu administratora.

%package -n cinnamon-nemo-extension-terminal
Summary:	Embedded terminal window for Nemo
Summary(pl.UTF-8):	Osadzone okno terminala dla Nemo
License:	GPL v3+
Group:		X11/Applications
Requires(post,postun):	glib2 >= 1:2.38
Requires:	%{name}-common = %{version}-%{release}
Requires:	cinnamon-nemo-python = %{version}-%{release}
Requires:	gtk+3 >= 3.8.4
Requires:	python3-pygobject3 >= 3.0
Requires:	vte >= 0.38
Requires:	xapps >= 2.6.0
BuildArch:	noarch

%description -n cinnamon-nemo-extension-terminal
Embedded terminal window for Nemo.

%description -n cinnamon-nemo-extension-terminal -l pl.UTF-8
Osadzone okno terminala dla Nemo.

%prep
%setup -q -n nemo-extensions-%{version} -a1
%patch0 -p1

%build
cd nemo-python
%meson build \
	-Dgtk_doc=true
%ninja_build -C build

cd ../nemo-audio-tab
%py3_build

cd ../nemo-compare
%py3_build

cd ../nemo-dropbox
%meson build
%ninja_build -C build

cd ../nemo-emblems
%py3_build

cd ../nemo-fileroller
%meson build
%ninja_build -C build

cd ../nemo-image-converter
%meson build \
	--default-library=shared
%ninja_build -C build

cd ../nemo-media-columns
%py3_build

cd ../nemo-pastebin
%py3_build

cd ../nemo-preview
%meson build
%ninja_build -C build

cd ../nemo-repairer
%meson build \
	--default-library=shared
%ninja_build -C build

cd ../nemo-seahorse
%meson build \
	--default-library=shared \
	-Dsharing=enabled
%ninja_build -C build

cd ../nemo-share
%meson build
%ninja_build -C build

cd ../nemo-terminal
%py3_build
cd ..

%{__make} -C cinnamon-translations-%{translations_version}

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C nemo-python/build

install -d $RPM_BUILD_ROOT%{_examplesdir}/cinnamon-nemo-python-%{version}
cp -p nemo-python/examples/* $RPM_BUILD_ROOT%{_examplesdir}/cinnamon-nemo-python-%{version}

cd nemo-audio-tab
%py3_install

cd ../nemo-compare
%py3_install
cd ..

%ninja_install -C nemo-dropbox/build

cd nemo-emblems
%py3_install
cd ..

%ninja_install -C nemo-fileroller/build

%ninja_install -C nemo-image-converter/build

cd nemo-media-columns
%py3_install

cd ../nemo-pastebin
%py3_install
cd ..

%ninja_install -C nemo-preview/build

%ninja_install -C nemo-repairer/build

%ninja_install -C nemo-seahorse/build

%ninja_install -C nemo-share/build

cd nemo-terminal
%py3_install
cd ..

cd cinnamon-translations-%{translations_version}
for f in usr/share/locale/*/LC_MESSAGES/nemo-extensions.mo ; do
	install -D "$f" "$RPM_BUILD_ROOT/$f"
done
cd ..

# not supported by glibc 2.39
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,mo}

# common for nemo-audio-tab[py],nemo-compare[py],nemo-emblems[py],nemo-fileroller[so],nemo-image-converter[so],nemo-media-columns[py],nemo-pastebin[py],nemo-preview[so],nemo-repairer[so],nemo-seahorse[so],nemo-share[so],nemo-terminal[py]
%find_lang nemo-extensions

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n cinnamon-nemo-extension-dropbox
%update_icon_cache hicolor

%postun	-n cinnamon-nemo-extension-dropbox
%update_icon_cache hicolor

%post	-n cinnamon-nemo-extension-media-columns
%glib_compile_schemas

%postun	-n cinnamon-nemo-extension-media-columns
%glib_compile_schemas

%post	-n cinnamon-nemo-extension-pastebin
%glib_compile_schemas
%update_icon_cache hicolor

%postun	-n cinnamon-nemo-extension-pastebin
%glib_compile_schemas
%update_icon_cache hicolor

%post	-n cinnamon-nemo-extension-seahorse
%glib_compile_schemas

%postun	-n cinnamon-nemo-extension-seahorse
%glib_compile_schemas

%post	-n cinnamon-nemo-extension-terminal
%glib_compile_schemas

%postun	-n cinnamon-nemo-extension-terminal
%glib_compile_schemas

%files common -f nemo-extensions.lang
%defattr(644,root,root,755)
%doc Readme.md

%files -n cinnamon-nemo-python
%defattr(644,root,root,755)
%doc nemo-python/{AUTHORS,README}
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-python.so
%dir %{_datadir}/nemo-python
%dir %{_datadir}/nemo-python/extensions

%files -n cinnamon-nemo-python-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/nemo-python.pc

%files -n cinnamon-nemo-python-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/nemo-python
%{_examplesdir}/cinnamon-nemo-python-%{version}

%files -n cinnamon-nemo-extension-audio-tab
%defattr(644,root,root,755)
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py
%dir %{_datadir}/nemo-audio-tab
%{_datadir}/nemo-audio-tab/nemo-audio-tab.glade
%{py3_sitescriptdir}/nemo_audio_tab-%{version}-py*.egg-info

%files -n cinnamon-nemo-extension-compare
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nemo-compare-preferences
%{_datadir}/nemo-python/extensions/nemo-compare.py
%dir %{_datadir}/nemo-compare
%{_datadir}/nemo-compare/nemo-compare-preferences.py
%{_datadir}/nemo-compare/utils.py*
%{py3_sitescriptdir}/nemo_compare-%{version}-py*.egg-info

%files -n cinnamon-nemo-extension-dropbox
%defattr(644,root,root,755)
%doc nemo-dropbox/{AUTHORS,README}
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-dropbox.so
%{_datadir}/nemo-dropbox
%{_iconsdir}/hicolor/symbolic/apps/nemo-dropbox-symbolic.svg

%files -n cinnamon-nemo-extension-emblems
%defattr(644,root,root,755)
%{_datadir}/nemo-python/extensions/nemo-emblems.py
%{py3_sitescriptdir}/nemo_emblems-%{version}-py*.egg-info

%files -n cinnamon-nemo-extension-fileroller
%defattr(644,root,root,755)
%doc nemo-fileroller/README
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so

%files -n cinnamon-nemo-extension-image-converter
%defattr(644,root,root,755)
%doc nemo-image-converter/{AUTHORS,NEWS,README}
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-image-converter.so
%{_datadir}/nemo-image-converter

%files -n cinnamon-nemo-extension-media-columns
%defattr(644,root,root,755)
%doc nemo-media-columns/{AUTHORS,MAINTAINERS,README}
%attr(755,root,root) %{_bindir}/nemo-media-columns-prefs
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-media-columns.gschema.xml
%{_datadir}/nemo-python/extensions/nemo-media-columns.py
%{py3_sitescriptdir}/nemo_media_columns-%{version}-py*.egg-info

%files -n cinnamon-nemo-extension-pastebin
%defattr(644,root,root,755)
%doc nemo-pastebin/{NEWS,README}
%attr(755,root,root) %{_bindir}/nemo-pastebin-configurator
%{_datadir}/nemo-python/extensions/nemo-pastebin.py
%{_datadir}/glib-2.0/schemas/nemo-pastebin.gschema.xml
%{_datadir}/nemo-pastebin
%{py3_sitescriptdir}/nemo_pastebin-%{version}-py*.egg-info
%{_iconsdir}/hicolor/48x48/apps/nemo-pastebin.png
%{_iconsdir}/hicolor/scalable/apps/nemo-pastebin.svg

%files -n cinnamon-nemo-extension-preview
%defattr(644,root,root,755)
%doc nemo-preview/{AUTHORS,README,TODO}
%attr(755,root,root) %{_bindir}/nemo-preview
%attr(755,root,root) %{_libexecdir}/nemo-preview-start
%dir %{_libdir}/nemo-preview
%attr(755,root,root) %{_libdir}/nemo-preview/libnemo-preview-1.0.so
%{_libdir}/nemo-preview/girepository-1.0
%dir %{_datadir}/nemo-preview
%{_datadir}/nemo-preview/gir-1.0
%{_datadir}/nemo-preview/js
%{_datadir}/dbus-1/services/org.nemo.Preview.service

%files -n cinnamon-nemo-extension-repairer
%defattr(644,root,root,755)
%doc nemo-repairer/{AUTHORS,NEWS,README}
%attr(755,root,root) %{_bindir}/nemo-filename-repairer
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-filename-repairer.so
%{_datadir}/nemo-filename-repairer

%files -n cinnamon-nemo-extension-seahorse
%defattr(644,root,root,755)
%doc nemo-seahorse/{AUTHORS,MAINTAINERS,NEWS,README}
%attr(755,root,root) %{_bindir}/nemo-seahorse-tool
%attr(755,root,root) %{_libdir}/nemo/extensions-3.0/libnemo-seahorse.so
%{_datadir}/glib-2.0/schemas/org.nemo.plugins.seahorse*.gschema.xml
%{_datadir}/nemo-seahorse
%{_mandir}/man1/nemo-seahorse-tool.1*

%files -n cinnamon-nemo-extension-share
%defattr(644,root,root,755)
%doc nemo-share/AUTHORS
%{_libdir}/nemo/extensions-3.0/libnemo-share.so
%{_datadir}/nemo-share
%{_datadir}/polkit-1/actions/org.nemo.share.samba_install.policy

%files -n cinnamon-nemo-extension-terminal
%defattr(644,root,root,755)
%doc nemo-terminal/{AUTHORS,README}
%attr(755,root,root) %{_bindir}/nemo-terminal-prefs
%{_datadir}/nemo-python/extensions/nemo_terminal.py
%{_datadir}/nemo-terminal
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%{py3_sitescriptdir}/nemo_terminal-%{version}-py*.egg-info
