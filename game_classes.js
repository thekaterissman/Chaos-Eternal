const fs = require('fs');

class ModesManager {
    constructor() {
        this.current_mode = 'hunter';
        this.xp = 0;
        this.shelters = [];
        this.difficulty = 'medium';
    }

    set_difficulty(level) {
        if (['easy', 'medium', 'hard'].includes(level)) {
            this.difficulty = level;
            return `Difficulty set to ${level}.`;
        }
        return "Invalid difficulty level.";
    }

    switch_mode(mode) {
        const modes = ['hunter', 'survival', 'pvp', 'raid', 'therapy'];
        if (modes.includes(mode)) {
            this.current_mode = mode;
            if (mode === 'survival') {
                return "Survival Mode: Craft vines to blades. XP sticks – no resets!";
            } else if (mode === 'pvp') {
                return "PvP: Teams self-select. Mix crews, clash in the arena!";
            } else if (mode === 'raid') {
                return "Raid villages! Steal loot, burn down – haptics make walls crack.";
            } else if (mode === 'therapy') {
                return "Therapy Mode: A peaceful space. No combat, just creation and reflection.";
            } else {
                return "Hunter Mode: Self-pick teams. Hunt or be hunted.";
            }
        }
        return "Invalid mode – chaos only!";
    }

    earn_xp(action) {
        const xp_gain = Math.floor(Math.random() * (50 - 10 + 1)) + 10;
        this.xp += xp_gain;
        if (this.current_mode === 'survival') {
            this.shelters.push('new_shelter');
        }
        return `XP +${xp_gain}! Total: ${this.xp}. Boosts Coliseum skills.`;
    }

    mix_modes(mode1, mode2) {
        return `Mixed: ${mode1} + ${mode2} = Pure dive! Remake world in 5s.`;
    }
}

class AIChaosBrain {
    constructor(modes_manager) {
        this.modes_manager = modes_manager;
        this.player_moves = [];
        this.fears = ['sandstorm', 'floating_islands', 'dance_or_die'];
        this.memory_file = 'chaos_memory.json';
    }

    learn_move(move) {
        this.player_moves.push(move);
        if (this.player_moves.length > 10) {
            this.player_moves = this.player_moves.slice(-10);
        }
        this.save_memory();
    }

    throw_twist() {
        const difficulty = this.modes_manager.difficulty;
        let twist_sensitivity = 3;

        if (difficulty === 'easy') {
            twist_sensitivity = 2;
        } else if (difficulty === 'hard') {
            twist_sensitivity = 4;
        }

        if (this.player_moves.length >= twist_sensitivity && this.player_moves.slice(-twist_sensitivity).includes('dodge')) {
            const twist = this.fears[Math.floor(Math.random() * this.fears.length)];
            if (twist === 'dance_or_die') {
                return "AI whispers: Dance for a shield, or get wrecked! Groove time.";
            } else if (twist === 'sandstorm') {
                return "Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury.";
            } else {
                return "Floating islands spawn—gravity flips! Stomach drop incoming.";
            }
        } else {
            return "AI adapts: Basic roar from Leo. Feel it rumble.";
        }
    }

    save_memory() {
        const memory = { moves: this.player_moves };
        fs.writeFileSync(this.memory_file, JSON.stringify(memory));
    }

    load_memory() {
        try {
            const data = fs.readFileSync(this.memory_file, 'utf8');
            const memory = JSON.parse(data);
            this.player_moves = memory.moves || [];
        } catch (err) {
            // Fresh chaos, no memory file found.
        }
    }
}

class BeastBestiary {
    constructor(modes_manager, coins = 0) {
        this.modes_manager = modes_manager;
        this.coins = coins;
        this.beasts = {
            'leo_lion': { 'cost': 1, 'effect': 'Roar shakes chest – haptic thunder!' },
            'scorpio_sting': { 'cost': 1, 'effect': 'Cosmic slap – buzz in your hand!' },
            'taurus_bull': { 'cost': 2, 'effect': 'Charge forward – ground quakes under feet.' },
            'phoenix': { 'cost': 5, 'effect': 'Rise from plasma – warm glow on skin.' },
            'knight_mount': { 'cost': 10, 'effect': 'Legendary knight: Customize plasma armor, win the Chaos Crown!' },
            'cosmic_whale': { 'cost': 12, 'effect': 'Swim through space-time, singing a low, resonant song.' },
            'shadow_panther': { 'cost': 7, 'effect': 'Meld into the darkness, striking with silent grace.' },
            'giant_eagle': { 'cost': 8, 'effect': 'Soar on cosmic winds, viewing the battlefield from above.' },
            'ice_dragon': { 'cost': 15, 'effect': 'Exhale a blast of frost that crystallizes the air.' },
            'fire_serpent': { 'cost': 14, 'effect': 'Slither through the air, leaving a trail of embers.' },
            'mech_tiger': { 'cost': 11, 'effect': 'A metallic roar echoes as laser claws extend.' },
            'celestial_griffin': { 'cost': 13, 'effect': 'A majestic creature of light and air, its cry inspires allies.' },
            'void_reaver': { 'cost': 18, 'effect': 'A terrifying beast from the abyss, it consumes light.' },
            'ironclad_rhino': { 'cost': 9, 'effect': 'An unstoppable force, its armor plated with starmetal.' }
        };
        this.owned_beasts = [];
    }

    buy_beast(beast_name) {
        if (!this.beasts[beast_name]) {
            return "Beast not found in the bestiary.";
        }

        const base_cost = this.beasts[beast_name].cost;
        const difficulty = this.modes_manager.difficulty;
        let cost_multiplier = 1.0;

        if (difficulty === 'easy') {
            cost_multiplier = 0.8;
        } else if (difficulty === 'hard') {
            cost_multiplier = 1.5;
        }

        const adjusted_cost = Math.floor(base_cost * cost_multiplier);

        if (this.coins >= adjusted_cost) {
            this.coins -= adjusted_cost;
            this.owned_beasts.push(beast_name);
            return `Beast acquired for ${adjusted_cost} coins: ${this.beasts[beast_name].effect} Sons' stars flare!`;
        } else {
            return `Not enough coins, queen. Need ${adjusted_cost}, have ${this.coins}. Raid a village!`;
        }
    }

    ride_beast(beast_name) {
        if (this.owned_beasts.includes(beast_name)) {
            const zodiac_boost = ['Leo roars', 'Scorpio stings', 'Libra balances'][Math.floor(Math.random() * 3)];
            return `Riding ${beast_name}! ${zodiac_boost} – feel the jolt in your spine.`;
        }
        return "No beast? Buy one first!";
    }
}

class Kate {
    constructor() {
        this.name = "Kate";
        this.trait = "Fiery and Unstoppable";
    }

    special_ability() {
        return "Kate's scepter glows! A Phoenix of pure plasma erupts, its cry a searing blast of heat and courage.";
    }
}

class Amya {
    constructor() {
        this.name = "Amya";
        this.trait = "Calm and Strategic";
    }

    special_ability() {
        return "Amya raises her hand! The very ground shifts, creating barriers and pathways. The arena is her chessboard.";
    }
}

class Holly {
    constructor() {
        this.name = "Holly";
        this.trait = "Joyful and Unpredictable";
    }

    special_ability() {
        return "Holly laughs, and the world glitters! It starts raining jellybeans, making the ground sticky and hilarious.";
    }
}

module.exports = {
    ModesManager,
    AIChaosBrain,
    BeastBestiary,
    Kate,
    Amya,
    Holly
};
