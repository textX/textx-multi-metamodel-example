from __future__ import unicode_literals
import os
import pytest
from pytest import raises
from textx import (TextXSemanticError, TextXSyntaxError,
                   metamodel_for_language,
                   clear_language_registrations)
from textx.cli import textx
from click.testing import CliRunner


this_folder = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='module')
def clear_all():
    clear_language_registrations()


def test_flow_dsl_generator(clear_all):
    fname = os.path.join(this_folder,
                         'models', 'data_flow.pu')
    try:
        os.remove(fname)
    except OSError:
        pass

    model_file = os.path.join(this_folder,
                              'models', 'data_flow.eflow2')
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


def test_types_dsl(clear_all):
    mmT = metamodel_for_language('types-dsl-s')
    this_folder = os.path.dirname(__file__)
    model = mmT.model_from_file(os.path.join(this_folder,
                                             'models',
                                             'types.etype2'))
    assert(model is not None)
    assert(len(model.types) == 2)


def test_types_dsl_validation(clear_all):
    mmT = metamodel_for_language('types-dsl-s')
    this_folder = os.path.dirname(__file__)
    with raises(TextXSyntaxError,
                match=r'.*lowercase.*'):
        mmT.model_from_file(os.path.join(this_folder,
                                         'models',
                                         'types_with_error.etype2'))


def test_data_dsl(clear_all):
    mmD = metamodel_for_language('data-dsl-s')
    this_folder = os.path.dirname(__file__)
    model = mmD.model_from_file(os.path.join(this_folder,
                                             'models',
                                             'data_structures.edata2'))
    assert(model is not None)
    assert(len(model.data) == 3)


def test_flow_dsl(clear_all):
    mmF = metamodel_for_language('flow-dsl-s')
    this_folder = os.path.dirname(__file__)
    model = mmF.model_from_file(os.path.join(this_folder,
                                             'models',
                                             'data_flow.eflow2'))
    assert(model is not None)
    assert(len(model.algos) == 2)
    assert(len(model.flows) == 1)


def test_flow_dsl_validation(clear_all):
    mmF = metamodel_for_language('flow-dsl-s')
    this_folder = os.path.dirname(__file__)
    with raises(TextXSemanticError,
                match=r'.*algo data types must match.*'):
        mmF.model_from_file(os.path.join(this_folder,
                                         'models',
                                         'data_flow_with_error.eflow2'))
