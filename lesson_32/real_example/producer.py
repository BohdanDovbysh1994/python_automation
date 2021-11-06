from json import dumps

for _ in range(1000000):
    name = f"report_{_}.json"
    report = dumps(
        {
            "name": f"test_{_}",
            "result": "Pass"
        }
    )
    with open(f"lesson_32/real_example/reports/{name}", "w") as file:
        file.write(report)
    