import logging

class log_generator_class:
    @staticmethod
    def log_generation_method():
        log_file=logging.FileHandler(".\\Logs\\Credkart_automation_testing.log")
        log_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
        log_file.setFormatter(log_format)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger
