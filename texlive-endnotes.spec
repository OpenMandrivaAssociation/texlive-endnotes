# revision 17197
# category Package
# catalog-ctan /macros/latex/contrib/endnotes
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-endnotes
Version:	20100309
Release:	1
Summary:	Place footnotes at the end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endnotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Accumulates footnotes and places them at the end of the
document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/endnotes/endnotes.sty
%doc %{_texmfdistdir}/doc/latex/endnotes/endnotes.pdf
%doc %{_texmfdistdir}/doc/latex/endnotes/endnotes.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
