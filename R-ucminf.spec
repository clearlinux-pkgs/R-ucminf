#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ucminf
Version  : 1.1.4
Release  : 25
URL      : https://cran.r-project.org/src/contrib/ucminf_1.1-4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ucminf_1.1-4.tar.gz
Summary  : General-Purpose Unconstrained Non-Linear Optimization
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ucminf-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
The algorithm is of quasi-Newton type with BFGS updating of the inverse
             Hessian and soft line search with a trust region type monitoring of the
             input to the line search algorithm. The interface of 'ucminf' is
             designed for easy interchange with 'optim'.

%package lib
Summary: lib components for the R-ucminf package.
Group: Libraries

%description lib
lib components for the R-ucminf package.


%prep
%setup -q -c -n ucminf
cd %{_builddir}/ucminf

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589531404

%install
export SOURCE_DATE_EPOCH=1589531404
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ucminf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ucminf
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ucminf
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ucminf || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ucminf/DESCRIPTION
/usr/lib64/R/library/ucminf/INDEX
/usr/lib64/R/library/ucminf/Meta/Rd.rds
/usr/lib64/R/library/ucminf/Meta/features.rds
/usr/lib64/R/library/ucminf/Meta/hsearch.rds
/usr/lib64/R/library/ucminf/Meta/links.rds
/usr/lib64/R/library/ucminf/Meta/nsInfo.rds
/usr/lib64/R/library/ucminf/Meta/package.rds
/usr/lib64/R/library/ucminf/NAMESPACE
/usr/lib64/R/library/ucminf/R/ucminf
/usr/lib64/R/library/ucminf/R/ucminf.rdb
/usr/lib64/R/library/ucminf/R/ucminf.rdx
/usr/lib64/R/library/ucminf/doc/TR0019.pdf
/usr/lib64/R/library/ucminf/help/AnIndex
/usr/lib64/R/library/ucminf/help/aliases.rds
/usr/lib64/R/library/ucminf/help/paths.rds
/usr/lib64/R/library/ucminf/help/ucminf.rdb
/usr/lib64/R/library/ucminf/help/ucminf.rdx
/usr/lib64/R/library/ucminf/html/00Index.html
/usr/lib64/R/library/ucminf/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ucminf/libs/ucminf.so
/usr/lib64/R/library/ucminf/libs/ucminf.so.avx2
