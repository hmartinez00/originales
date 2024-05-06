```python
from bs4 import BeautifulSoup

html = """
<span class="RankingStatus_rankingvalueNum__d_m_a index-mobile_rankingvalueNum__U8Jaj">65</span>

<span class="CardPc_titleText__RYOWo"># <!-- -->holamayo</span>
<span class="CardPc_itemValue__XGDmG">51K</span>
<span class="CardPc_itemLabel__FRKbE">Posts</span>
<span class="CardPc_itemValue__XGDmG">34M</span>
<span class="CardPc_itemLabel__FRKbE">Views</span>
"""

soup = BeautifulSoup(html, 'html.parser')

# Obtener los últimos 5 elementos span
spans = soup.find_all('span')[-5:]

# Extraer los valores de texto de los spans
values = [span.text for span in spans]

# Imprimir los valores
print(values)
```