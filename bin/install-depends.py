import pathlib
import sys


sys.path.append(
    pathlib.Path(__file__).absolute().parent.parent.__str__()
)


from launch import prepare_environment



prepare_environment()
