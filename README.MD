# ⛏️Scrapper for Google Finance 📈
Scraping out information about stocks in Google Finance in python

### Libraries Used 🗃️
make sure these are installed before use the Scrapper
* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


### Use 💻 
```python
import scraper
g=scraper.GoogleFinance("RELIANCE:nse")
print(g.get_details())
```
Output
```
>>> {'name': 'Reliance Industries Ltd', 'price': 1288.35, 'low': 1287.45, 'high': 1294.95, 'low52': 1184.95, 'high52': 1608.8, 'pe': 25.66}
```

<b>NB :</b> This is not the full code of the Scraper
