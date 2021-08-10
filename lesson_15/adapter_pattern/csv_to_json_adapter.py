from typing import List, Dict


class CSVToJsonAdapter:
    def __init__(self, headers: str, data: List[str]):
        self.__headers = headers
        self.__data = data

    def get_json(self) -> List[Dict]:
        headers: List[str] = self.__headers.split(',')
        users_data: List[List[str]] = []

        for row in self.__data:
            user_data = row.split(',')
            users_data.append(user_data)

        result = []

        for user_data in users_data:
            result.append(dict(zip(headers, user_data)))

        return result
