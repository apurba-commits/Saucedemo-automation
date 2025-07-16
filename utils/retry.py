import time
import functools

def retry_on_failure(retries=2, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {i+1}/{retries} failed: {e}")
                    last_exc = e
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator
