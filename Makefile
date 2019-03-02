#! /usr/bin/env make
## author: AL
## Date: 2019 March
## Purpose: This script is to create a fully automated pipeline
## 					of our project
##
## Usage : make report_branch

###################################################
### test branch coverage
###################################################
.PHONY : coverage_br_std_plus
coverage_br_std_plus : CorrPy/test/test_std_plus.py
	coverage run -m --branch pytest -q CorrPy/test/test_std_plus.py
	coverage report -m

.PHONY : coverage_br_corr_plus
coverage_br_corr_plus : CorrPy/test/test_corr_plus.py
	coverage run -m --branch pytest -q CorrPy/test/test_corr_plus.py
	coverage report -m

.PHONY : coverage_br_cov_mx
coverage_br_cov_mx : CorrPy/test/test_cov_mx.py
	coverage run -m --branch pytest -q CorrPy/test/test_cov_mx.py
	coverage report -m

.PHONY : coverage_branch
coverage_branch : CorrPy/test/test_cov_mx.py CorrPy/test/test_corr_plus.py CorrPy/test/test_std_plus.py
	coverage run -m --branch pytest -q CorrPy/test/test_cov_mx.py CorrPy/test/test_corr_plus.py CorrPy/test/test_std_plus.py
	coverage report -m

.PHONY : report_branch
report_branch : coverage_branch
	coverage html -d coverage_html


###################################################
### test statement coverage
###################################################
.PHONY : coverage_std_plus
coverage_std_plus : CorrPy/test/test_std_plus.py
	coverage run -m --branch pytest -q CorrPy/test/test_std_plus.py
	coverage report -m

.PHONY : coverage_corr_plus
coverage_corr_plus : CorrPy/test/test_corr_plus.py
	coverage run -m --branch pytest -q CorrPy/test/test_corr_plus.py
	coverage report -m

.PHONY : coverage_cov_mx
coverage_cov_mx : CorrPy/test/test_cov_mx.py
	coverage run -m --branch pytest -q CorrPy/test/test_cov_mx.py
	coverage report -m

.PHONY : coverage_statement
coverage_statement : CorrPy/test/test_cov_mx.py CorrPy/test/test_corr_plus.py CorrPy/test/test_std_plus.py
	coverage run -m pytest -q CorrPy/test/test_cov_mx.py CorrPy/test/test_corr_plus.py CorrPy/test/test_std_plus.py
	coverage report -m
