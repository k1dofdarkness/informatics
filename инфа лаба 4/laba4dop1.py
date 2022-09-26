import yaml
import json
def main():
    with open("timetable.yml", 'r', encoding='utf-8') as yaml_in, open("out1.json", "w", encoding='utf-8') as json_out: 
        yaml_object = yaml.safe_load(yaml_in) 
        json.dump(yaml_object, json_out, ensure_ascii=False) 
main()
