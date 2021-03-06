import sys, logging
import PyCUST
import PyCUST.settings

log_level = "DEBUG" if PyCUST.settings.debug_mode else "INFO"
log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "CRITICAL": logging.CRITICAL,
}

logger = logging.getLogger(__name__)
logger.setLevel(log_levels[log_level])

if PyCUST.settings.logging_stream_type is "file":
    open(PyCUST.settings.logging_file_name, "w").close()  # clear the log file
    logging_handler = logging.FileHandler(filename=PyCUST.settings.logging_file_name)
elif PyCUST.settings.logging_stream_type is "terminal":
    logging_handler = logging.StreamHandler(stream=sys.stdout)
logging_handler.terminator = "\n"
logging_handler.setLevel(log_levels[log_level])

formatter = logging.Formatter(
    "%(name)s_log %(levelname)s: %(message)s"
)  # default "%(name)s - %(levelname)s - %(message)s - %(asctime)s\n", datefmt="%d-%b-%y %H:%M:%S"
logging_handler.setFormatter(formatter)

logger.addHandler(logging_handler)


def log(message, *args, **kwargs):  # create logging decorator
    def decorator(function):
        def inner(*args, **kwargs):
            logger.info("EVENT: " + message)
            return function(*args, **kwargs)

        return inner

    return decorator
