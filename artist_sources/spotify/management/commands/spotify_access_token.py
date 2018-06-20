import spotipy.util as util
from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        username = options['username']
        token = util.prompt_for_user_token(username, scope='playlist-read-private user-library-read user-follow-read')
        print(token)
