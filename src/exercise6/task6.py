import json


def get_films(path='input.txt'):
    try:
        with open(path, 'r', encoding="UTF-8") as data:
            content = data.read().strip()
            if not content:
                print("Empty file")
                return None

            return json.loads(content)

    except FileNotFoundError:
        print("Error: input.txt not found")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON")
        return None


def merge_movie_lists(data):
    try:
        if not isinstance(data, dict) or 'list1' not in data or 'list2' not in data:  # Validation
            print("Error: Invalid input format. Expected two lists in a dictionary.")
            return

        lst1 = data['list1']
        lst2 = data['list2']

        # Combine and sort based on 'year'
        merged_list = sorted(lst1 + lst2, key=lambda x: x['year'])

        print(json.dumps(merged_list, indent=4, ensure_ascii=False))

    except KeyError:
        print("Error: Missing 'year' key in movie data")


if __name__ == "__main__":
    movies_data = get_films()
    if movies_data:
        merge_movie_lists(movies_data)
