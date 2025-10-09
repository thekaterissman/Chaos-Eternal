// --- Type Definitions for the World Clock ---
export interface WorldEvent {
    description: string;
    type: 'dangerous' | 'peaceful' | 'chaotic' | 'cataclysm';
    duration: number;
}

export class WorldClock {
    public time: number;
    public currentEventName: string | null;
    public eventTimer: number;
    private events: Record<string, WorldEvent>;
    private cataclysms: Record<string, WorldEvent>;

    constructor() {
        this.time = 0;
        this.currentEventName = null;
        this.eventTimer = 0;
        this.events = {
            'blood_moon': { description: "The Blood Moon rises! The air crackles with dark energy, and beasts are more ferocious.", type: 'dangerous', duration: 10 },
            'merchants_festival': { description: "The Merchant's Festival is here! Rare goods are available for a limited time.", type: 'peaceful', duration: 20 },
            'celestial_alignment': { description: "The stars align! The veil between worlds thins, and strange creatures may appear.", type: 'chaotic', duration: 15 },
            'era_of_calm': { description: "An era of calm settles upon the land. A perfect time for building and growth.", type: 'peaceful', duration: 30 },
            'plague_of_shadows': { description: "A Plague of Shadows sweeps the land. The world is darker, and Geeves is more likely to be cruel.", type: 'dangerous', duration: 10 }
        };
        this.cataclysms = {
            'raging_typhoon': { description: "A RAGING TYPHOON makes landfall! The world is battered by cosmic winds and torrential rain.", type: 'cataclysm', duration: 25 },
            'worldquake': { description: "A WORLDQUAKE shatters the landscape! The ground itself is unstable and treacherous.", type: 'cataclysm', duration: 30 },
            'mana_vortex': { description: "A MANA VORTEX has opened! Raw magic pours into the world, making all abilities dangerously unpredictable.", type: 'cataclysm', duration: 20 }
        };
    }

    public advanceTime(ticks = 1): string {
        this.time += ticks;

        if (this.currentEventName) {
            this.eventTimer -= ticks;
            if (this.eventTimer <= 0) {
                const endedEvent = this.currentEventName;
                this.currentEventName = null;
                return `The ${endedEvent.replace(/_/g, ' ')} has ended. The world returns to normal.`;
            } else {
                return `The ${this.currentEventName.replace(/_/g, ' ')} continues. ${this.eventTimer} ticks remaining.`;
            }
        }

        // There's a small chance for a cataclysm to occur instead of a normal event.
        if (Math.random() < 0.05) { // 5% chance for a world-shaking event
            this.triggerRandomEvent(true);
            const event = this.cataclysms[this.currentEventName!];
            return `A CATACLYSM has begun! ${event.description}`;
        }

        if (Math.random() < 0.25) { // 25% chance for a normal event
            this.triggerRandomEvent(false);
            const event = this.events[this.currentEventName!];
            return `A new event has begun! ${event.description}`;
        }

        return "Time passes, but the world remains unchanged.";
    }

    private triggerRandomEvent(isCataclysm: boolean): void {
        const eventSource = isCataclysm ? this.cataclysms : this.events;
        const eventKeys = Object.keys(eventSource);
        const eventName = eventKeys[Math.floor(Math.random() * eventKeys.length)];
        this.currentEventName = eventName;
        this.eventTimer = eventSource[eventName].duration;
    }

    public getCurrentEvent(): (WorldEvent & { name: string }) | null {
        if (this.currentEventName) {
            const eventData = this.events[this.currentEventName] || this.cataclysms[this.currentEventName];
            return {
                name: this.currentEventName,
                ...eventData
            };
        }
        return null;
    }

    public getStatus(): string {
        const eventDesc = this.currentEventName
            ? `Current Event: ${this.currentEventName.replace(/_/g, ' ')} (${this.eventTimer} ticks left)`
            : "Current Event: None";
        return `World Time: ${this.time}. ${eventDesc}`;
    }
}