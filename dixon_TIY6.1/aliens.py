aliens = []

for alienNumber in range(30):
    newAlien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(newAlien)

for alien in aliens[:5]:
    print(alien)

print(f"Total Aliens: {len(aliens)}")
