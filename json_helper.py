import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def read_all_json_files(JSON_ROOT):
    for direpath, direnames, filenames in os.walk(JSON_ROOT):
        result = []
        for f in filenames:
            if f.endswith('.json'):
                json_content_2 = read_json(os.path.join(JSON_ROOT,f))
                for i in json_content_2["results"]:
                    result.append(i)
        df = pd.DataFrame(result)
        return df


