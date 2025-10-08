// --- Type Definitions for the Reputation Engine ---
export type DeedType = 'honorable' | 'chaotic';

export type ReputationTitle =
    | "Unknown (A blank slate)"
    | "Noble Hero (A beacon of light)"
    | "Valiant Knight (Respected and honorable)"
    | "Chaotic Good (An unpredictable savior)"
    | "Chaotic Mercenary (Your only allegiance is to coin)"
    | "Dreaded Tyrant (A scourge upon the land)"
    | "Wandering Soul (Your path is yet undecided)";

export class ReputationEngine {
    public honorPoints: number;
    public chaosPoints: number;
    public deedsLog: string[];

    constructor() {
        this.honorPoints = 0;
        this.chaosPoints = 0;
        this.deedsLog = [];
    }

    public recordDeed(deedType: DeedType, amount: number, description: string): string {
        if (deedType === 'honorable') {
            this.honorPoints += amount;
        } else { // 'chaotic'
            this.chaosPoints += amount;
        }

        const logEntry = `${deedType.charAt(0).toUpperCase() + deedType.slice(1)} deed: ${description} (+${amount} points)`;
        this.deedsLog.push(logEntry);
        return `Your reputation shifts... You performed a(n) ${deedType} deed.`;
    }

    public getReputation(): ReputationTitle {
        const totalPoints = this.honorPoints + this.chaosPoints;

        if (totalPoints === 0) {
            return "Unknown (A blank slate)";
        }

        const honorRatio = this.honorPoints / totalPoints;

        if (honorRatio > 0.8 && this.honorPoints > 10) {
            return "Noble Hero (A beacon of light)";
        } else if (honorRatio > 0.6) {
            return "Valiant Knight (Respected and honorable)";
        } else if (honorRatio > 0.4) {
            return "Chaotic Good (An unpredictable savior)";
        } else if (honorRatio > 0.2) {
            return "Chaotic Mercenary (Your only allegiance is to coin)";
        } else if (this.chaosPoints > 10) {
            return "Dreaded Tyrant (A scourge upon the land)";
        } else {
            return "Wandering Soul (Your path is yet undecided)";
        }
    }

    public getStatus(): string {
        const title = this.getReputation();
        return `Reputation: ${title}\nHonor Points: ${this.honorPoints}\nChaos Points: ${this.chaosPoints}`;
    }
}