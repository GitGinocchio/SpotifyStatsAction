

def format_authors(authors: list) -> str:
    return ', '.join(author['name'] for author in authors)