Summary:	Qt widget for plotting and data visualization
Summary(pl.UTF-8):	Widget do rysowania wykresów i wizualizacji danych dla Qt
Name:		QCustomPlot
Version:	1.3.0
Release:	0.1
License:	GPL v3
Group:		X11/Libraries
Source0:	http://www.qcustomplot.com/release/%{version}/%{name}.tar.gz
# Source0-md5:	03b6d97cf8f0d4eb2902c0805a72e8bd
Source1:	%{name}.cmake
URL:		http://www.qcustomplot.com/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	cmake >= 2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.qch

%description
QCustomPlot is a Qt C++ widget for plotting and data visualization.
This plotting library focuses on making good looking, publication
quality 2D plots, graphs and charts, as well as offering high
performance for realtime visualization applications.

%package        devel
Summary:	Development files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
Header files for QCustomPlot library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki QCustomPlot

%package        doc
Summary:	Documentation and examples for QCustomPlot
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description    doc
Documentation and examples for QCustomPlot

%description doc -l pl.UTF-8
Dokumentacja i przykłady biblioteki QCustomPlot

%prep
%setup -q -n qcustomplot
install -p %{SOURCE1} CMakeLists.txt

%build

install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc changelog.txt
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so

%files doc
%defattr(644,root,root,755)
%doc documentation examples
