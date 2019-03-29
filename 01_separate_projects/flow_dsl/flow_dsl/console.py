from textx.scoping import MetaModelProvider
import click
import flow_dsl
import textx_inspector

##############################################
#  overrides validate command from types_dsl
##############################################


@click.argument('model_files', nargs=-1)
def inspect(model_files):
    """
    This command inspects *.flow, *.data or *.type-files.
    """
    flow_dsl.get_metamodel_flow()  # activate/register meta model
    root = None
    for filename in model_files:
        try:
            mm = MetaModelProvider.get_metamodel(None, filename)
            m = mm.model_from_file(filename)
            root = textx_inspector.inspect(m, root, False)
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))
    if root is not None:
        root.mainloop()


@click.argument('model_files', nargs=-1)
def validate(model_files):
    """
    This command validates *.flow, *.data or *.type-files.
    """
    flow_dsl.get_metamodel_flow()  # activate/register meta model
    for filename in model_files:
        try:
            print('validating flow/types/data dsl {}'.format(filename))
            mm = MetaModelProvider.get_metamodel(None, filename)
            mm.model_from_file(filename)
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))
