import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Entering {func.__name__}")
        result = func(*args, **kwargs)
        logger.info(f"Exiting {func.__name__}")
        return result
    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info(f"Finished in {func.__name__} in {end - start}")
        return result
    return wrapper