import re


text = """<div id="some">Some</div>
<div id="ololo">Ololo</div>
"""

print(re.findall(r"div id=\"(.+)\">(.+)<", text))
