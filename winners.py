import random
import time

def get_participants():
    participants = {}
    for i in range(1, 11):
        count = int(input(f"Сколько участников выбрало вариант {i}? "))
        participants[i] = list(range(1, count + 1))
    return participants

def draw_winners(participants, total_winners):
    winners = []
    for place in range(total_winners, 0, -1):
        print(f"\nМесто номер {place} занимает...")
        valid_choices = [key for key in participants if participants[key]]
        time.sleep(10)
        if not valid_choices:
            print("Больше участников нет!")
            break
        chosen_key = random.choice(valid_choices)
        chosen_participant = random.choice(participants[chosen_key])
        print(f"Номер {chosen_participant} из варианта ответа {chosen_key}!")
        participants[chosen_key].remove(chosen_participant)
        if not participants[chosen_key]:
            participants.pop(chosen_key)

def main():
    total_winners = int(input("Введите количество победителей: "))
    participants = get_participants()
    draw_winners(participants, total_winners)

if __name__ == "__main__":
    main()
