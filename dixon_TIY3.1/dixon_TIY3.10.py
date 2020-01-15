video_games = ['Half-Life', 'Call of Duty', 'Left 4 Dead']
print(f"My favorite video games are {video_games[0]}, {video_games[1]}, {video_games[2]}. ")
video_games.append('Overwatch')
video_games.insert(2, 'Rocket League')
print(f"These are my favorite games: {video_games[0]}, {video_games[1]}, {video_games[2]}, {video_games[3]}, {video_games[4]}.")
del video_games[2]
popped_game = video_games.pop(3)
print(f"Yeah, {popped_game.title()} was boring.")
too_repetitive = 'Call of Duty'
video_games.remove(too_repetitive)
print(f"{too_repetitive.title()} was too repetitive.")
print(video_games)
print(sorted(video_games))
video_games.sort()
video_games.reverse()
print(video_games)
length = len(video_games)
print(f"I have {length} favorite games.")

