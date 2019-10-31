from api.scopus_searcher import ScopusSearcher

if __name__ == "__main__":
    searcher = ScopusSearcher()
    results = searcher.search("query.txt")  # loads from ./queries
    searcher.dump_results(results, "query_results.csv")  # writes to ./data
