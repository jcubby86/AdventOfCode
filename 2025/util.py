import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_lines(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.readlines()]
    return []

def read_comma_separated(fileName: str) -> list:
    with open(fileName, "r") as f:
        return [x.strip() for x in f.read().split(",")]
    return []

def parse_args(args: list):
    verbose = False
    filename = None
    for arg in args[1:]:
        if arg in ["-v", "--verbose"]:
            verbose = True
        else:
            filename = arg
    return verbose, filename

def track_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Function {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper