def colormap():
    layout_data = [['Satellite','https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}','dark'],
               ['Dark','https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png','dark'],
               ['Light','https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png','dark'],
               ['Street Map','https://tile.openstreetmap.org/{z}/{x}/{y}.png','dark']]
    return layout_data