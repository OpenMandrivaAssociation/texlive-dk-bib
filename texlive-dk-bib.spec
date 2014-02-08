# revision 15878
# category Package
# catalog-ctan /biblio/bibtex/contrib/dk-bib
# catalog-date 2009-09-25 22:54:35 +0200
# catalog-license other-free
# catalog-version 0.6
Name:		texlive-dk-bib
Version:	0.6
Release:	3
Summary:	Danish variants of standard BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/dk-bib
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) and the apalike style file into
Danish. The files have been extended with URL, ISBN, ISSN,
annote and printing fields which can be enabled through a LaTeX
style file. Dk-bib also comes with a couple of Danish sorting
order files for BibTeX8.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/dk-bib/litteratur.bib
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-abbrv.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-alpha.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-apali.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-plain.bst
%{_texmfdistdir}/bibtex/bst/dk-bib/dk-unsrt.bst
%{_texmfdistdir}/bibtex/csf/dk-bib/88591-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/cp850-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/mac-dk.csf
%{_texmfdistdir}/bibtex/csf/dk-bib/utf8-dk.csf
%{_texmfdistdir}/tex/latex/dk-bib/dk-apali.sty
%{_texmfdistdir}/tex/latex/dk-bib/dk-bib.sty
%doc %{_texmfdistdir}/doc/latex/dk-bib/COPYRIGHT
%doc %{_texmfdistdir}/doc/latex/dk-bib/README
%doc %{_texmfdistdir}/doc/latex/dk-bib/dk-bib.ltx
%doc %{_texmfdistdir}/doc/latex/dk-bib/dk-bib.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dk-bib/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6-2
+ Revision: 751002
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6-1
+ Revision: 718239
- texlive-dk-bib
- texlive-dk-bib
- texlive-dk-bib
- texlive-dk-bib

