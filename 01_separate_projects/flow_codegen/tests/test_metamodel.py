from __future__ import unicode_literals
import os
from textx.cli import textx
from click.testing import CliRunner


this_folder = os.path.abspath(os.path.dirname(__file__))


def test_flow_dsl():
    fname = os.path.join(this_folder,
                         'models', 'data_flow.pu')
    try:
        os.remove(fname)
    except OSError:
        pass

    model_file = os.path.join(this_folder,
                              'models', 'data_flow.eflow')
    assert os.path.exists(model_file)

    runner = CliRunner()
    result = runner.invoke(textx, ['generate',
                                   '--target', 'PlantUML',
                                   '--overwrite', model_file])
    assert result.exit_code == 0
    assert 'Generating PlantUML target from models' in result.output
    assert '->' in result.output
    assert 'models/data_flow.pu' in result.output

    assert os.path.exists(fname)
    txt = open(fname, 'r').read()
    assert txt == """@startuml
component A1
component A2
A1 "City" #--# A2
@enduml
"""
