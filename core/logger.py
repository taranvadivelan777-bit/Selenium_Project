
import logging, os
def get_logger(name='demo'):
    logs = os.path.join(os.getcwd(), 'reports', 'logs')
    os.makedirs(logs, exist_ok=True)
    fn = os.path.join(logs, 'run.log')
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(fn)
        fh.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(fh)
    return logger
