from textx import metamodel_from_file
import textx.scoping
import textx.scoping.tools as tools
import os
from textx_ls_core.languages import LanguageTemplate

_mm_types = None


def get_metamodel_types():
    global _mm_types
    return _mm_types


def _library_init():
    global _mm_types, _mm_data, _mm_flow
    global_repo = True
    current_dir = os.path.dirname(__file__)
    p = os.path.join(current_dir, 'Types.tx')
    _mm_types = metamodel_from_file(p,
                                    global_repository=global_repo)
    textx.scoping.MetaModelProvider.add_metamodel("*.type", _mm_types)

    def check_type(t):
        if t.name[0].isupper():
            raise textx.exceptions.TextXSyntaxError(
                "types must be lowercase",
                **tools.get_location(t)
            )

    _mm_types.register_obj_processors({
        'Type': check_type
    })


class TypesDslLang(LanguageTemplate):

    def __init__(self):
        super(TypesDslLang, self).__init__(auto_load_mm=False)

        self._metamodel = get_metamodel_types()

    @property
    def extensions(self):
        return ['type']

    @property
    def language_name(self):
        return 'types_dsl'


_library_init()
