%global tl_name mahjong
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Typeset Mahjong Tiles using MPSZ Notation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/mahjong
License:	mit cc-by-1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mahjong.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mahjong package provides a LaTeX2e and LaTeX3 interface for
typesetting mahjong tiles using an extended version of MPSZ algebraic
notation. Features include spaces, rotated, blank, and concealed tiles,
as well as red fives. The size of the mahjong tiles can be controlled
using a package option and an optional argument of \mahjong. It is
primarily aimed at Riichi (aka. Japanese) Mahjong but can be used to
typeset any style of mahjong.

