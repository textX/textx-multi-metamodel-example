from setuptools import setup, find_packages

setup(name='data_dsl',
      version='0.1',
      description='(example)',
      url='',
      author='YOUR NAME',
      author_email='YOUR.NAME@ADDRESS',
      license='TODO',
      packages=find_packages(),
      package_data={'': ['*.tx']},
      install_requires=["textx", "arpeggio", "click", "types_dsl"],
      tests_require=[
          'pytest',
      ],
      keywords="parser meta-language meta-model language DSL",
      entry_points={
          'types_data_flow_dslc_commands': [
              'data_dsl_validate=data_dsl.console:validate',
          ]
      },
      )
