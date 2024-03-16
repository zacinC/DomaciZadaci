class Televizor:
    def __init__(self):
        self.currChannel = 1
        self.currChannelName = ""
        self.channels = []
        self.volume = 5

    def set_channel(self, broj):
        if 0 < broj <= len(self.channels):
            self.currChannel = broj

    def get_channel(self):
        return self.currChannel

    def set_current_channel_name(self, naziv):
        self.currChannelName = naziv

    def get_current_channel_name(self):
        return self.currChannelName

    def set_volume(self):
        if 0 <= self.volume <= 10:
            self.volume += 1
        return self.volume

    def get_volume(self):
        return self.volume

    def dodaj_kanal(self, naziv_kanala):
        self.channels.append(naziv_kanala)

    def obrisi_kanal(self, naziv_kanala):
        if naziv_kanala in self.channels:
            self.channels.remove(naziv_kanala)

    def pojacaj_ton(self):
        if self.volume < 10:
            self.volume += 1

    def ime_kanala(self, broj_kanala):
        if 1 <= broj_kanala <= len(self.channels):
            return self.channels[broj_kanala - 1]
        else:
            return "Kanal ne postoji"
