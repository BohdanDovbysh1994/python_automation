import yaml

# with open("data.yaml") as yaml_file:
#     data = yaml.safe_load(yaml_file)
#
# print(data)


data = {
    "services": [
        {
            "postgres": {
                "port": 5432,
                "db": "postgres",
                "password": "postgres"
            },
            "mongo_db": {
                "port": 7321,
                "schema": "users",
                "password": "super_password"
            }
        }
    ],
    "aws_access_key": "askdfhjlaskjdfhlaskdjhflajksdhf"
}

with open("new_yaml.yaml", "w") as file:
    yaml.dump(data, file)
