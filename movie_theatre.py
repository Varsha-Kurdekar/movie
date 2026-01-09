class MovieTheatre:
    def __init__(self):
        # Initial booked seats per show
        self.show_slots = {
            "10AM": 40,
            "1PM": 75,
            "4PM": 120,
            "7PM": 60
        }

    def book_seats(self, slot, seats):
        if slot not in self.show_slots:
            raise ValueError("Invalid show slot")

        if seats <= 0:
            raise ValueError("Seat count must be positive")

        self.show_slots[slot] += seats

    def analyze_crowd(self, slot):
        count = self.show_slots.get(slot, 0)

        if count <= 50:
            return "LOW"
        elif count <= 100:
            return "MEDIUM"
        else:
            return "HIGH"

    def best_show_slot(self):
        return min(self.show_slots, key=self.show_slots.get)

    def display_status(self):
        result = []
        for slot, count in self.show_slots.items():
            level = self.analyze_crowd(slot)
            result.append(f"{slot} -> {count} seats -> Crowd: {level}")
        return result


def main():
    theatre = MovieTheatre()
    theatre.book_seats("1PM", 10)

    for line in theatre.display_status():
        print(line)

    print("\nBest show slot:", theatre.best_show_slot())


if __name__ == "__main__":
    main()