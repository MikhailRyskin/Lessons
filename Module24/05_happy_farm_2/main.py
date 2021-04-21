from garden import PotatoGarden, Gardener

garden = PotatoGarden(5)
our_gardener = Gardener('Остин', garden)
while not garden.are_all_ripe():
    our_gardener.handle_garden()
our_gardener.harvest()
