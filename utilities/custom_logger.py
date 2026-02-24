import logging
class log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\logs\\nopcommerce.log",level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger