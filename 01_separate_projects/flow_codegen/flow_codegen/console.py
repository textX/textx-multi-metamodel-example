from textx.scoping import MetaModelProvider
import click
import flow_codegen
from flow_dsl import get_metamodel_flow


@click.argument('model_files', nargs=-1)
def codegen_flow_pu(model_files):
    """
    This command transforms *.flow-files to *.pu files (plantuml).
    """
    mm_flow = get_metamodel_flow()  # activate/register dsl
    for filename in model_files:
        try:
            mm = MetaModelProvider.get_metamodel(None, filename)
            if mm == mm_flow:
                print('transforming {}'.format(filename))
                m = mm.model_from_file(filename)
                txt = flow_codegen.codegen(m)
                with open(filename+".pu", "w") as f:
                    f.write(txt)
            else:
                raise Exception("no code generator defined for metamodel {}".
                                format(mm))
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))
