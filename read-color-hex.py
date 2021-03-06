from bs4 import BeautifulSoup
import urllib
import urllib.request

def read_page (addr):
  try:
    f4 = urllib.request.urlopen (addr)
    html = f4.read ()
    f4.close ()
    html = html.decode ()
  except urllib.error.HTTPError:
    html = "\n[Page does not exist.]"
  return html + "\n"

for i in range (1,3):
  addr = f"https://www.color-hex.com/color-palettes/?page={i}"
  print ("# Receiving:",addr)
  html = read_page (addr)
  soup = BeautifulSoup (html, "html.parser")
  anchs = soup.find_all ('a')
  for anc in anchs:
    name = anc.text.strip()
    divs = anc.find_all ('div', attrs={'class':"palettecolordiv"})
    if divs:
      print (f'palette ["{name}"] = [')
      for div in divs:
        hexcode = div.attrs ['style'].split (":")[1]
        print (f'  "{hexcode}",')
      print ("]")

"""
<a href="/color-palette/106107" title="Color palette Orange squash">
<div class="palettecolordivcon">
<div class="palettecolordiv" style="background-color:#df9683"></div>
<div class="palettecolordiv" style="background-color:#e5b160"></div>
<div class="palettecolordiv" style="background-color:#d69839"></div>
<div class="palettecolordiv" style="background-color:#d8753f"></div>
<div class="palettecolordiv" style="background-color:#b66826"></div>
<div class="clearfix"></div>
</div>
Orange squash</a>

# Receiving: https://www.color-hex.com/color-palettes/?page=1
palette ["Dream of Calm Creams"] = [
  "#fffee6",
  "#fffdd4",
  "#fdfbce",
  "#fdfbc9",
  "#fffdc2",
]
palette ["Planner Purples"] = [
  "#e5cde4",
  "#cb99c7",
  "#b78fcb",
  "#d0a5e3",
  "#e6c3f6",
]
"""
