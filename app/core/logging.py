import logging


# this function is used to set up the logger for the application
def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name) 

    # add handler if not already present
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # create formatter
        formatter = logging.Formatter( 
            # format of the log message
            "[%(asctime)s] %(levelname)s - %(name)s - %(message)s" 
        ) 

        # create console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # add console handler to logger
        logger.addHandler(console_handler)

    return logger