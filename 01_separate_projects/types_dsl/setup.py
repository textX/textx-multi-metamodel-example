from setuptools import setup, find_packages

setup(name='types_dsl',
      version='0.1',
      description='(example)',
      url='',
      author='YOUR NAME',
      author_email='YOUR.NAME@ADDRESS',
      license='TODO',
      packages=find_packages(),
      package_data={'': ['*.tx']},
      install_requires=["textx", "arpeggio", "click",
                        "textx_ls_core"],
      tests_require=[
          'pytest',
      ],
      keywords="parser meta-language meta-model language DSL",
      entry_points={
          'console_scripts': [
              'types_data_flow_dslc=types_dsl.console:types_data_flow_dslc',
          ],
          'textxls_langs': [
              'types_dsl = types_dsl:TypesDslLang'
          ]
      },
      )
