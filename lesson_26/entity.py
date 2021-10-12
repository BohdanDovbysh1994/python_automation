class Entity:
    def to_dict(self):
        data = {}

        for key, value in self._vals_.items():
            data[key] = value

        return data
