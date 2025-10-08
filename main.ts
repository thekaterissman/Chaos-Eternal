import { GeevesBrain } from './GeevesBrain';
import { BeastEcosystem } from './BeastEcosystem';
import { WorldClock } from './WorldClock';
import { ReputationEngine } from './ReputationEngine';
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const ask = (query: string): Promise<string> => new Promise((resolve) => rl.question(query, resolve));
const sleep = (ms: number): Promise<void> => new Promise(resolve => setTimeout(resolve, ms));

class GameWorld {
    private geeves: GeevesBrain;
    private ecosystem: BeastEcosystem;
    private clock: WorldClock;
    private reputation: ReputationEngine;
    private playerBeasts: string[]; // Stores beast IDs

    constructor() {
        console.log("Forging the world's core systems...");
        this.geeves = new GeevesBrain();
        this.ecosystem = new BeastEcosystem(20); // Start with 20 coins
        this.clock = new WorldClock();
        this.reputation = new ReputationEngine();
        this.playerBeasts = [];
    }

    public async initialize(): Promise<void> {
        await this.geeves.loadMemory();
        console.log("The world is ready. Welcome, creator.");
    }

    public async mainLoop(): Promise<void> {
        while (true) {
            console.log("\n" + "=".repeat(20));
            console.log("What is your will, creator?");
            console.log("1. [Status] - View the state of the world.");
            console.log("2. [Advance Time] - Let a day pass.");
            console.log("3. [Work] - Perform work to earn a coin.");
            console.log("4. [Buy Beast] - Purchase a new beast.");
            console.log("5. [Train Beast] - Train a beast to gain XP.");
            console.log("6. [Use Beast Ability] - Command a beast in a drill.");
            console.log("7. [Simulate Fight] - Test yourself and Geeves.");
            console.log("8. [Exit] - Leave the world.");

            const choice = (await ask("> ")).toLowerCase().trim();
            console.clear();

            switch (choice) {
                case '1': this.printStatus(); break;
                case '2': console.log(this.clock.advanceTime()); break;
                case '3': this.ecosystem.coins++; console.log("You earn 1 coin for your efforts."); break;
                case '4': await this.buyBeastInterface(); break;
                case '5': await this.trainBeastInterface(); break;
                case '6': await this.useBeastAbilityInterface(); break;
                case '7': this.simulateFight(); break;
                case '8': console.log("The world will await your return."); rl.close(); return;
                default: console.log("An invalid command. The world does not respond."); break;
            }
        }
    }

    private printStatus(): void {
        console.log("\n--- WORLD STATUS ---");
        console.log(this.clock.getStatus());
        console.log(this.reputation.getStatus());
        console.log(`Player Coins: ${this.ecosystem.coins}`);
        console.log("\n--- Player's Beasts ---");
        if (this.playerBeasts.length === 0) {
            console.log("You own no beasts.");
        } else {
            this.playerBeasts.forEach(id => console.log(this.ecosystem.getBeastDetails(id)));
        }
        console.log("--------------------");
    }

    private async buyBeastInterface(): Promise<void> {
        const currentEvent = this.clock.getCurrentEvent();
        const availableBeasts = this.ecosystem.getAvailableBeasts(currentEvent ?? undefined);

        console.log("--- Beast Market ---");
        if (availableBeasts.length === 0) {
            console.log("The beasts are hiding... No one is available for purchase.");
            return;
        }

        console.log("Available beasts for purchase:");
        availableBeasts.forEach(name => {
            const template = this.ecosystem.beastTemplates[name];
            console.log(`- ${name} (Cost: ${template.cost})`);
        });

        const beastToBuy = (await ask("Which beast do you wish to acquire? > ")).toLowerCase().trim();
        const [message, beastId] = this.ecosystem.buyBeast(beastToBuy, availableBeasts);

        if (beastId) {
            this.playerBeasts.push(beastId);
            console.log(`Success! ${message.split('!')[0]}! Your new beast's ID is ${beastId.substring(0, 8)}`);
        } else {
            console.log(message);
        }
    }

    private async trainBeastInterface(): Promise<void> {
        if (this.playerBeasts.length === 0) {
            console.log("You have no beasts to train.");
            return;
        }

        console.log("Which beast do you want to train?");
        this.playerBeasts.forEach((id, i) => console.log(`${i + 1}. ${this.ecosystem.getBeastDetails(id)}`));

        const choice = parseInt(await ask("> "), 10) - 1;
        if (!isNaN(choice) && choice >= 0 && choice < this.playerBeasts.length) {
            const beastId = this.playerBeasts[choice];
            const xpGain = Math.floor(Math.random() * 31) + 20; // 20-50
            console.log(this.ecosystem.gainXp(beastId, xpGain));
        } else {
            console.log("Invalid choice.");
        }
    }

    private async useBeastAbilityInterface(): Promise<void> {
        if (this.playerBeasts.length === 0) {
            console.log("You have no beasts to command.");
            return;
        }
        console.log("Which beast's ability do you want to use?");
        this.playerBeasts.forEach((id, i) => console.log(`${i + 1}. ${this.ecosystem.getBeastDetails(id)}`));

        const choice = parseInt(await ask("> "), 10) - 1;
        if (!isNaN(choice) && choice >= 0 && choice < this.playerBeasts.length) {
            const beastId = this.playerBeasts[choice];
            const beastTemplate = this.ecosystem.ownedBeasts[beastId].template;
            const move = `use_beast_${beastTemplate}`;
            this.geeves.learnMove(move);
            console.log(`\nYou command your beast...`);
            await sleep(500);
            console.log(this.ecosystem.useBeastAbility(beastId));
            console.log(`Geeves observes you using '${move}'.`);
        } else {
            console.log("Invalid choice.");
        }
    }

    private simulateFight(): void {
        console.log("\nA challenger appears! You enter a simulated battle.");
        const moves = ['attack', 'dodge', 'attack', 'block', 'use_item', 'attack', 'dodge'];
        moves.forEach(move => {
            this.geeves.learnMove(move);
            console.log(`You use '${move}'...`);
        });

        console.log("\nThe battle ends!");
        console.log(this.reputation.recordDeed('honorable', 5, "Won a simulated battle."));

        const reputationTitle = this.reputation.getReputation();
        console.log(`Geeves considers your reputation: ${reputationTitle}`);
        const reaction = this.geeves.getReaction(reputationTitle);
        console.log(`\nGEEVES' REACTION: ${reaction}`);
    }
}

async function main() {
    const world = new GameWorld();
    await world.initialize();
    await world.mainLoop();
}

main();