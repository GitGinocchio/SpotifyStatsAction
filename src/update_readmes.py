from argparse import ArgumentParser, Namespace
from jinja2 import Environment, FileSystemLoader
from auth import get_spotify
from utils import *
import re

env = Environment(loader=FileSystemLoader('templates/markdown'))

spotify = get_spotify()

def validate_args(args : Namespace):
    assert os.path.exists(f'templates/markdown/{args.last_played_template}')
    assert os.path.exists(f'templates/markdown/{args.top_artists_template}')
    assert os.path.exists(f'templates/markdown/{args.most_played_template}')

    assert args.num_top_artists > 0 and args.num_top_artists <= 20
    assert args.num_last_played_songs > 0 and args.num_last_played_songs <= 50
    assert args.num_most_played_songs > 0 and args.num_most_played_songs <= 20

def update_section(readme_path : str, section_name : str, content : str):
    begin_marker = f"<!-- BEGIN SPOTIFY STATS: {section_name} -->"
    end_marker = f"<!-- END SPOTIFY STATS: {section_name} -->"

    with open(readme_path, 'r') as file:
        readme_content = file.read()
    
    pattern = rf'{re.escape(begin_marker)}.*?{re.escape(end_marker)}'

    updated_content = re.sub(
        pattern,
        f'{begin_marker}\n{content}\n{end_marker}',
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, 'w') as file:
        file.write(updated_content)



def update_user_last_played_songs(readme_path : str, args : Namespace):
    recent_songs : list = spotify.current_user_recently_played(limit=args.num_last_played_songs)['items']

    template = env.get_template(args.last_played_template)

    content = template.render(
      	username=spotify.me()['display_name'],
        user_page_url=spotify.me()['external_urls']['spotify'],
        recent_songs=recent_songs,
        format_authors=format_authors
    )

    update_section(readme_path,"LAST PLAYED SONGS",content)

def update_user_top_artists(readme_path : str, args : Namespace):
    top_artists = spotify.current_user_top_artists(limit=args.num_top_artists)['items']

    template = env.get_template(args.top_artists_template)

    content = template.render(
      	username=spotify.me()['display_name'],
        user_page_url=spotify.me()['external_urls']['spotify'],
        top_artists=top_artists
    )

    update_section(readme_path,"TOP ARTISTS",content)

def update_user_most_played_songs(readme_path : str, args : Namespace):
    top_songs = spotify.current_user_top_tracks(limit=args.num_most_played_songs)['items']

    template = env.get_template(args.most_played_template)

    content = template.render(
      	username=spotify.me()['display_name'],
        user_page_url=spotify.me()['external_urls']['spotify'],
        top_songs=top_songs,
        format_authors=format_authors
    )

    update_section(readme_path,"MOST PLAYED SONG",content)



def main(args : Namespace) -> None:
    readme_list = str(args.readme_list).split(',')

    for readme in readme_list:
        if args.update_last_played:
            update_user_last_played_songs(readme,args)
        
        if args.update_top_artists:
            update_user_top_artists(readme,args)

        if args.update_most_played:
            update_user_most_played_songs(readme,args)


if __name__ == '__main__':
    parser = ArgumentParser()
    # GENERAL ARGS
    parser.add_argument(
        "--readme-list",
        dest="readme_list",
        help="A list of comma separated paths to the READMEs files to be updated",
        default="README.md"
    )
    
    # UPDATE LAST PLAYED SONGS ARGS
    parser.add_argument(
        "--update-last-played-songs",
        dest="update_last_played",
        help="Whether to update the recently played songs section",
        action='store_true'
    )

    parser.add_argument(
        "--last-played-songs-template-path",
        dest="last_played_template",
        help="The path of the template to use",
        default="last_played_songs.md"
    )

    parser.add_argument(
        "--last-played-songs-to-show",
        dest="num_last_played_songs",
        help="How many recently listened songs to show",
        default=5,
        type=int
    )

    # UPDATE USER TOP ARTISTS ARGS
    parser.add_argument(
        "--update-user-top-artists",
        dest="update_top_artists",
        help="Whether to update the user top artists section",
        action='store_true'
    )

    parser.add_argument(
        "--user-top-artists-template-path",
        dest="top_artists_template",
        help="The path of the template to use",
        default="user_top_artists.md"
    )

    parser.add_argument(
        "--user-top-artists-num-of-artists-to-show",
        dest="num_top_artists",
        help="How many top artists to show",
        default=5,
        type=int
    )

    # UPDATE USER MOST PLAYED SONGS ARGS
    parser.add_argument(
        "--update-user-most-played-songs",
        dest="update_most_played",
        help="Whether to update the user most played songs section",
        action='store_true'
    )

    parser.add_argument(
        "--user-most-played-template-path",
        dest="most_played_template",
        help="The path of the template to use",
        default="user_most_played.md"
    )

    parser.add_argument(
        "--most-played-songs-to-show",
        dest="num_most_played_songs",
        help="How many most played songs to show",
        default=5,
        type=int
    )



    args = parser.parse_args()

    # Args Validations
    validate_args(args)

    # Update READMEs
    main(args)