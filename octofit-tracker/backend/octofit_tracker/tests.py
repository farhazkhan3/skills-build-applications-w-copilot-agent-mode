from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_create_activity(self):
        activity = Activity.objects.create(name='Run', user='ironman')
        self.assertEqual(activity.name, 'Run')
        self.assertEqual(activity.user, 'ironman')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')
        self.assertEqual(leaderboard.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_create_user(self):
        user = get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com')
        self.assertEqual(user.username, 'ironman')
        self.assertEqual(user.email, 'ironman@marvel.com')
