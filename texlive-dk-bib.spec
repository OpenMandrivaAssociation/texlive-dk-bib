Name:		texlive-dk-bib
Version:	0.6
Release:	1
Summary:	Danish variants of standard BibTeX styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/dk-bib
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) and the apalike style file into
Danish. The files have been extended with URL, ISBN, ISSN,
annote and printing fields which can be enabled through a LaTeX
style file. Dk-bib also comes with a couple of Danish sorting
order files for BibTeX8.

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
