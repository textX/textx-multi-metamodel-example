import os
from textx import (metamodel_from_file, language, TextXSemanticError,
                   TextXSyntaxError)
import textx.scoping.tools as tools
import textx.scoping.providers as scoping_providers


current_dir = os.path.dirname(__file__)


@language('types-dsl-s', '*.etype2')
def types_dsl_s():
    mm_types = metamodel_from_file(os.path.join(current_dir, 'Types.tx'),
                                   global_repository=True)

    def check_type(t):
        if t.name[0].isupper():
            raise TextXSyntaxError(
                "types must be lowercase",
                **tools.get_location(t)
            )

    mm_types.register_obj_processors({
        'Type': check_type
    })

    return mm_types


@language('data-dsl-s', '*.edata2')
def data_dsl_s():
    mm_data = metamodel_from_file(os.path.join(current_dir, 'Data.tx'),
                                  global_repository=True)
    # Note, it is better to share a common repo, instead of having one
    # for each meta model separately.

    mm_data.register_scope_providers(
        {"*.*": scoping_providers.FQNImportURI()})

    return mm_data


@language('flow-dsl-s', '*.eflow2')
def flow_dsl_s():
    mm_flow = metamodel_from_file(os.path.join(current_dir, 'Flow.tx'),
                                  global_repository=True)
    # Note, it is better to share a common repo, instead of having one
    # for each meta model separately.

    mm_flow.register_scope_providers(
        {"*.*": scoping_providers.FQNImportURI()})

    def check_flow(f):
        if f.algo1.outp != f.algo2.inp:
            raise TextXSemanticError(
                "algo data types must match",
                **tools.get_location(f)
            )

    mm_flow.register_obj_processors({
        'Flow': check_flow
    })

    return mm_flow
