from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com')
        batman = User.objects.create_user(username='batman', email='batman@dc.com')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com')

        # Create activities
        Activity.objects.create(name='Run', user='ironman')
        Activity.objects.create(name='Swim', user='batman')
        Activity.objects.create(name='Bike', user='wonderwoman')
        Activity.objects.create(name='Yoga', user='spiderman')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Squats', difficulty='Medium')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
