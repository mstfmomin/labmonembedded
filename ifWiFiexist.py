from wifi import Cell, Scheme
cell = Cell.all('wlan0')[2]
scheme = Scheme.for_cell('wlan0', 'fiBonAcci', cell, b'silentscream')
scheme.activate()
