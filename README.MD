# ⛏️WebReader : Scrapper for Google Finance 📈
Scraping out information about stocks in Google Finance in python

> [!IMPORTANT]
> ### 🗃️ Libraries Used 
> make sure these are installed before use the Scrapper
> * [requests](https://pypi.org/project/requests/)
> * [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)


### 💻 Sample Usage  
```python
import WebReader
g=WebReader.GoogleFinance("RELIANCE:NSE")
print(g.get_details())
```
Output
```
>>> {'name': 'Reliance Industries Ltd', 'price': 1288.35, 'low': 1287.45, 'high': 1294.95, 'low52': 1184.95, 'high52': 1608.8, 'pe': 25.66}
```
<br/>

## ✏️ Syntax 

```python
import WebReader
g=WebReader.GoogleFinance(share)
g.get_details(attribute)
```
* ${\color{red}share: }$
The share symbol for the security to consider. It’s mandatory to use both the exchange symbol and share symbol for accurate results and to avoid discrepancies
    - **Example :**
    `RELIANCE:NSE` where `RELIANCE` is *Share Symbol* and `NSE` is *Exchange Symbol*
* ${\color{red}attribute: }$
The attribute to fetch about `share` from Google Finance. It shows all details by default 
    - ${\color{orange}name : }$ `name` of the share
    - ${\color{orange}price : }$ `current price` of the share
    - ${\color{orange}low : }$ `today's low price` of the share
    - ${\color{orange}high : }$ `today's high price` of the share
    - ${\color{orange}low52 : }$ `52 week's low price` of the share
    - ${\color{orange}high52 : }$ `52 week's high price` of the share
    - ${\color{orange}pe : }$ `PE ratio` of the share

> [!CAUTION]
> * This is not the full code of the WebReader
> * This is not Offcial Code as Well or any kind of licensed by Google
> * No proper debugging & testing
