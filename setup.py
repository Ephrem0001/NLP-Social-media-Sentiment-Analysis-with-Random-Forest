import setuptools

setuptools.setup(
	name = 'preprocess_kgptalkie', #this should be unique
	include_package_data=True,
	version = '0.1.3',
	author = 'Dan energy Interns',
	author_email = 'dan@energy.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
	)
