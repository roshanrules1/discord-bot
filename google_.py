from googlesearch import search


def google(query):
    return list(search(query, tld="co.in", num=5, stop=5, pause=2))
