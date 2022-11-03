from Youtility import *
import os


def test_logger_outputs_to_console(capsys):
    # https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function
    logger = initialize_logger(name='test_logger_outputs_to_console', file_logging=False)

    logger.info('test logging message')
    console_value = capsys.readouterr().out

    assert 'test logging message' in console_value

def test_logger_outputs_to_file():
    assert os.path.exists('test_debug.log') == False

    # Have to use a different logger name as logging.shutdown() is only called atexit
    # https://docs.python.org/3/library/logging.html#logging.shutdown
    logger = initialize_logger(name='test_logger_outputs_to_file', 
        filename='test_debug.log', file_arguments={'mode': 'w'})

    logger.info('test logger outputs to file')
    assert os.path.exists('test_debug.log') == True

    with open('test_debug.log', 'r') as file:
        lines = file.readline()
        assert 'test logger outputs to file' in lines
    
    os.remove('test_debug.log')


def test_timer(capsys):

    @timer
    def dummy_function():
        time.sleep(1)
    
    dummy_function()
    assert 'Time taken for dummy_function' in capsys.readouterr().out