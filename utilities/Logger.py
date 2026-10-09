import logging
import os


class LogGen:

    @staticmethod
    def loggen():

        os.makedirs("Logs", exist_ok=True)

        logger = logging.getLogger("LUZO")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "Logs/log_file.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger