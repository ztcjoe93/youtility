import logging
import sys

class Youtility:
    '''Utility class that contains commonly used functions'''

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
