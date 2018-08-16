from colorama import Fore, Style

# todo if coloring doesn't work on an os, just add WARNING or EXCEPTION tags in front of each stuff

class ConditionalPrint(object):

    def __init__(self, condition, exception_condition, warning_condition, leading_tag= None):
        # init(autoreset=True)  # reset color back to standard after each line print
        self._condition = condition
        self._exception_condition = exception_condition
        self._warning_condition = warning_condition
        if leading_tag is not None:
            self._leading_tag = leading_tag+":"
        else:
            self._leading_tag = None

    def print(self, *args):
        if self._condition is True:
            if self._leading_tag is not None:
                print(self._leading_tag,*args)
            else:
                print(*args)

    def printex(self, *args):

        if self._condition is True or self._exception_condition is True:
            if self._leading_tag is not None:
                print(self._leading_tag, Fore.RED, *args, Style.RESET_ALL)
            else:
                print(Fore.RED, *args, Style.RESET_ALL)

    def printw(self, *args):

        if self._condition is True or self._warning_condition is True:
            if self._leading_tag is not None:
                print(self._leading_tag, Fore.YELLOW, *args, Style.RESET_ALL)
            else:
                print(Fore.YELLOW, *args, Style.RESET_ALL)
