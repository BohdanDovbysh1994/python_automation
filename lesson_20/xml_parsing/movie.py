from __future__ import annotations

from typing import List
from xml.etree import ElementTree


class Movie:
    def __init__(
        self,
        title: str,
        format: str,
        year: int,
        rating: str,
        description: str,
        category: str,
    ):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path: str) -> List[Movie]:
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []

        for category in collection:
            for decade in category:
                for movie in decade:
                    cls(
                        movie.attrib["title"])

if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")