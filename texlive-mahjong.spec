Name:		texlive-mahjong
Version:	58896
Release:	1
Summary:	Typeset Mahjong Tiles using MPSZ Notation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mahjong
License:	mit cc-by-1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The mahjong package provides a LaTeX2e and LaTeX3 interface for
typesetting mahjong tiles using an extended version of MPSZ
algebraic notation. Features include spaces, rotated, blank,
and concealed tiles, as well as red fives. The size of the
mahjong tiles can be controlled using a package option and an
optional argument of \mahjong. It is primarily aimed at Riichi
(aka. Japanese) Mahjong but can be used to typeset any style of
mahjong.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mahjong
%{_texmfdistdir}/tex/latex/mahjong
%doc %{_texmfdistdir}/doc/latex/mahjong

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
