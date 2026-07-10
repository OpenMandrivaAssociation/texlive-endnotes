%global tl_name endnotes
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Place footnotes at the end
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/endnotes
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Accumulates notes (using the \endnote command, which can be used as a
replacement for \footnote), and places them at the end of the section,
chapter or document.

