import os

def format_authors(authors: list, include_urls: bool = False) -> str:
    return ', '.join(
        f'<a href="{author["external_urls"]["spotify"]}">{author["name"]}</a>'
        if include_urls else author['name']
        for author in authors 
    )