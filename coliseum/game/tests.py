from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import PlayerProfile
from django.urls import reverse

class GameAuthTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.user_agreement_url = reverse('user_agreement')
        self.username = 'testuser'
        self.password = 'a-very-strong-password-123!'
        self.email = 'test@example.com'

    def test_signup_view(self):
        """Test that a user can sign up."""
        response = self.client.post(self.signup_url, {
            'username': self.username,
            'email': self.email,
            'password1': self.password,
            'password2': self.password,
            'agree_to_terms': True,
        }, follow=True)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(User.objects.filter(username=self.username).exists())
        user = User.objects.get(username=self.username)
        self.assertTrue(PlayerProfile.objects.filter(user=user).exists())
        self.assertTrue(response.context['user'].is_authenticated)

    def test_signup_requires_agreement(self):
        """Test that signup fails if the user does not agree to the terms."""
        response = self.client.post(self.signup_url, {
            'username': 'testuser2',
            'email': 'test2@example.com',
            'password1': self.password,
            'password2': self.password,
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser2').exists())

    def test_login_view(self):
        """Test that a user can log in."""
        User.objects.create_user(username=self.username, password=self.password)
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        }, follow=True)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout_view(self):
        """Test that a user can log out."""
        User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.home_url)
        response = self.client.get(self.home_url, follow=True)
        self.assertRedirects(response, f'{self.login_url}?next={self.home_url}')


class GameLogicTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.username = 'testplayer'
        self.password = 'playerpass123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)
        self.player_profile = self.user.playerprofile

    def test_game_interaction_updates_profile(self):
        """Test that a player can interact with the game and their profile is updated."""
        initial_score = self.player_profile.score
        response = self.client.post(self.home_url, {'action': 'fight'})
        self.assertEqual(response.status_code, 200)
        self.player_profile.refresh_from_db()
        self.assertNotEqual(self.player_profile.score, initial_score)
        self.assertContains(response, f"Score: {self.player_profile.score}")

    def test_home_view_displays_player_info(self):
        """Test that the home view displays the correct player information."""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Welcome to The Coliseum, {self.username}!")
        self.assertContains(response, f"Score: {self.player_profile.score}")
        self.assertContains(response, f"Level: {self.player_profile.level}")