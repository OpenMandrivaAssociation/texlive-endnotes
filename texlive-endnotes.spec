Name:		texlive-endnotes
Version:	53319
Release:	1
Summary:	Place footnotes at the end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endnotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Accumulates footnotes and places them at the end of the
document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endnotes
%doc %{_texmfdistdir}/doc/latex/endnotes

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
