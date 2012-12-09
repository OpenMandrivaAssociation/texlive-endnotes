# revision 17197
# category Package
# catalog-ctan /macros/latex/contrib/endnotes
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-endnotes
Version:	20100309
Release:	2
Summary:	Place footnotes at the end
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/endnotes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/endnotes.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/endnotes/endnotes.sty
%doc %{_texmfdistdir}/doc/latex/endnotes/endnotes.pdf
%doc %{_texmfdistdir}/doc/latex/endnotes/endnotes.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100309-2
+ Revision: 751419
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100309-1
+ Revision: 718333
- texlive-endnotes
- texlive-endnotes
- texlive-endnotes
- texlive-endnotes

