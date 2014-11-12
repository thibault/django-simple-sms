test:
	flake8 djsms --ignore=E501
	coverage run --branch --source=djsms `which django-admin.py` test --settings=djsms.test_settings djsms
	coverage report --omit=djsms/test*

docs:
	cd docs && make html

.PHONY: test docs
