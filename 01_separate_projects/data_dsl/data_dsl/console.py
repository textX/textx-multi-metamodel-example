from textx.scoping import MetaModelProvider
import click
import data_dsl


##############################################
#  overrides validate command from types_dsl
##############################################


@click.argument('model_files', nargs=-1)
def validate(model_files):
    """
    This command validates *.data or *.type-files.
    """
    data_dsl.get_metamodel_data()  # activate/register meta model

    for filename in model_files:
        try:
            print('validating types/data dsl {}'.format(filename))
            mm = MetaModelProvider.get_metamodel(None, filename)
            mm.model_from_file(filename)
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))
