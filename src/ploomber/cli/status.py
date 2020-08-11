from ploomber.cli.parsers import _custom_command, CustomParser


def main():
    parser = CustomParser(description='Show pipeline status')
    with parser:
        # this command has no static args
        pass
    dag, args = _custom_command(parser)
    print(dag.status())
