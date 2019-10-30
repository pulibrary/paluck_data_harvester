from api.scopus_searcher import ScopusSearcher

if __name__ == "__main__":
    searcher = ScopusSearcher()
    results = searcher.search()  # defaults to query.txt
    print(results)  # TODO: dump to CSV
