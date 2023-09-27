Name: ocean-sounds
Version: 5.27.8
Release: 1
Source0:  %{name}.tar.gz
Summary: Ocean Sound Theme for Plasma
URL: https://invent.kde.org/plasma/ocean-sounds/
License: CC-BY-SA-4.0
Group: Graphical desktop/KDE
BuildArch: noarch
BuildRequires: cmake ninja extra-cmake-modules

%description
Ocean Sound Theme for Plasma

%prep
%setup -qn %{name}

%build

%install
mkdir -p %{buildroot}%{_datadir}/sounds/ocean
cp -r * %{buildroot}%{_datadir}/sounds/ocean/

%files
%dir %{_datadir}/sounds/ocean/
%{_datadir}/sounds/ocean/*
