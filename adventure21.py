#!/user/bin/python
# vim: et sw=2 ts=2 sts=2
#

from advent import *
from advent import Game, Location, Connection, Object, Animal, Robot, Pet, Player
from advent import NORTH, SOUTH, EAST, WEST, UP, DOWN, RIGHT, LEFT, IN, OUT, FORWARD, BACK, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST, NOT_DIRECTION

# Create the game

game = Game("Adventure 21")

# Create all Rooms

room_flur_nord = game.new_location(
  "Flur Nord",
  """Du befindest dich im Flur. Im Westen ist das Wohnzimmer, im Osten ist eine Tuer mit Zahlenschloss. 
Der Flur erstreckt sich weiter gen Sueden.""")

room_flur_mitte = game.new_location(
  "Flur Mitte",
"""Du befindest dich immer noch im Flur. Im Westen ist ein Raum mit verschlossener Tuer.
Der Flur erstreckt sich nun gen Sueden und Norden.""")

room_flur_sued = game.new_location(
  "Flur Sued",
"""Du befindest dich am Suedende des Flurs. Im Westen ist eine offene Tuer. Im Sueden die Kueche. 
Der Flur erstreckt sich nun gen Norden und Osten.""")

room_flur_ost = game.new_location(
  "Flur Ost",
"""Du befindest dich am Ostfluegel des Flurs. Im Osten ist das Bad. Im Norden die Toilette.
Du siehst eine Wendeltreppe welche nach oben fuehrt. 
Im Westen geht es den weiten, weiten Weg zurueck.""")

room_wohnzimmer = game.new_location(
  "Wohnzimmer",
"""Im Wohnzimmer wird niemals gewohnt.""")

room_laura = game.new_location(
  "Laura's Zimmer",
"""Du siehst ein Boxspringbett, sieht sehr gemuetlich aus.""")

room_maga = game.new_location(
  "Maga's Zimmer",
"""Kunst, ueberall Kunst an den Waenden.""")

room_kueche = game.new_location(
  "Kueche",
"""Hier wird gekocht.""")

room_bad = game.new_location(
  "Bad",
"""Hmmm...""")

room_klo = game.new_location(
  "Toilette",
"""Wenn man muss, dann muss man""")

room_oben = game.new_location(
  "Wendeltreppe oben",
"""Es gibt ein oben!?!?
Du siehst eine Wand voller Skateboards vor dir.
Im Norden und Sueden siehst du je eine offene Tuer.""")

room_marco = game.new_location(
  "Marco's Zimmer",
"""Du befindest dich in einem Antiquitaetenladen.""")

room_andz = game.new_location(
  "Andz's Zimmer",
"""Chaos, ueberall Chaos.
Du siehst eine verschlossene Tuer im Norden""")

room_dachboden = game.new_location(
  "Dachboden",
"""Ein Dachboden!""")

# connect the rooms

game.new_connection("Flur", room_flur_nord, room_flur_mitte, SOUTH, NORTH)
game.new_connection("Flur", room_flur_mitte, room_flur_sued, SOUTH, NORTH)
game.new_connection("Flur", room_flur_sued, room_flur_ost, EAST, WEST)

game.new_connection("Tuer", room_flur_nord, room_wohnzimmer, WEST, EAST)
game.new_connection("Tuer", room_flur_mitte, room_laura, WEST, EAST)
game.new_connection("Tuer", room_flur_sued, room_maga, WEST, EAST)
game.new_connection("Tuer", room_flur_sued, room_kueche, SOUTH, NORTH)
game.new_connection("Tuer", room_flur_ost, room_bad, EAST, WEST)
game.new_connection("Tuer", room_flur_ost, room_klo, NORTH, SOUTH)

game.new_connection("Wendeltreppe", room_flur_ost, room_oben, UP, DOWN)

game.new_connection("Tuer", room_oben, room_marco, SOUTH, NORTH)
game.new_connection("Tuer", room_oben, room_andz, NORTH, SOUTH)
game.new_connection("Tuer", room_andz, room_dachboden, NORTH, SOUTH)

# Now we are going to add our player at the starting location:

player = game.new_player(room_flur_nord)

game.run()
