from setuptools import setup, find_packages

setup(name='types_data_flow_dsls',
      version='0.1',
      description='(example)',
      url='',
      author='YOUR NAME',
      author_email='YOUR.NAME@ADDRESS',
      license='TODO',
      packages=find_packages(),
      package_data={'': ['*.tx']},
      install_requires=["textx", "arpeggio"],
      tests_require=[
          'pytest',
      ],
      keywords="parser meta-language meta-model language DSL",
      entry_points={
        'textx_languages': [
            'flow_dsl_s = types_data_flow_dsls:flow_dsl_s',
            'data_dsl_s = types_data_flow_dsls:data_dsl_s',
            'types_dsl_s = types_data_flow_dsls:types_dsl_s',
          ],
        'textx_generators': [
              'flow_dsl_s_plantuml=types_data_flow_dsls.generators:flow_pu',
          ]
      },
      )
