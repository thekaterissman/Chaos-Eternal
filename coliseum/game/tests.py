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

    def test_game_sequence(self):
        """Test a sequence of game actions to verify the game loop and state changes."""
        # Initial state check
        self.assertEqual(self.player_profile.score, 0)
        self.assertEqual(self.player_profile.current_mode, 'hunter')

        # Action 1: A standard action in hunter mode
        self.client.post(self.home_url, {'action': 'fight'})
        self.player_profile.refresh_from_db()
        self.assertGreater(self.player_profile.score, 0)

        # Action 2: Switch to therapy mode
        self.client.post(self.home_url, {'action': 'switch_mode therapy'})
        self.player_profile.refresh_from_db()
        self.assertEqual(self.player_profile.current_mode, 'therapy')

        # Action 3: Perform a therapy-specific action
        score_before_therapy = self.player_profile.score
        self.client.post(self.home_url, {'action': 'create with golden light'})
        self.player_profile.refresh_from_db()
        self.assertEqual(self.player_profile.score, score_before_therapy + 5)

        # Action 4: Switch back to hunter mode
        self.client.post(self.home_url, {'action': 'switch_mode hunter'})
        self.player_profile.refresh_from_db()
        self.assertEqual(self.player_profile.current_mode, 'hunter')

        # Action 5: Use a special ability
        score_before_ability = self.player_profile.score
        response = self.client.post(self.home_url, {'action': 'use ability'})
        self.player_profile.refresh_from_db()
        self.assertContains(response, "special ability")
        self.assertGreater(self.player_profile.score, score_before_ability)


class LightTherapyTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.username = 'therapist'
        self.password = 'a-very-calm-password-456!'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_switch_to_therapy_mode(self):
        """Test that a player can switch to therapy mode and see suggested actions."""
        response = self.client.post(self.home_url, {'action': 'switch_mode therapy'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Current Mode:</strong> Therapy")
        self.assertContains(response, "Therapy Mode Suggestions:")
        self.assertContains(response, "Create with golden light")

    def test_light_therapy_actions(self):
        """Test that therapy-specific actions produce the correct messages."""
        # First, switch to therapy mode
        self.client.post(self.home_url, {'action': 'switch_mode therapy'})

        # Test a create action
        response = self.client.post(self.home_url, {'action': 'create with blue light'})
        self.assertContains(response, "You weave blue light into the form of")

        # Test a reflect action
        response = self.client.post(self.home_url, {'action': 'reflect on my aura'})
        self.assertContains(response, "You look inward, sensing your aura.")