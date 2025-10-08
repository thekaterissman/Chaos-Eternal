import random

class WorldClock:
    def __init__(self):
        self.time = 0
        self.current_event = None
        self.events = {
            'blood_moon': {
                'description': "The Blood Moon rises! The air crackles with dark energy, and beasts are more ferocious.",
                'type': 'dangerous',
                'duration': 10 # in ticks
            },
            'merchants_festival': {
                'description': "The Merchant's Festival is here! Rare goods are available for a limited time.",
                'type': 'peaceful',
                'duration': 20
            },
            'celestial_alignment': {
                'description': "The stars align! The veil between worlds thins, and strange creatures may appear.",
                'type': 'chaotic',
                'duration': 15
            },
            'era_of_calm': {
                'description': "An era of calm settles upon the land. A perfect time for building and growth.",
                'type': 'peaceful',
                'duration': 30
            },
            'plague_of_shadows': {
                'description': "A Plague of Shadows sweeps the land. The world is darker, and Geeves is more likely to be cruel.",
                'type': 'dangerous',
                'duration': 10
            }
        }
        self.event_timer = 0

    def advance_time(self, ticks=1):
        self.time += ticks

        # If an event is active, count it down.
        if self.current_event:
            self.event_timer -= ticks
            if self.event_timer <= 0:
                event_name = self.current_event
                self.current_event = None
                return f"The {event_name.replace('_', ' ')} has ended. The world returns to normal."
            else:
                 return f"The {self.current_event.replace('_', ' ')} continues. {self.event_timer} ticks remaining."

        # If no event is active, there's a chance to trigger a new one.
        # Let's say a 25% chance per tick to keep things interesting.
        if random.random() < 0.25:
            self.trigger_random_event()
            event = self.events[self.current_event]
            return f"A new event has begun! {event['description']}"

        return "Time passes, but the world remains unchanged."

    def trigger_random_event(self):
        event_name = random.choice(list(self.events.keys()))
        self.current_event = event_name
        self.event_timer = self.events[event_name]['duration']

    def get_current_event(self):
        if self.current_event:
            return self.events[self.current_event]
        return None

    def get_status(self):
        event_desc = f"Current Event: {self.current_event} ({self.event_timer} ticks left)" if self.current_event else "Current Event: None"
        return f"World Time: {self.time}. {event_desc}"

# --- Example Usage ---
# clock = WorldClock()
# for i in range(50):
#     print(f"Tick {i+1}: {clock.advance_time()}")
#     print(f"--- Status: {clock.get_status()} ---")