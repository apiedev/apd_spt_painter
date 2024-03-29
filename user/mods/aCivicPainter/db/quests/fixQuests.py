import json, glob

files = glob.glob('./*.json', recursive=True)

for f in files:
    with open(f, 'r') as fi:

        try:
            json_file = json.load(fi)
            questCounter = 0

            for quest in json_file:
                print("Here!")
                
                totalConditions = len(quest["conditions"]["AvailableForFinish"])

                newQuest = quest
                newQuest.conditions.AvailableForFinish.clear()
                newQuest.conditions.AvailableForStart.clear()

                conditionCounter = 0

                for fin in quest.get("conditions").get("AvailableForFinish"):

                    newQuest.get("conditions").get("AvailableForFinish")[conditionCounter] = {
                        "conditionType": fin._parent,
                        "dogtagLevel": fin._props.dogtagLevel,
                        "dynamicLocale": fin.dynamicLocale,
                        "globalQuestCounterId": "",
                        "id": fin._props.id,
                        "index": fin._props.index,
                        "isEncoded": false,
                        "maxDurability": fin._props.maxDurability,
                        "minDurability": fin._props.minDurability,
                        "onlyFoundInRaid": fin._props.onlyFoundInRaid,
                        "parentId": fin._props.parentId,
                        "target": fin._props.target,
                        "value": fin._props.value,
                        "visibilityConditions": fin._props.visibilityConditions  
                    }

                    conditionCounter += 1

                conditionCounter = 0

                for fin in quest.get("conditions").get("AvailableForStart"):
                    newQuest.get("conditions").get("AvailableForStart")[conditionCounter] = {
                        "compareMethod": fin._props.compareMethod,
                        "conditionType": fin._parent,
                        "dynamicLocale": fin.dynamicLocale,
                        "globalQuestCounterId": "",
                        "id": fin._props.id,
                        "index": fin._props.index,
                        "parentId": fin._props.parentId,
                        "value": fin._props.value,
                        "visibilityConditions": fin._props.visibilityConditions
                    }

                    conditionCounter += 1

                json_file[questCounter] = newQuest
                questCounter += 1

            print(json_file)
        except KeyError:
            print(f'Skipping {f}')
