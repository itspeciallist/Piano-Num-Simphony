from midiutil import MIDIFile

# --- ფიბონაჩის გენერატორი ---
def generate_fibonacci(n):
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# --- ციფრების ჩატვირთვა file-დან ---
def load_digits_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        digits = [int(char) for char in content if char.isdigit()]
        return digits

# --- ფიბონაჩის მიხედვით ციფრების გარდაქმნა ნოტებად ---
def digits_to_notes(digits, fibs):
    notes = []
    for i, d in enumerate(digits):
        fib_index = (d + i) % len(fibs)
        pitch = 40 + (fibs[fib_index] % 48)  # ნოტის დიაპაზონი (40-88)
        duration = 0.25 + (fibs[fib_index] % 3) * 0.25
        volume = 60 + (fibs[fib_index] % 40)
        notes.append((pitch, duration, volume))
    return notes

# --- MIDI სიმფონიის შექმნა ---
def create_symphony(notes, filename="symphony.mid"):
    midi = MIDIFile(1)  # ერთი ტრეკი
    track = 0
    time = 0
    midi.addTrackName(track, time, "Symphony")
    midi.addTempo(track, time, 120)

    channel = 0
    for pitch, duration, volume in notes:
        midi.addNote(track, channel, pitch, time, duration, volume)
        time += duration

    with open(filename, "wb") as output_file:
        midi.writeFile(output_file)
    print(f"[+] სიმფონია შეიქმნა: {filename}")

# --- მთავარი ფუნქცია ---
def main():
    fibonacci_sequence = generate_fibonacci(100)
    digits = load_digits_from_file("numbers.txt")
    if not digits:
        print("[-] ფაილში ციფრები არ მოიძებნა!")
        return

    notes = digits_to_notes(digits, fibonacci_sequence)
    create_symphony(notes)

if __name__ == "__main__":
    main()
