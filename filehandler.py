import os
import shutil


class FileHandler(object):
    """
    Utility class for performing various default file operations.

    """

    @staticmethod
    def delete_directory_tree(path):
        if os.path.exists(path):
            shutil.rmtree(path)


    @staticmethod
    def create_directory_tree(path):
        if not os.path.exists(path):
            os.makedirs(path)