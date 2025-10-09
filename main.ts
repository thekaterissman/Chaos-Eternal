import { GeevesBrain } from './GeevesBrain';
import { BeastEcosystem, OwnedBeast } from './BeastEcosystem';
import { WorldClock } from './WorldClock';
import { ReputationEngine } from './ReputationEngine';
import * as readline from 'readline';
import { promises as fs } from 'fs';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const ask = (query: string): Promise<string> => new Promise((resolve) => rl.question(query, resolve));

// --- Type Definition for the World's Persistent State ---
interface WorldState {
    ecosystem: { coins: number; ownedBeasts: Record<string, OwnedBeast> };
    clock: { time: number; currentEventName: string | null; eventTimer: number };
    reputation: { honorPoints: number; chaosPoints: number; deedsLog: string[] };
    playerBeasts: string[];
}

class GameWorld {
    private geeves: GeevesBrain;
    private ecosystem: BeastEcosystem;
    private clock: WorldClock;
    private reputation: ReputationEngine;
    private playerBeasts: string[];
    private worldTimer: NodeJS.Timeout | null = null;
    private readonly saveFilePath = 'world_state.json';

    constructor() {
        console.log("Forging the world's core systems...");
        this.geeves = new GeevesBrain();
        this.ecosystem = new BeastEcosystem(20);
        this.clock = new WorldClock();
        this.reputation = new ReputationEngine();
        this.playerBeasts = [];
    }

    public async initialize(): Promise<void> {
        await this.loadWorld();
        console.log("The world is ready. Welcome, creator.");
    }

    public start(): void {
        console.log("The world's heartbeat begins...");
        this.worldTimer = setInterval(() => this.tick(), 5000);
        this.promptUser();
    }

    private tick(): void {
        console.log("\n\n--- [The world takes a breath...] ---");
        const eventMessage = this.clock.advanceTime();
        if (!eventMessage.includes("remains unchanged")) {
            console.log(`[EVENT]: ${eventMessage}`);
            // Check if the new event is a cataclysm and handle its effects
            const currentEvent = this.clock.getCurrentEvent();
            if (currentEvent?.type === 'cataclysm') {
                const cataclysmMessages = this.ecosystem.handleCataclysm();
                cataclysmMessages.forEach(msg => console.log(`[CATACLYSM EFFECT]: ${msg}`));
            }
        }
        // The weight of time now affects your companions
        this.ecosystem.decayHappiness();
        this.showMenu();
    }

    private showMenu(): void {
        console.log("\n" + "=".repeat(20));
        console.log("What is your will, creator? (The world continues to breathe)");
        console.log("1. [Status] | 2. [Work] | 3. [Buy Beast] | 4. [Train] | 5. [Play] | 6. [Use Ability] | 7. [Fight] | 8. [Exit]");
        process.stdout.write("> ");
    }

    private async promptUser(): Promise<void> {
        this.showMenu();
        for await (const line of rl) {
            console.clear();
            await this.processCommand(line.trim().toLowerCase());
            if (this.worldTimer === null) break;
            this.showMenu();
        }
    }

    private async processCommand(choice: string): Promise<void> {
        switch (choice) {
            case '1': this.printStatus(); break;
            case '2': this.ecosystem.coins++; console.log("You earn 1 coin for your efforts."); break;
            case '3': await this.buyBeastInterface(); break;
            case '4': await this.trainBeastInterface(); break;
            case '5': await this.playWithBeastInterface(); break;
            case '6': await this.useBeastAbilityInterface(); break;
            case '7': this.simulateFight(); break;
            case '8': await this.stop(); break;
            default: console.log("An invalid command. The world does not respond."); break;
        }
    }

    public async stop(): Promise<void> {
        console.log("The world holds its breath, awaiting your return.");
        if (this.worldTimer) {
            clearInterval(this.worldTimer);
            this.worldTimer = null;
        }
        await this.saveWorld();
        rl.close();
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
            this.playerBeasts.forEach((id: string) => console.log(this.ecosystem.getBeastDetails(id)));
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
        availableBeasts.forEach((name: string) => console.log(`- ${name} (Cost: ${this.ecosystem.beastTemplates[name].cost})`));
        const beastToBuy = (await ask("Which beast? > ")).toLowerCase().trim();
        const [message, beastId] = this.ecosystem.buyBeast(beastToBuy, availableBeasts);
        if (beastId) {
            this.playerBeasts.push(beastId);
            console.log(`Success! ${message.split('!')[0]}! ID: ${beastId.substring(0, 8)}`);
        } else {
            console.log(message);
        }
    }

    private async trainBeastInterface(): Promise<void> {
        if (this.playerBeasts.length === 0) { console.log("You have no beasts to train."); return; }
        this.playerBeasts.forEach((id: string, i: number) => console.log(`${i + 1}. ${this.ecosystem.getBeastDetails(id)}`));
        const choice = parseInt(await ask("Train which beast? > "), 10) - 1;
        if (!isNaN(choice) && this.playerBeasts[choice]) {
            console.log(this.ecosystem.gainXp(this.playerBeasts[choice], Math.floor(Math.random() * 31) + 20));
        } else { console.log("Invalid choice."); }
    }

    private async useBeastAbilityInterface(): Promise<void> {
        if (this.playerBeasts.length === 0) { console.log("You have no beasts to command."); return; }
        this.playerBeasts.forEach((id: string, i: number) => console.log(`${i + 1}. ${this.ecosystem.getBeastDetails(id)}`));
        const choice = parseInt(await ask("Use which ability? > "), 10) - 1;
        if (!isNaN(choice) && this.playerBeasts[choice]) {
            const beastId = this.playerBeasts[choice];
            const move = `use_beast_${this.ecosystem.ownedBeasts[beastId].template}`;
            this.geeves.learnMove(move);
            console.log(this.ecosystem.useBeastAbility(beastId));
            console.log(`Geeves observes you using '${move}'.`);
        } else { console.log("Invalid choice."); }
    }

    private async playWithBeastInterface(): Promise<void> {
        if (this.playerBeasts.length === 0) {
            console.log("You have no beasts to play with.");
            return;
        }
        console.log("Which beast do you want to play with?");
        this.playerBeasts.forEach((id, i) => console.log(`${i + 1}. ${this.ecosystem.getBeastDetails(id)}`));

        const choice = parseInt(await ask("> "), 10) - 1;
        if (!isNaN(choice) && this.playerBeasts[choice]) {
            const beastId = this.playerBeasts[choice];
            console.log(this.ecosystem.playWithBeast(beastId));
        } else {
            console.log("Invalid choice.");
        }
    }

    private simulateFight(): void {
        console.log("\nA challenger appears!");
        const moves = ['attack', 'dodge', 'attack', 'block', 'use_item', 'attack', 'dodge'];
        moves.forEach(move => { this.geeves.learnMove(move); console.log(`You use '${move}'...`); });
        console.log("\nThe battle ends!");
        console.log(this.reputation.recordDeed('honorable', 5, "Won a simulated battle."));

        const reputationTitle = this.reputation.getReputation();
        const currentEvent = this.clock.getCurrentEvent();

        console.log(`Geeves considers your reputation: ${reputationTitle}`);
        if(currentEvent) {
            console.log(`And the current world event: ${currentEvent.name}`);
        }

        const reaction = this.geeves.getReaction(reputationTitle, currentEvent);
        console.log(`\nGEEVES' REACTION: ${reaction}`);
    }

    private async saveWorld(): Promise<void> {
        const worldState: WorldState = {
            ecosystem: { coins: this.ecosystem.coins, ownedBeasts: this.ecosystem.ownedBeasts },
            clock: { time: this.clock.time, currentEventName: this.clock.currentEventName, eventTimer: this.clock.eventTimer },
            reputation: { honorPoints: this.reputation.honorPoints, chaosPoints: this.reputation.chaosPoints, deedsLog: this.reputation.deedsLog },
            playerBeasts: this.playerBeasts
        };
        try {
            await fs.writeFile(this.saveFilePath, JSON.stringify(worldState, null, 2));
            await this.geeves.saveMemory();
            console.log("The world's soul has been committed to memory.");
        } catch (error) {
            console.error("Fatal error: Failed to save the world's soul.", error);
        }
    }

    private async loadWorld(): Promise<void> {
        try {
            const data = await fs.readFile(this.saveFilePath, 'utf-8');
            const worldState: WorldState = JSON.parse(data);
            this.ecosystem.coins = worldState.ecosystem.coins;
            this.ecosystem.ownedBeasts = worldState.ecosystem.ownedBeasts;
            this.clock.time = worldState.clock.time;
            this.clock.currentEventName = worldState.clock.currentEventName;
            this.clock.eventTimer = worldState.clock.eventTimer;
            this.reputation.honorPoints = worldState.reputation.honorPoints;
            this.reputation.chaosPoints = worldState.reputation.chaosPoints;
            this.reputation.deedsLog = worldState.reputation.deedsLog;
            this.playerBeasts = worldState.playerBeasts;
            await this.geeves.loadMemory();
            console.log("The world's soul has been restored from memory.");
        } catch (error) {
            if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
                console.log("A new world is born, its soul yet unwritten.");
            } else {
                console.error("Fatal error: Failed to restore the world's soul.", error);
            }
        }
    }
}

async function main() {
    const world = new GameWorld();
    await world.initialize();
    world.start();
}

main();