import regex

class RegexUtil(object):
    """
    Utility functions for utilizing regular expressions
    """


    @staticmethod
    def fuzzy_search(pattern, text, err_number=2):
        """
        Fuzzy search wrapper around a regex pattern,
        it returns the best match with least errors (?b)-flag

        :param pattern: regex pattern which will be wrapped
        :param text: string to use for search
        :param err_number: allowed errors which where match is still triggered
        :return: result of regex search
        """
        compiled_wrapper = regex.compile(r"(?b)(?:" + pattern + "){e<=" + str(err_number) + "}")
        result = compiled_wrapper.search(text)
        if result is not None:
            # substitutions, insertions, deletions
            substs, inserts, dels = result.fuzzy_counts
            accumulated_error_count = substs + inserts + dels
            return result, accumulated_error_count
        else:
            return result, 0
