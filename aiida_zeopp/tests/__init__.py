""" Sample data needed for tests"""
import os

TEST_DIR = os.path.dirname(os.path.realpath(__file__))


def get_backend():
    from aiida.backends.profile import BACKEND_DJANGO, BACKEND_SQLA
    if os.environ.get('TEST_AIIDA_BACKEND') == BACKEND_SQLA:
        return BACKEND_SQLA
    return BACKEND_DJANGO


def get_zeopp_binary():
    env = os.environ.get('ZEOPP')
    if not env:
        raise ValueError(
            "Provide path to 'network' binary in ZEOPP environment variable before running tests."
        )
    elif not os.path.isfile(env):
        raise ValueError("ZEOPP binary '{}' does not exist.".format(env))
    return env


def get_localhost_computer():
    """Setup localhost computer"""
    from aiida.orm import Computer
    import tempfile
    computer = Computer(
        name='localhost',
        description='my computer',
        hostname='localhost',
        workdir=tempfile.mkdtemp(),
        transport_type='local',
        scheduler_type='direct',
        enabled_state=True)
    return computer


def get_network_code():
    """Setup code on localhost computer"""
    from aiida.orm import Code

    executable = get_zeopp_binary()

    code = Code(
        files=[executable],
        input_plugin_name='zeopp.network',
        local_executable='network')
    code.label = 'zeopp'
    code.description = 'zeo++'

    return code