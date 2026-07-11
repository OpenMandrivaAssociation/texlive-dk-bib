%global tl_name dk-bib
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6
Release:	%{tl_revision}.1
Summary:	Danish variants of standard BibTeX styles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/dk-bib
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dk-bib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Dk-bib is a translation of the four standard BibTeX style files (abbrv,
alpha, plain and unsrt) and the apalike style file into Danish. The
files have been extended with URL, ISBN, ISSN, annote and printing
fields which can be enabled through a LaTeX style file. Dk-bib also
comes with a couple of Danish sorting order files for BibTeX8.

