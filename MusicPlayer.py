class MusicPlayer:
    def __init__(self):
        self.stations = {
            "Classical": "Playing timeless classical music.",
            "Rock": "Rocking out to the classics.",
            "Synthwave": "Riding the retro waves of synth.",
            "Lofi": "Chilling to some lofi beats."
        }
        self.current_station = None

    def select_station(self, station_name):
        if station_name in self.stations:
            self.current_station = station_name
            return f"Tuned into {station_name}. {self.stations[station_name]}"
        return f"Station '{station_name}' not found. Available stations: {', '.join(self.stations.keys())}"

    def stop_music(self):
        self.current_station = None
        return "Music stopped."

    def get_stations(self):
        return list(self.stations.keys())