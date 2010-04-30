Name:           clementine
Version:        0.2.99
Release:        1%{?dist}
Summary:        A music player and library organiser

Group:          Applications/Multimedia
License:        GPLv3
URL:            http://code.google.com/p/clementine-player
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  desktop-file-utils liblastfm-devel taglib-devel gettext
BuildRequires:  libnotify-devel qt4-devel boost-devel gcc-c++
BuildRequires:  cmake gstreamer-devel gstreamer-plugins-base-devel

# GStreamer codec dependencies
Requires:       gstreamer0.10(decoder-audio/mpeg)(mpegversion=1)(layer=3)
Requires:       gstreamer0.10(decoder-audio/x-vorbis)
Requires:       gstreamer0.10(decoder-audio/x-flac)
Requires:       gstreamer0.10(decoder-audio/x-speex)
Requires:       gstreamer0.10(decoder-audio/x-wav)

%description
Clementine is a modern music player and library organiser.
It is largely a port of Amarok 1.4, with some features rewritten to take
advantage of Qt4.

%prep
%setup -q


%build
cd bin
cmake .. -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr/
make %{?_smp_mflags}

%install
cd bin
make install

%clean
cd bin
make clean


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/clementine
%{_datadir}/applications/clementine.desktop
%{_datadir}/icons/hicolor/64x64/apps/application-x-clementine.png


%changelog
* Thu Apr 29 2010 David Sansome <me@davidsansome.com> - 0.2.99
- Version 0.3 rc 1

* Mon Mar 22 2010 David Sansome <me@davidsansome.com> - 0.2
- Version 0.2

* Sun Feb 21 2010 David Sansome <me@davidsansome.com> - 0.1-5
- Various last-minute bugfixes

* Sun Jan 17 2010 David Sansome <me@davidsansome.com> - 0.1-1
- Initial package
