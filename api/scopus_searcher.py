from csv import DictWriter
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from os import environ
from os.path import abspath, dirname, join
from re import split

#
# TODO: We may need an insttoken; not sure
#
# Some basic examples here:
#   https://github.com/ElsevierDev/elsapy/blob/master/exampleProg.py
#

DEFAULT_CSV_FIELDS = (
    "dc:creator",
    "dc:title",
    "prism:coverDate",
    "prism:doi",
    "prism:issn",
    "prism:issueIdentifier",
    "prism:publicationName",
    "prism:url",
    "prism:volume",
    "prism:aggregationType",
    "subtypeDescription",
    "openaccessFlag",
)


class ScopusSearcher:
    """Class for further encapulation of elsapy and the Elsevier API.
    """

    def __init__(self):
        """Initialize a ScopusSearcher instance.

        Raises:
            KeyError if ELSEVIER_API_KEY is not set as an environment variable.
        """
        self.api_key = environ["ELSEVIER_API_KEY"]
        project_dir = abspath(dirname(dirname(__file__)))
        self.queries_dir = join(project_dir, "queries")
        self.data_dir = join(project_dir, "data")

    def _load_query(self, query_name):
        """Loads a query from the queries directory.

        Args:
            query_name (str): the name of the file in the ./queries/ directory
                that contains the query.

        Returns:
            str: The contents of the file as a string with whitespace
                normalized.
        """
        query_path = join(self.queries_dir, query_name)
        with open(query_path) as f:
            query_string = ScopusSearcher.normalize_whitepace(f.read())
        return query_string

    @staticmethod
    def normalize_whitepace(s):
        """Collapse whitespace and newlines down to single spaces.

        Args:
            s (str): the string to be normalized

        Returns:
            str: the normalized string
        """
        return " ".join(split("\s+", s))

    def search(self, query_name):
        """Do a search.

        Args:
            query_name (str): the name of the file in the ./queries/ directory
                that contains the query. Defaults to "query.txt".

        Raises:
            FileNotFoundError if the file query file can not be found.

        Returns:
            list: The results.
        """
        query = self._load_query(query_name)
        client = ElsClient(self.api_key)
        search = ElsSearch(query, "scopus")
        search.execute(client)
        return search.results

    def dump_results(self, results, file_name, fieldnames=DEFAULT_CSV_FIELDS):
        """Dumps results to a CSV file

        Args:
            results (list): the results of call to #search
            file_name (str): the name of the file to which the results should
                be written. The file will be in ./data. _NOTE_ that the file
                will be overwritten.
            fieldnames (list): A list of fields to write to the file.

        Returns:
            None
        """
        file_path = join(self.data_dir, file_name)
        with open(file_path, "w") as csvf:
            args = {
                "extrasaction": "ignore",
                "restval": "none",
                "fieldnames": fieldnames,
                "dialect": "unix",
            }
            writer = DictWriter(csvf, **args)
            writer.writeheader()
            [writer.writerow(r) for r in results]
