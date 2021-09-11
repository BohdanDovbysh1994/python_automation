from xml.etree import ElementTree

tree = ElementTree.parse("market.xml")
root = tree.getroot()

for movie in root.iter("movie"):
    print(movie.attrib["title"])

    for child in movie.findall("*"):
        print(child.text)
    print()
# print(ElementTree.tostring(root).decode())
