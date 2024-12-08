# Marvel Rivals Code Scraper

Scrapes some websites for free Marvel Rivals codes.

## Installation

```bash
pip install -r requirements.txt
```

## Usage
```bash
python rivals_code_scraper.py
```

## Adding Websites

To add a new website, you need the website's name, URL, and the HTML tags that contain the codes section.

1. Add the website's name and URL to the `URLS` dictionary in `rivals_code_scraper.py`.
2. Add the website's name and the some identifying property of an HTML element that contains the codes section to the `COMPONENTS` dictionary in `rivals_code_scraper.py`.
    a. **NOTE:** The property can be a class name, id, or any uniquely identifying attribute. It does not need to be the top level element, nor the direct parent.
3. Add the website's name and the index of the ul containing the codes section to the `UL_INDEXES` dictionary in `rivals_code_scraper.py`. For example, if the codes are listed in an unordered list that is the 3rd list in the component defined in step 2, then the value should be  `"FooBar": [2]`.

## Improvements
This is my first attempt at web scraping, so it is not the best. I already thought of some improvements. Feel free to submit a PR with any of the following:

- More flexible HTML parsing (i.e.: reading other types of tags)
- Functionality to send the codes to a Discord webhook.
- Functionality to send the codes to an email.
- A `CodeWebsite` class with attributes needed for scraping the website, as well as some easy interface for adding new websites.
