from types_dsl import get_metamodel_types
import click
import pkg_resources


@click.group()
@click.pass_context
def types_data_flow_dslc(ctx):
    pass


@types_data_flow_dslc.command()
@click.argument('model_files', nargs=-1)
def validate(model_files):
    """
    This command validates *.type-files.
    """
    mm = get_metamodel_types()

    for filename in model_files:
        try:
            print('validating {}'.format(filename))
            mm.model_from_file(filename)
        except BaseException as e:
            print('  WARNING/ERROR: {}'.format(e))


def register_types_data_flow_dslc_subcommands():
    """
    Find and use all DSL sub-commands registered through extension points.
    Extension points for CLI extension are:
    - `types_data_flow_dslc_commands` - for registering top-level commands.
    - `types_data_flow_dslc_command_groups` - for registering command groups.
    """
    # Register direct sub-commands
    global types_data_flow_dslc
    for subcommand in pkg_resources.iter_entry_points(
            group='types_data_flow_dslc_commands'):
        types_data_flow_dslc.command()(subcommand.load())

    # Register sub-command groups
    for subgroup in pkg_resources.iter_entry_points(
            group='types_data_flow_dslc_command_groups'):
        subgroup.load()(types_data_flow_dslc)


# Register sub-commands registered through extension points.
register_types_data_flow_dslc_subcommands()
