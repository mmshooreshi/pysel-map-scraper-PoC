# pysel-map-scraper   ✨ ![LoopGif3](https://cultofthepartyparrot.com/parrots/hd/parrot.gif)




![LoopGif2](https://media.giphy.com/media/sltXBTQh2ogIFYwNNk/giphy.gif)



![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![PoC](https://img.shields.io/badge/PoC-Proof--of--Concept-3EE9A1?style=for-the-badge&logo=selenium&logoColor=white) 

#### This project is more of a Proof-of-Concept than something for production use.  (´ｰ｀ )ﾉ 🔫

# Table of contents
- [Markdown Badges](#markdown-badges)
- [Table of contents](#table-of-contents)
- [Usage](#usage)
- [Tips](#tips)
- [Contribution](#contribution)
- [License](#license)
- [Badges](#badges)


## Open to any Contributions

<small>_may the source be with you!_<small>
contribution file [file](./CONTRIBUTING.md)


## Contact

You can reach me on [Telegram @forthetim6being](https://t.me/forthetim6being)

## License

[![Licence](https://img.shields.io/github/license/mmshooreshi/pysel-map-scraper-PoC?style=for-the-badge)](./LICENSE)
<hr>


                  
#   ⚡                      
┌┬────────────────┐
││General Features│
└┴────────────────┘
 ▼🚶
 🜚 Scraping google places using Selenium Python in a simple approach.
 🜚 No need to google maps API
 🜚 No need of any scrolling on the google maps sidebar or handling the pagination
 🜚 In case of URL redirecting triggered by google maps, It continue the scraping process from the last place it has been scraped, after it reloaded the page.
 🜚 Predefined scraping track as a GEOJSON file, define the movement route of the scraper on the map.
 🜚 Each time the app start to move in the ❮☡ GEOJSON file❯, it reads the customized search queries and map zooms from the CSV input file. as there may be more than a single query, It may repeat the track for any query and map zoom once it finished the track.

```
,
|'.
|_ r
  ⁮\\
   `
```

 
# two

<details>
 <summary>
  <p> 
 
   
   
  </p>
 </summary>
<p>

 
</p>
</details>





```{r df-drop-ok, class.source="bg-success"}
mtcars[1:5, "mpg", drop = FALSE]
```



```{css, echo=FALSE}
.scroll-100 {
  max-height: 100px;
  overflow-y: auto;
  background-color: inherit;
}
```

```{r, class.output="scroll-100"}
print(mtcars)
```
 
---

⧆ Why?
When your money value become close to zero in the real world outside your country, google APIs may not be in your options as a hobbyist data enthusiast.
this project may be beneficial for small projects, looking to a fast and easy way to look around the local places data. 💸🔰⊞ ⊟ ⊠ ⊡ ⚿ ⛝ ❎ ⟎ ⟏ ⧄ ⧅ ⧆ ⧇ ⧈ ⸬☻ 

---

⚅ What's new?
Previous open-source selenium tools have been mostly based on scrolling on the google maps paginated sidebar of places and scrape the data. However, in this project, google places information are extracted from the local storage of the browser directly with using the content scripts of the GPlaces-get extension, as another open-source project on JavaScript. So without the use of any google APIs, map viewport gets moving and moving on the predefined route and extracts the places data as CSV files for every <n> scraped places (default: 100).

---

 ＊ Get started:
pysel-map-scraper get's moving on the map based on the GEOJSON file defining the route (INPUT-ROUTE.geojson). It run the procedure of scraping for each of search queries in the CSV input file (INPUT-queries.csv), And restart the route once each query finished. The app triggers "search this area" button every time gets to a new viewport. GPlaces-get is writing all the data on CSV files and exporting them automatically, whenever it stores 100 new places (and also you may customize this).
anytime you run the app, it uses the stored logs and gets able to continue the process from the last location&query it has been scraped.  

---

![LoopGif1](https://media.giphy.com/media/D1BbNdibKVeuBZAAJT/giphy.gif)

 Scraped fields for each place:

 UUID | Created_at | Query | *Full address* | `Local name` | **Local full address**
 Latitude & Longitude | Categories | Reviews | Rating | URL | Domain
 Thumbnail | Addr1 | Addr2 | Addr3 | Addr4 | District
 Timezone
 
 ❨UUID❩
❬Created_at❭
❲  

Query
Name
Full address
Local name
Local full address
Phone number(s)
Latitude & Longitude
Categories
Reviews
Rating
URL
Domain
Thumbnail
Addr1 | Addr2 | Addr3 | Addr4
District
Timezone
🗒 📓 📔 📝 📒 📋📎 🖇

---
 ⚙
Get started
1. Clone this repository.
2. 📎 ❮GPlaces-get.crx❯ ❳❪ ❫ ❴ ❵ ❬ ❭ ❮ ❯ ❰ ❱  ➜  . / pysel-map-scraper-SOC / [move to here]
Either download the GPlaces-get.crx or clone it's repository and export it to CRX using google chrome extensions developer tools (or other applicable tools).
3. donwload the latest chromedriver (which is also open-source) for your operating system from the link below:
https://browsers.chromedriver.chromium.org
It is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.  ChromeDriver is a standalone server that implements the W3C WebDriver standard, and is available for Chrome on Android and Chrome on Desktop (Mac, Linux, Windows and ChromeOS).
