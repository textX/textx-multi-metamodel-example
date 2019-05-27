import os
from textx import metamodel_from_file, language, get_model
from textx.exceptions import TextXSemanticError


@language('json-ref-dsl', '*.jref3')
def json_ref_dsl():
    global_repo = True
    current_dir = os.path.dirname(__file__)

    mm = metamodel_from_file(os.path.join(current_dir, 'JsonRef.tx'),
                             global_repository=global_repo)

    def json_scope_provider(obj, attr, attr_ref):
        if not obj.pyobj:
            from textx.scoping import Postponed
            return Postponed()
        if not hasattr(obj.pyobj, "data"):
            import json
            obj.pyobj.data = json.load(open(
                os.path.join(os.path.abspath(os.path.dirname(
                    get_model(obj)._tx_filename)),
                    obj.pyobj.filename)))
        if attr_ref.obj_name in obj.pyobj.data:
            return obj.pyobj.data[attr_ref.obj_name]
        else:
            raise TextXSemanticError("{} not found".format(attr_ref.obj_name))

    mm.register_scope_providers(
        {"Access.pyattr": json_scope_provider})
    return mm
