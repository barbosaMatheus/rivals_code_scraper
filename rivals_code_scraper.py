import requests
import bs4

# mapping of website name to url
URLS = {"GamesRadar": "https://www.gamesradar.com/games/third-person-shooter/marvel-rivals-codes-redeem/",
        "IGN": "https://www.ign.com/articles/marvel-rivals-codes",
        "Polygon": "https://www.polygon.com/marvel-rivals-guide/492083/codes-list-redeem-costumes-skins"}

# maps website name to class name or id of component 
# containing the codes section in the page
COMPONENTS = {"GamesRadar": {"class": "wcp-item-content"},
              "IGN": {"class": "jsx-3517015813 article-content page-0"},
              "Polygon": {"id": "zephr-anchor"}}

# maps website name to indexes of uls containing the codes
# 0 is the first ul under the div defined in COMPONENTS
UL_INDEXES = {"GamesRadar": [1],
             "IGN": [0],
             "Polygon": [0]}

for name, url in URLS.items():
    req = requests.get(url)
    print("==================================================")
    print(f"{name}:")
    if req.status_code == 200:
        page = bs4.BeautifulSoup(req.text, "html.parser")
        try:
            main_text = page.find("div", COMPONENTS[name])
            uls = main_text.find_all("ul")
            for index in UL_INDEXES[name]:
                for li in uls[index].find_all("li"):
                    print(f"-> {li.text.strip()}")
        except AttributeError as attr_err:
            print(f"AttributeError while parsing webpage request, check the values" +
                  f" in the dictionaries COMPONENTS and UL_INDEXES:\n{attr_err}")
    else:
        print(f"Failed to fetch data from {name}\nStatus code: {req.status_code}\nURL: {url}")
    print("==================================================\n")
