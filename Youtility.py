import logging
import sys
import time
import typing

def initialize_logger(name: str = None, debug_level: int = 10,
    filename: str = 'debug.log', console_logging: bool = True,
    file_logging: bool = True, file_arguments: dict = {}) -> logging.Logger:
    """A detailed generic logger that can be further configured.

    Returns a pre-configured logger that has common settings, but can be
    further configured if required by specifying required parameters.

    Args:
        name: Name of the logger.
        debug_level: Debug level for the logger, takes in values in intervals of 10
            from 0 to 50.
        filename: Name of the log file.
        console_logging: Enable log records to be displayed in the console.
        file_logging: Enable log records to be saved into a log file.
        file_arguments: Keyword arguments for the file handler.

    Returns:
        A Logger class that can be utilized.
    """

    logger = logging.getLogger(name)
    logger.setLevel(debug_level)
    # https://stackoverflow.com/questions/6729268/log-messages-appearing-twice-with-python-logging#answer-44426266
    logger.propagate = False

    file_handler = logging.FileHandler(filename, **file_arguments)
    console_handler = logging.StreamHandler(sys.stdout)

    for handler in [file_handler, console_handler]:
        handler.setLevel(debug_level)
        handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(threadName)s] %(filename)s.%(funcName)-20s %(levelname)s  %(message)s'
        ))

    if file_logging:
        logger.addHandler(file_handler)

    if console_logging:
        logger.addHandler(console_handler)

    return logger

def timer(fn: typing.Callable) -> typing.Callable:
    """A decorator to measure time performance of functions (garbage-collected).

    Returns the return value of the provided function, if any. 

    Args:
        fn: Function to start the timer on, can pass in args/kwargs
    """

    def time_taken(*args, **kwargs):
        logger = initialize_logger(name="Performance Timer")
        start_time = time.perf_counter()
        return_value = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        logger.info("Time taken for {0}: {1:0.3f}s".format(fn.__name__, time_taken))
        return return_value

    return time_taken

