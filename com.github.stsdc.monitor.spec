%global srcname monitor
%global appname com.github.stsdc.monitor

Name: com.github.stsdc.monitor
Version: 0.11.0
Release: %autorelease
Summary: Manage processes and monitor system resources
License: GPLv3
URL: https://github.com/stsdc/monitor

Source: monitor.tar.gz


BuildRequires: meson
BuildRequires: vala
BuildRequires: gcc
BuildRequires: sassc
BuildRequires: git
BuildRequires: libxnvctrl0-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(libgtop-2.0) # libgtop2-devel
BuildRequires: pkgconfig(libwnck-3.0) # libwnck3-devel
BuildRequires: pkgconfig(wingpanel) # wingpanel-devel
BuildRequires: pkgconfig(gdk-x11-3.0) # gdk3-devel
BuildRequires: pkgconfig(libx11-6)
BuildRequires: pkgconfig(libhandy-1) # libhandy-devel
BuildRequires: pkgconfig(libudisks2-devel)

%description

%prep
%autosetup -n %{srcname} -p1

%build
%meson -Dindicator-wingpanel=enabled # this will probably go, since majority uses gnome on Fedora
%meson_build

%install
%meson_install
%find_lang %{appname}

%files -f %{appname}.lang
%{_bindir}/com.github.stsdc.monitor
%{_libdir}/liblivechart.so
%{_libdir}/wingpanel/libmonitor.so

%{_libdir}/pkgconfig/livechart.pc
%{_datadir}/vala/vapi/livechart.vapi
%{_includedir}/livechart.h

%{_datadir}/vala/vapi/libxnvctrl.vapi

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.appdata.xml

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Tue Oct 05 2021 meson <meson@example.com> - 
- 
