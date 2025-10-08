// --- Type Definitions for the World Clock ---
export interface WorldEvent {
    description: string;
    type: 'dangerous' | 'peaceful' | 'chaotic';
    duration: number;
}

export class WorldClock {
    public time: number;
    public currentEventName: string | null;
    public eventTimer: number;
    private events: Record<string, WorldEvent>;

    constructor() {
        this.time = 0;
        this.currentEventName = null;
        this.eventTimer = 0;
        this.events = {
            'blood_moon': {
                description: "The Blood Moon rises! The air crackles with dark energy, and beasts are more ferocious.",
                type: 'dangerous',
                duration: 10
            },
            'merchants_festival': {
                description: "The Merchant's Festival is here! Rare goods are available for a limited time.",
                type: 'peaceful',
                duration: 20
            },
            'celestial_alignment': {
                description: "The stars align! The veil between worlds thins, and strange creatures may appear.",
                type: 'chaotic',
                duration: 15
            },
            'era_of_calm': {
                description: "An era of calm settles upon the land. A perfect time for building and growth.",
                type: 'peaceful',
                duration: 30
            },
            'plague_of_shadows': {
                description: "A Plague of Shadows sweeps the land. The world is darker, and Geeves is more likely to be cruel.",
                type: 'dangerous',
                duration: 10
            }
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

        // 25% chance per tick to trigger a new event if none is active
        if (Math.random() < 0.25) {
            this.triggerRandomEvent();
            const event = this.events[this.currentEventName!];
            return `A new event has begun! ${event.description}`;
        }

        return "Time passes, but the world remains unchanged.";
    }

    private triggerRandomEvent(): void {
        const eventKeys = Object.keys(this.events);
        const eventName = eventKeys[Math.floor(Math.random() * eventKeys.length)];
        this.currentEventName = eventName;
        this.eventTimer = this.events[eventName].duration;
    }

    public getCurrentEvent(): (WorldEvent & { name: string }) | null {
        if (this.currentEventName) {
            return {
                name: this.currentEventName,
                ...this.events[this.currentEventName]
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