import random
import json  # For saving "memories"

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "AI whispers: Dance for a shield, or get wrecked! Groove time."
            elif twist == 'sandstorm':
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury."
            else:
                return "Floating islands spawn—gravity flips! Stomach drop incoming."
        else:
            return "AI adapts: Basic roar from Leo. Feel it rumble."

    def save_memory(self):
        memory = {'moves': self.player_moves}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos

    def tarot_reading(self):
        cards = {
            'The Fool': 'A new beginning, a leap of faith.',
            'The Magician': 'You have the power to manifest your desires.',
            'The High Priestess': 'Trust your intuition and inner knowledge.',
            'The Empress': 'Nurture your creative side and embrace abundance.',
            'The Emperor': 'Take control of your life with structure and authority.',
            'The Hierophant': 'Seek guidance from tradition and trusted advisors.',
            'The Lovers': 'A choice must be made. Follow your heart.',
            'The Chariot': 'Charge forward with determination and willpower.',
            'Strength': 'You have the inner strength to overcome any obstacle.',
            'The Hermit': 'Take time for introspection and soul-searching.',
            'Wheel of Fortune': 'A turning point is near. Embrace change.',
            'Justice': 'Your actions have consequences. Seek balance and fairness.',
            'The Hanged Man': 'Let go of what no longer serves you. A new perspective awaits.',
            'Death': 'An era is ending. Embrace transformation.',
            'Temperance': 'Find harmony and balance in all things.',
            'The Devil': 'Confront your shadow self and break free from bondage.',
            'The Tower': 'A sudden upheaval will bring truth and liberation.',
            'The Star': 'Hope and inspiration are on the horizon.',
            'The Moon': 'Navigate through your fears and illusions.',
            'The Sun': 'Joy, success, and abundance are yours.',
            'Judgement': 'A time of reckoning and rebirth.',
            'The World': 'You have completed a cycle. Celebrate your achievements.'
        }
        card = random.choice(list(cards.keys()))
        return f"The AI deals a card: {card}. Its meaning: '{cards[card]}'"

    def get_horoscope(self, zodiac_sign):
        # Determine playstyle from recent moves
        attacks = self.player_moves.count('attack')
        dodges = self.player_moves.count('dodge')

        if attacks > dodges and attacks > 2:
            playstyle = 'aggressive'
        elif dodges > attacks and dodges > 2:
            playstyle = 'defensive'
        else:
            playstyle = 'balanced'

        # Dynamic horoscope templates
        horoscope_templates = {
            'Leo': {
                'aggressive': "The heart of the lion beats within you, fierce and bold! Your recent aggression in the arena has not gone unnoticed by the cosmos. The stars advise you to temper your fury with wisdom, lest your own fire consumes you.",
                'defensive': "A lion's roar is not its only weapon. Your patience and defensive prowess are a shield of cosmic proportions. The stars see a great victory in your future, won not by force, but by cunning and resolve.",
                'balanced': "You walk the path of the king, Leo, with a balanced heart and a steady hand. The stars see your potential for greatness. Continue to lead with both courage and compassion, and your kingdom will flourish."
            },
            'Taurus': {
                'aggressive': "The bull's charge is a fearsome sight, but even the strongest horns can be broken. Your aggressive spirit is a great asset, but the stars warn you to choose your battles wisely. A strategic retreat is not a defeat.",
                'defensive': "You are the unmovable mountain, Taurus, a bastion of defense in the chaotic arena. The stars admire your resilience. A great treasure will soon be within your grasp, if you have the patience to wait for the opportune moment.",
                'balanced': "The earth provides for those who respect its strength. Your balanced approach to combat is a testament to your wisdom. The stars see a future of great abundance for you, both in victory and in peace."
            },
            'Scorpio': {
                'aggressive': "The scorpion's sting is swift and deadly, and your recent actions have proven it. The stars see a path to glory paved with the husks of your enemies, but they also warn of the poison of obsession. Do not lose yourself in the thrill of the hunt.",
                'defensive': "A true predator knows when to lie in wait. Your defensive tactics are a masterclass in cunning. The stars whisper of a great secret that will soon be revealed to you, a key to unlocking a power you never knew you possessed.",
                'balanced': "The scorpion's dance is a delicate balance of attack and defense. You have mastered this art, and the stars are pleased. A great alliance is on the horizon, one that will bring you both power and prestige."
            },
            'Libra': {
                'aggressive': "The scales of justice can also be a weapon. Your aggressive pursuit of victory has thrown the arena into disarray. The stars caution you to find your center, for true power lies not in dominance, but in balance.",
                'defensive': "You are a master of a thousand cuts, a defensive artist who turns the enemy's strength against them. The stars see a great masterpiece in your future, a victory so elegant it will be sung by the bards of the cosmos for eons.",
                'balanced': "You are the fulcrum of the arena, the calm in the eye of the storm. Your balanced approach brings harmony to the chaos. The stars see a great destiny for you, one that will shape the future of the Coliseum itself."
            }
        }

        if zodiac_sign in horoscope_templates:
            return horoscope_templates[zodiac_sign][playstyle]
        else:
            return "The stars are silent on this sign. Choose from Leo, Taurus, Scorpio, or Libra."

# Usage:
# brain = AIChaosBrain()
# brain.learn_move('attack')
# brain.learn_move('attack')
# brain.learn_move('attack')
# print(brain.get_horoscope('Leo'))
