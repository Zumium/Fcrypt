from setuptools import setup

setup(
	name="fcrypt",
	version="1.3",
	license="http://www.gnu.org/licenses/gpl",
	description="A simple file encrypt/decrypt tool",
	author='Zumium',
	author_email='martin007323@gmail.com',
	url='https://github.com/Zumium/Fcrypt',
	packages=['Fcrypt'],
	package_data={
		'Fcrypt':['README.md','COPYING']
	},
	entry_points="""
	[console_scripts]
	fcrypt=Fcrypt.inter:main
	""",
	classifiers=[
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4'
	],
)
	
