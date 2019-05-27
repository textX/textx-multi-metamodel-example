from __future__ import unicode_literals
import pytest
from pytest import raises
import os
from textx import (metamodel_for_language,
                   clear_language_registrations)
from textx.scoping.tools import get_unique_named_object


current_dir = os.path.dirname(__file__)


@pytest.fixture(scope='module')
def clear_all():
    clear_language_registrations()


def test_json_ref_dsl(clear_all):
    mm = metamodel_for_language('json-ref-dsl')
    current_dir = os.path.dirname(__file__)
    my_model = mm.model_from_file(os.path.join(current_dir,
                                               'models',
                                               'ok.jref3'))

    # check that the references are OK
    A1_name = get_unique_named_object(my_model, "A1").pyattr
    assert A1_name == "pierre"
    A2_gender = get_unique_named_object(my_model, "A2").pyattr
    assert A2_gender == "male"


def test_json_ref_dsl_bad_attribute(clear_all):
    mm = metamodel_for_language('json-ref-dsl')
    current_dir = os.path.dirname(__file__)
    with raises(Exception, match=r'.*noname.*'):
        mm.model_from_file(os.path.join(current_dir,
                                        'models',
                                        'noname.jref3'))


def test_json_ref_dsl_bad_filename(clear_all):
    mm = metamodel_for_language('json-ref-dsl')
    current_dir = os.path.dirname(__file__)
    with raises(Exception, match=r'.*filenotfound.*'):
        mm.model_from_file(os.path.join(current_dir,
                                        'models',
                                        'filenotfound.jref3'))
