import { randomUUID } from 'crypto';

// Define a placeholder for the WorldEvent type for now.
// This will eventually be imported from WorldClock.ts
export interface WorldEvent {
    name: string;
    type: 'dangerous' | 'peaceful' | 'chaotic' | 'cataclysm';
}

// --- Type Definitions for the Beast Ecosystem ---
export interface BeastTemplate {
    cost: number;
    ability: string;
    xpToNextLevel: number;
    evolution: string | null;
}

export interface OwnedBeast {
    template: string;
    level: number;
    xp: number;
    happiness: number; // 0-100
}

export class BeastEcosystem {
    public coins: number;
    public beastTemplates: Record<string, BeastTemplate>;
    public ownedBeasts: Record<string, OwnedBeast>;

    constructor(coins = 0) {
        this.coins = coins;
        this.ownedBeasts = {};
        this.beastTemplates = {
            'leo_cub': { cost: 1, ability: 'A playful roar that slightly distracts enemies.', xpToNextLevel: 100, evolution: 'leo_lion' },
            'leo_lion': { cost: 0, ability: 'A mighty roar that stuns nearby foes for a short duration.', xpToNextLevel: 500, evolution: 'celestial_lion' },
            'celestial_lion': { cost: 0, ability: 'A cosmic roar that damages all enemies and grants a temporary shield.', xpToNextLevel: 9999, evolution: null },
            'scorpio_hatchling': { cost: 1, ability: 'A weak sting that applies a minor poison effect.', xpToNextLevel: 100, evolution: 'scorpio_sting' },
            'scorpio_sting': { cost: 0, ability: 'A venomous sting that deals significant poison damage over time.', xpToNextLevel: 500, evolution: 'astral_scorpion' },
            'astral_scorpion': { cost: 0, ability: 'A cosmic sting that instantly halves an enemy\'s health.', xpToNextLevel: 9999, evolution: null },
            'phoenix_hatchling': { cost: 25, ability: 'A spark of warmth that slightly heals the user.', xpToNextLevel: 200, evolution: 'phoenix_firebird' },
            'phoenix_firebird': { cost: 0, ability: 'A wave of fire that damages enemies and heals allies.', xpToNextLevel: 9999, evolution: null }
        };
    }

    public getAvailableBeasts(worldEvent?: WorldEvent): string[] {
        const available: string[] = [];
        if (worldEvent?.type === 'dangerous') {
            return []; // No beasts available during dangerous events
        }

        for (const name in this.beastTemplates) {
            const template = this.beastTemplates[name];
            if (template.cost > 0) {
                if (name === 'leo_cub' || name === 'scorpio_hatchling') {
                    available.push(name);
                }
                if (worldEvent?.name === 'merchants_festival' && name === 'phoenix_hatchling') {
                    available.push(name);
                }
            }
        }
        return available;
    }

    public buyBeast(beastName: string, availableBeasts: string[]): [string, string | null] {
        if (!availableBeasts.includes(beastName)) {
            return ["This beast is currently not available for purchase.", null];
        }

        const template = this.beastTemplates[beastName];
        if (this.coins >= template.cost) {
            this.coins -= template.cost;
            const beastId = randomUUID();
            this.ownedBeasts[beastId] = {
                template: beastName,
                level: 1,
                xp: 0,
                happiness: 100 // Start with maximum happiness
            };
            return [`A new ${beastName} joins your sanctuary! Its journey begins.`, beastId];
        } else {
            return ["Not enough coins, creator. The world is expensive.", null];
        }
    }

    public gainXp(beastId: string, amount: number): string {
        const beast = this.ownedBeasts[beastId];
        if (!beast) return "Unknown beast.";

        beast.xp += amount;
        let template = this.beastTemplates[beast.template];
        let leveledUp = false;

        while (beast.xp >= template.xpToNextLevel) {
            beast.level++;
            beast.xp -= template.xpToNextLevel;
            leveledUp = true;

            if (template.evolution) {
                const oldTemplateName = beast.template;
                beast.template = template.evolution;
                template = this.beastTemplates[beast.template];
                return `Your ${oldTemplateName} has Evolved into a ${beast.template}! It is now level ${beast.level}.`;
            }
        }

        return leveledUp
            ? `Your beast ${beast.template} has leveled up to level ${beast.level}!`
            : `Your beast ${beast.template} gained ${amount} XP.`;
    }

    public useBeastAbility(beastId: string): string {
        const beast = this.ownedBeasts[beastId];
        if (!beast) return "Unknown beast.";

        if (beast.happiness < 20) {
            return `Your ${beast.template} is too sad to use its ability. It looks away dejectedly.`;
        }

        const template = this.beastTemplates[beast.template];
        let effectiveness = "";
        if (beast.happiness > 80) {
            effectiveness = " It's a critical success!";
        }

        return `Your ${beast.template} (Lvl ${beast.level}) uses its ability: ${template.ability}${effectiveness}`;
    }

    public getBeastDetails(beastId: string): string {
        const beast = this.ownedBeasts[beastId];
        if (!beast) return "Unknown beast.";

        const template = this.beastTemplates[beast.template];
        const xpNeeded = template.xpToNextLevel;
        return `Beast ID: ${beastId.substring(0, 8)}, Type: ${beast.template}, Level: ${beast.level}, XP: ${beast.xp}/${xpNeeded}, Happiness: ${beast.happiness}/100`;
    }

    public decayHappiness(amount = 1): void {
        for (const id in this.ownedBeasts) {
            this.ownedBeasts[id].happiness = Math.max(0, this.ownedBeasts[id].happiness - amount);
        }
    }

    public playWithBeast(beastId: string): string {
        const beast = this.ownedBeasts[beastId];
        if (!beast) return "Unknown beast.";

        beast.happiness = Math.min(100, beast.happiness + 15);
        return `You play with your ${beast.template}. It looks much happier now! (Happiness: ${beast.happiness}/100)`;
    }

    public handleCataclysm(): string[] {
        const messages: string[] = [];
        if (Object.keys(this.ownedBeasts).length === 0) {
            return ["The cataclysm rages, but you have no beasts to be frightened."];
        }

        messages.push("Your beasts are terrified by the cataclysm!");
        for (const id in this.ownedBeasts) {
            const beast = this.ownedBeasts[id];
            const oldHappiness = beast.happiness;
            beast.happiness = Math.max(0, oldHappiness - 30); // Cataclysms are very scary
            messages.push(`- Your ${beast.template}'s happiness dropped from ${oldHappiness} to ${beast.happiness}.`);
        }
        return messages;
    }
}