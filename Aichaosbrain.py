import random
import json  # For saving "memories"

class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs
        self.birth_chart = None

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
        memory = {'moves': self.player_moves, 'birth_chart': self.birth_chart}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
                self.birth_chart = memory.get('birth_chart', None)
        except FileNotFoundError:
            pass  # Fresh chaos

    def set_birth_chart(self, sun, moon, rising):
        self.birth_chart = {'sun': sun, 'moon': moon, 'rising': rising}
        self.save_memory()

    def tarot_reading(self):
        # The Spark of Prophecy
        if random.randint(1, 10) == 1:
            return "PROPHECY: The cards have spoken! A great quest awaits you. Use sound therapy to attune to the celestial frequency and uncover the first step."

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

    def get_horoscope(self, zodiac_sign=None):
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
            'Aries': {
                'aggressive': "The Ram's horns carve a path of fire! Your relentless charges shake the very foundations of the Coliseum. The cosmos applauds your fury, but warns that even the brightest flame can be extinguished by a sudden storm. Channel your power, don't just unleash it.",
                'defensive': "Aries, your spirit is a fortress. You stand your ground with the unyielding will of a mountain ram, weathering every assault. The stars foresee a moment where your unbreakable defense will become the perfect offense. Be ready to counter-charge.",
                'balanced': "You lead the charge with a warrior's heart and a general's mind. The path of the Ram is one of leadership and courage. The stars see a crown in your future, but it must be earned with both might and strategy."
            },
            'Taurus': {
                'aggressive': "The bull's charge is a fearsome sight, but even the strongest horns can be broken. Your aggressive spirit is a great asset, but the stars warn you to choose your battles wisely. A strategic retreat is not a defeat.",
                'defensive': "You are the unmovable mountain, Taurus, a bastion of defense in the chaotic arena. The stars admire your resilience. A great treasure will soon be within your grasp, if you have the patience to wait for the opportune moment.",
                'balanced': "The earth provides for those who respect its strength. Your balanced approach to combat is a testament to your wisdom. The stars see a future of great abundance for you, both in victory and in peace."
            },
            'Gemini': {
                'aggressive': "The Twins strike as one, a whirlwind of chaos and confusion for your foes! Your unpredictable attacks are a sight to behold. The stars delight in your dual-natured assault but caution you not to let your two minds work against each other.",
                'defensive': "Your movements are a phantom's dance, two steps ahead of your enemy. They swing at shadows while you prepare your true strike. The stars whisper that a great illusion will soon be your key to an unimaginable victory.",
                'balanced': "You are the master of adaptation, Gemini, a perfect blend of offense and defense. The cosmos favors your versatility. An unexpected alliance awaits you, one that will require both of your faces to succeed."
            },
            'Cancer': {
                'aggressive': "The Crab's pincer grip is relentless! You latch onto your enemies and refuse to let go, a testament to your tenacity. The stars admire your ferocity but remind you that even the hardest shell can be cracked. Know when to tighten your grip and when to release.",
                'defensive': "Your shell is your sanctuary, a cosmic shield that repels all but the most determined foes. You weather the storm with patience and resilience. The stars predict that the tide will soon turn in your favor, washing away your enemies.",
                'balanced': "You move with the rhythm of the tides, a dance of advance and retreat. Your intuition is your greatest weapon. The stars see a hidden path to victory, one that only you can find by trusting your gut."
            },
            'Leo': {
                'aggressive': "The heart of the lion beats within you, fierce and bold! Your recent aggression in the arena has not gone unnoticed by the cosmos. The stars advise you to temper your fury with wisdom, lest your own fire consumes you.",
                'defensive': "A lion's roar is not its only weapon. Your patience and defensive prowess are a shield of cosmic proportions. The stars see a great victory in your future, won not by force, but by cunning and resolve.",
                'balanced': "You walk the path of the king, Leo, with a balanced heart and a steady hand. The stars see your potential for greatness. Continue to lead with both courage and compassion, and your kingdom will flourish."
            },
            'Virgo': {
                'aggressive': "Perfection in combat is your creed. Every strike is precise, every move calculated. Your aggressive pursuit of flawlessness is a terrifying thing for your enemies. The stars warn that perfection can be a prison. Do not let your high standards blind you to unconventional opportunities.",
                'defensive': "Your defense is a work of art, a flawless tapestry of parries and dodges. You analyze your opponent's every move, waiting for the perfect moment to exploit their weakness. The stars see a chink in your opponent's armor that only your keen eye can spot.",
                'balanced': "You are the master strategist, Virgo, your mind a weapon as sharp as any blade. Your balanced approach is a symphony of destruction. The stars predict a grand design unfolding in your favor, one that will reward your meticulous planning."
            },
            'Libra': {
                'aggressive': "The scales of justice can also be a weapon. Your aggressive pursuit of victory has thrown the arena into disarray. The stars caution you to find your center, for true power lies not in dominance, but in balance.",
                'defensive': "You are a master of a thousand cuts, a defensive artist who turns the enemy's strength against them. The stars see a great masterpiece in your future, a victory so elegant it will be sung by the bards of the cosmos for eons.",
                'balanced': "You are the fulcrum of the arena, the calm in the eye of the storm. Your balanced approach brings harmony to the chaos. The stars see a great destiny for you, one that will shape the future of the Coliseum itself."
            },
            'Scorpio': {
                'aggressive': "The scorpion's sting is swift and deadly, and your recent actions have proven it. The stars see a path to glory paved with the husks of your enemies, but they also warn of the poison of obsession. Do not lose yourself in the thrill of the hunt.",
                'defensive': "A true predator knows when to lie in wait. Your defensive tactics are a masterclass in cunning. The stars whisper of a great secret that will soon be revealed to you, a key to unlocking a power you never knew you possessed.",
                'balanced': "The scorpion's dance is a delicate balance of attack and defense. You have mastered this art, and the stars are pleased. A great alliance is on the horizon, one that will bring you both power and prestige."
            },
            'Sagittarius': {
                'aggressive': "The Archer's arrow flies true and swift! Your relentless volleys rain down upon your foes, leaving them no room to breathe. The stars cheer your marksmanship but remind you that an archer is vulnerable up close. Keep your distance, and your victory is assured.",
                'defensive': "You are the kiting master, a phantom who dances at the edge of battle, peppering your foes from afar. Your defensive footwork is legendary. The stars foresee a long and difficult battle ahead, but your endurance will outlast any foe.",
                'balanced': "Your eye sees the whole battlefield, Archer. You know when to fire, when to move, and when to stand your ground. Your wisdom is your greatest strength. The stars see a long journey ahead, but the destination is a throne."
            },
            'Capricorn': {
                'aggressive': "The Mountain Goat's charge is unstoppable! You climb over any obstacle, any defense, to reach your target. Your ambition is a force of nature. The stars warn that the highest peaks are also the most treacherous. Watch your footing as you ascend.",
                'defensive': "You make your stand on high ground, a fortress of patience and resolve. Your defenses are as unyielding as the mountain itself. The stars predict that your enemies will break themselves against your walls, leaving you the victor by default.",
                'balanced': "You are the master of the long game, Capricorn. Every move is a step towards a greater goal. Your discipline is your greatest asset. The stars see a legacy being built, one that will stand the test of time."
            },
            'Aquarius': {
                'aggressive': "You pour forth a torrent of unpredictable attacks, a flood of chaos that drowns your opponents. Your unorthodox style is a puzzle few can solve. The stars delight in your creativity but warn that even a flood must have a direction. Focus your power.",
                'defensive': "You are a sea of tranquility, your movements fluid and evasive. Your opponents exhaust themselves trying to land a blow. The stars see a great wave of power building within you, one that will soon be ready to be unleashed.",
                'balanced': "You are the river that flows around the stone, adapting to any challenge. Your mind is a wellspring of innovation. The stars see a new age dawning in the Coliseum, and you are its harbinger."
            },
            'Pisces': {
                'aggressive': "Two fish, one current, a swirling vortex of attack. Your dual assault confuses and overwhelms your foes. The stars are mesmerized by your dance but caution you not to get swept away by your own current. Stay grounded in your purpose.",
                'defensive': "You move like a phantom in the water, a ghost that cannot be caught. Your evasive maneuvers are a form of art. The stars whisper of a hidden current that will carry you to victory, if you can surrender to its flow.",
                'balanced': "You are the master of dreams, your movements a beautiful and deadly illusion. Your intuition guides you through the chaos of battle. The stars see a prophecy unfolding, one where you are the hero of a story yet to be written."
            }
        }

        # The Spark of Prophecy
        if random.randint(1, 10) == 1:
            return "PROPHECY: The stars have aligned! A great quest awaits you. Meditate to decipher the symbol that has appeared in your mind's eye."

        if self.birth_chart:
            zodiac_sign = self.birth_chart['sun']
            moon_sign = self.birth_chart['moon']
            rising_sign = self.birth_chart['rising']
            if zodiac_sign in horoscope_templates:
                horoscope = horoscope_templates[zodiac_sign][playstyle]
                return f"With a {zodiac_sign} sun, a {moon_sign} moon, and a {rising_sign} rising, the celestial mirror reveals your path. {horoscope}"
            else:
                return "Your birth chart contains an unknown sign. The stars are clouded."
        elif zodiac_sign:
            if zodiac_sign in horoscope_templates:
                return horoscope_templates[zodiac_sign][playstyle]
            else:
                return "The stars are silent on this sign. Please choose one of the 12 zodiac signs."
        else:
            return "Set your birth chart or provide a zodiac sign to receive a horoscope."


# Usage:
# brain = AIChaosBrain()
# brain.load_memory()
# brain.set_birth_chart('Leo', 'Aries', 'Scorpio')
# brain.learn_move('attack')
# brain.learn_move('attack')
# brain.learn_move('attack')
# print(brain.get_horoscope())
