class MusicPlayer:
    def __init__(self):
        self.stations = {
            "Classical": {
                "description": "Playing timeless classical music.",
                "bonus": None
            },
            "Rock": {
                "description": "Rocking out to the classics. Increases damage by 10%.",
                "bonus": {"stat": "damage", "amount": 1.1}
            },
            "Synthwave": {
                "description": "Riding the retro waves of synth.",
                "bonus": None
            },
            "Lofi": {
                "description": "Chilling to some lofi beats. Increases healing by 20%.",
                "bonus": {"stat": "heal", "amount": 1.2}
            }
        }
        self.current_station = None

    def select_station(self, station_name):
        if station_name in self.stations:
            self.current_station = station_name
            description = self.stations[station_name]["description"]
            return f"Tuned into {station_name}. {description}"
        return f"Station '{station_name}' not found. Available stations: {', '.join(self.stations.keys())}"

    def stop_music(self):
        self.current_station = None
        return "Music stopped."

    def get_stations(self):
        return list(self.stations.keys())

    def get_current_bonus(self):
        if not self.current_station:
            return None
        return self.stations[self.current_station].get("bonus")