import logging
import sys

import traad.app
from traad.plugin import RopeWorkspacePlugin


log = logging.getLogger('traad.server')


def run_server(project_path, app, port):
    host = 'localhost'

    log.info('Python version: {}'.format(sys.version))

    log.info(
        'Running traad server for app "{}" at {}:{}'.format(
            app,
            host,
            port))

    workspace_plugin = RopeWorkspacePlugin(project_path)
    app.install(workspace_plugin)
    app.run(host=host, port=port)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Run a traad server.')

    parser.add_argument(
        '-p, --port', metavar='N', type=int,
        dest='port', default=0,
        help='the port on which the server will listen. '
             '(0 selects an unused port.)')

    parser.add_argument(
        '-V, --verbosity', metavar='N', type=int,
        dest='verbosity', default=0,
        help='Verbosity level (0=normal, 1=info, 2=debug).')

    parser.add_argument(
        'project', metavar='P', type=str,
        help='the directory containing the project to serve')

    args = parser.parse_args()

    # Configure logging
    level = {
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG
    }[args.verbosity]

    logging.basicConfig(
        level=level)

    log.info('Project root: %s', args.project)

    run_server(args.project,
               traad.app.app,
               args.port)


if __name__ == '__main__':
    main()
