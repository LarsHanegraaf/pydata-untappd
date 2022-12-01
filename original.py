import requests
import pandas as pd
from bs4 import BeautifulSoup

EINDHOVEN_TASTING_ROOMS = [
    "Rabauw",
]


def main():
    # Get the data
    parsed_beers = []
    for brewery in EINDHOVEN_TASTING_ROOMS:
        url = f"https://untappd.com/{brewery}/beer"
        headers = {"User-Agent": "PyData example app"}
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        beers = soup.find_all("div", class_="beer-item")

        for beer in beers:
            parsed_beer = dict()
            parsed_beer["name"] = beer.find("p", class_="name").find("a").text.strip()
            parsed_beer["style"] = beer.find("p", class_="style").text.strip()
            parsed_beer["abv"] = beer.find("div", class_="abv").text.strip()
            parsed_beer["rating"] = beer.find("div", class_="caps")["data-rating"]
            parsed_beer["num_ratings"] = beer.find("div", class_="raters").text.strip()
            parsed_beer["brewery"] = brewery
            parsed_beers.append(parsed_beer)

    # Transform the data
    df = pd.DataFrame(parsed_beers)

    df["abv"] = df["abv"].str.replace("% ABV", "").astype("float")
    df["rating"] = df["rating"].astype("float")
    df["num_ratings"] = (
        df["num_ratings"].str.replace(" Ratings", "").str.replace(",", "").astype("int")
    )
    df[["style", "subtype"]] = df["style"].str.split("-", n=1, expand=True)
    df = df.loc[df["num_ratings"] > 1000]

    df_grouped = df.groupby("style").mean()
    df_grouped = df_grouped.sort_values(by="rating", ascending=False)

    # Write result
    df_grouped.to_csv("beers.csv")


if __name__ == "__main__":
    main()
