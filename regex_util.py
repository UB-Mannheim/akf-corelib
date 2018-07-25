import regex

class RegexUtil(object):
    """
    Utility functions for utilizing regular expressions
    """


    @staticmethod
    def fuzzy_search(pattern, text, err_number=2):
        """
        Fuzzy search wrapper around a regex pattern
        :param pattern: regex pattern which will be wrapped
        :param text: string to use for search
        :param err_number: allowed errors which where match is stil triggered
        :return: result of regex search
        """
        compiled_wrapper = regex.compile(r"(?:" + pattern + "){e<=" + str(err_number) + "}")
        result = compiled_wrapper.search(text)
        return result
