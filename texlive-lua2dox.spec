# revision 27205
# category Package
# catalog-ctan /web/lua2dox
# catalog-date 2012-07-21 10:40:57 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-lua2dox
Version:	0.1
Release:	2
Summary:	Auto-documentation of lua code
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/web/lua2dox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua2dox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua2dox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-lua2dox.bin = %{EVRD}

%description
The package extends the well-known C-like language autodoc
tool, doxygen, to read and document lua code. In use, you edit
and test your code and periodically run the autodoc tool to
update the documentation, which may be viewed via an html
browser. Autodoc tools can read the code well enough to find
function/... declarations and document them. If the code also
contains appropriatly formatted "magic comments", the tool can
use them to supplement the documentation. The package is a
first prototype of a planned TeX2DoX tool (in development),
which will process joint (La)TeX/lua documents.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/lua2dox_filter
%{_bindir}/lua2dox_lua
%{_texmfdistdir}/scripts/lua2dox/lua.def
%{_texmfdistdir}/scripts/lua2dox/lua2dox.lua
%{_texmfdistdir}/scripts/lua2dox/lua2dox_lua
%doc %{_texmfdistdir}/doc/support/lua2dox/Doxyfile
%doc %{_texmfdistdir}/doc/support/lua2dox/INSTALL
%doc %{_texmfdistdir}/doc/support/lua2dox/README
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/doxygen.css
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/doxygen.png
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/files.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/globals.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/globals_func.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/index.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/lua2dox_8lua-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/lua2dox_8lua.html
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/tab_b.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/tab_l.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/tab_r.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/docs/html/tabs.css
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/Doxyfile
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/animals.lua
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/class.lua
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/animals_8lua-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/animals_8lua.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/annotated.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classAnimal-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classAnimal.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classAnimal.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classBird-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classBird.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classBird.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classCat-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classCat.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classCat.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classDog-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classDog.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classDog.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classMammal-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classMammal.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classMammal.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classPigeon-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classPigeon.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classPigeon.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classRedKite-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classRedKite.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/classRedKite.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/class_8lua-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/class_8lua.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/doxygen.css
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/doxygen.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/files.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/functions.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/functions_func.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/globals.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/globals_func.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/hierarchy.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/index.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/main_8lua-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/main_8lua.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/tab_b.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/tab_l.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/tab_r.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/docs/html/tabs.css
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/lua/main.lua
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/Doxyfile
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/animals.php
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/animals_8php-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/animals_8php.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/annotated.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classAnimal-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classAnimal.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classAnimal.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classBird-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classBird.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classBird.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classCat-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classCat.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classCat.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classDog-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classDog.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classDog.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classMammal-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classMammal.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classMammal.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classPigeon-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classPigeon.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classPigeon.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classRedKite-members.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classRedKite.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/classRedKite.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/doxygen.css
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/doxygen.png
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/files.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/functions.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/functions_func.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/globals.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/globals_func.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/globals_vars.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/hierarchy.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/index.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/main_8php-source.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/main_8php.html
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/tab_b.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/tab_l.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/tab_r.gif
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/docs/html/tabs.css
%doc %{_texmfdistdir}/doc/support/lua2dox/examples/php/main.php
%doc %{_texmfdistdir}/doc/support/lua2dox/install.sh
%doc %{_texmfdistdir}/doc/support/lua2dox/lua2dox-refm.pdf
%doc %{_texmfdistdir}/doc/support/lua2dox/lua2dox-refm.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/lua2dox/lua2dox_lua lua2dox_lua
    ln -sf lua2dox_lua lua2dox_filter
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 813654
- Import texlive-lua2dox
- Import texlive-lua2dox

