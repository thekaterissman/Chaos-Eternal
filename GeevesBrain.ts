import { promises as fs } from 'fs';
import { ReputationTitle } from './ReputationEngine';
import { WorldEvent } from './WorldClock';

// --- Type Definitions for Geeves' Brain ---
interface TwistOrBoon {
    responses: string[];
}

interface MemoryData {
    moves: string[];
}

export class GeevesBrain {
    private playerMoves: string[];
    private readonly memoryFile: string;
    private readonly twists: Record<string, TwistOrBoon>;
    private readonly twistCounters: Record<string, string[]>;
    private readonly boons: Record<string, TwistOrBoon>;
    private readonly boonTriggers: Record<string, string[]>;

    constructor() {
        this.playerMoves = [];
        this.memoryFile = 'chaos_memory.json';
        this.twists = {
            'sandstorm': { responses: ["Sudden sandstorm! Haptics: Grit in your teeth. Dodge or bury.", "The desert awakens! A blinding sandstorm engulfs the arena."] },
            'gravity_flip': { responses: ["Floating islands spawn—gravity flips! Stomach drop incoming.", "Up is down, down is up! Gravity has been inverted."] },
            'dance_or_die': { responses: ["AI whispers: Dance for a shield, or get wrecked! Groove time.", "The beat drops... and so will you if you don't dance!"] },
            'vampire_curse': { responses: ["A vampire's curse! Your health drains, but every hit you land restores it.", "Feel the life draining from you... only violence can sustain you now."] },
            'mirrored_damage': { responses: ["A curse of mirrored pain! For the next 10 seconds, you feel what you inflict.", "Careful now. Every blow you land will be returned in kind."] },
            // ... and so on for all twists
        };
        this.twistCounters = {
            'defensive': ['vampire_curse', 'monster_mash', 'floor_is_lava', 'gladiators_challenge'],
            'offensive_spam': ['mirrored_damage', 'doppelganger', 'one_hit_wonder', 'giants_growth'],
            'dodge_spam': ['slippery_floor', 'forced_emotes', 'gravity_flip', 'shrink_ray'],
            'item_spam': ['weapon_swap', 'mana_overload', 'golden_touch', 'clown_fiesta'],
        };
        this.boons = {
            'divine_shield': { responses: ["A shimmering shield surrounds you, absorbing the next blow.", "Geeves grants you a barrier of pure light."] },
            'mana_font': { responses: ["A font of pure energy erupts at your feet, rapidly restoring your magic.", "Your power returns, overflowing."] },
            'lucky_clover': { responses: ["Your critical hit chance is doubled for the next 15 seconds.", "You feel inexplicably lucky."] },
            'ghost_wolf': { responses: ["A spectral wolf fights by your side for a short time.", "You are no longer alone. A spirit wolf joins the hunt."] },
            'health_potion': { responses: ["Geeves tosses you a potent health potion. Cheers!", "A gift, for a worthy performance."] }
        };
        this.boonTriggers = {
            'variety': ['divine_shield', 'mana_font', 'lucky_clover', 'ghost_wolf', 'health_potion']
        };
    }

    public learnMove(move: string): void {
        this.playerMoves.push(move);
        if (this.playerMoves.length > 10) {
            this.playerMoves = this.playerMoves.slice(-10);
        }
        this.saveMemory();
    }

    public getReaction(
        reputationTitle: ReputationTitle = "Unknown (A blank slate)",
        currentEvent: (WorldEvent & { name: string; }) | null = null
    ): string {
        if (this.playerMoves.length < 5) {
            return "Geeves is observing your opening moves.";
        }

        const recentMoves = this.playerMoves.slice(-5);
        const moveCounts = recentMoves.reduce((acc, move) => {
            acc[move] = (acc[move] || 0) + 1;
            return acc;
        }, {} as Record<string, number>);

        // --- Cataclysm Influence ---
        let twistChance = 0.2; // Base chance for a random twist
        let cataclysmActive = false;
        if (currentEvent?.type === 'cataclysm') {
            twistChance = 0.75; // During a cataclysm, Geeves is much more active
            cataclysmActive = true;
        }

        // --- Boon System ---
        let boonChance = 0.3;
        if (reputationTitle.includes('Noble Hero')) boonChance = 0.6;
        if (reputationTitle.includes('Dreaded Tyrant')) boonChance = 0.0;
        if (cataclysmActive) boonChance /= 2; // Boons are rarer in a cataclysm

        if (Object.keys(moveCounts).length >= 4 && Math.random() < boonChance) {
            const boonName = this.boonTriggers['variety'][Math.floor(Math.random() * this.boonTriggers['variety'].length)];
            const response = this.boons[boonName].responses[Math.floor(Math.random() * this.boons[boonName].responses.length)];
            return boonChance > 0.5 ? `Geeves smiles upon your noble deeds: ${response}` : `Geeves acknowledges your skill: ${response}`;
        }

        // --- Twist System (Pattern-based) ---
        let twistCategory: string | null = null;
        if ((moveCounts['dodge'] || 0) + (moveCounts['block'] || 0) >= 4) twistCategory = 'defensive';
        else if ((moveCounts['attack'] || 0) >= 4) twistCategory = 'offensive_spam';
        else if ((moveCounts['dodge'] || 0) >= 3) twistCategory = 'dodge_spam';
        else if ((moveCounts['use_item'] || 0) >= 3) twistCategory = 'item_spam';

        if (twistCategory) {
            const counters = this.twistCounters[twistCategory];
            const twistName = counters[Math.floor(Math.random() * counters.length)];
            const response = this.twists[twistName].responses[Math.floor(Math.random() * this.twists[twistName].responses.length)];
            return `Geeves counters your ${twistCategory.replace(/_/g, ' ')}: ${response}`;
        }

        // --- Random Twist Chance (influenced by Cataclysm) ---
        if (Math.random() < twistChance) {
            const allTwists = Object.keys(this.twists);
            const twistName = allTwists[Math.floor(Math.random() * allTwists.length)];
            const response = this.twists[twistName].responses[Math.floor(Math.random() * this.twists[twistName].responses.length)];
            return cataclysmActive
                ? `The ${currentEvent?.name.replace(/_/g, ' ')} intensifies as Geeves adds to the madness: ${response}`
                : `Geeves intervenes, unprovoked: ${response}`;
        }

        return "Geeves watches, silently judging your predictable moves.";
    }

    public async saveMemory(): Promise<void> {
        try {
            const data: MemoryData = { moves: this.playerMoves };
            await fs.writeFile(this.memoryFile, JSON.stringify(data, null, 2));
        } catch (error) {
            console.error("Failed to save Geeves's memory:", error);
        }
    }

    public async loadMemory(): Promise<void> {
        try {
            const data = await fs.readFile(this.memoryFile, 'utf-8');
            const memory: MemoryData = JSON.parse(data);
            this.playerMoves = memory.moves || [];
        } catch (error) {
            // If the file doesn't exist, it's a fresh start, which is fine.
            if ((error as NodeJS.ErrnoException).code !== 'ENOENT') {
                console.error("Failed to load Geeves's memory:", error);
            }
        }
    }
}