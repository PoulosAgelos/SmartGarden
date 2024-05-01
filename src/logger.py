import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
