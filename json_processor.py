import json


def process_and_sort_json(raw_message):
    try:

        json_string = raw_message.decode('utf-8')
        json_data = json.loads(json_string)
        data = json_data.get('nodeInstances')

        processed_data = [
            {
                "nodeName": item.get("nodeName"),
                "nodeDefinitionType": item.get("nodeDefinitionType"),
                "error": item.get("error"),
                "state": item.get("state"),
                "creationOrder": item.get("creationOrder"),
            }
            for item in data
        ]

        sorted_data = sorted(processed_data, key=lambda x: x["creationOrder"])

        return sorted_data

    except json.JSONDecodeError:
        print("Invalid JSON")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []