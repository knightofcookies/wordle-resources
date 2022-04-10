# import json

# with open("words.json", "rt") as jsonContent:
# 	dictionaryFromJSON = json.load(jsonContent)

# i = 1
# for key in dictionaryFromJSON.keys():
# 	dictionaryFromJSON[key] = i
# 	i += 1

# dictionaryFromJSON = {value:key for key, value in dictionaryFromJSON.items()}
# newJSONContent = json.dumps(dictionaryFromJSON)
# newJSONFile = open("words_updated.json", "wt")
# newJSONFile.write(newJSONContent)

# with open("words_updated.json", "rt") as jsonFile:
# 	dictionaryFromJSON = json.load(jsonFile)

# wordleDict = {}
# i = 1

# for key in dictionaryFromJSON.keys():
# 	if len(dictionaryFromJSON[key]) == 5:
# 		wordleDict[i] = dictionaryFromJSON[key]
# 		i += 1

# with open("wordle_words_list.json", "wt") as newFile:
# 	newJSONFile = json.dump(wordleDict, newFile, indent="")
