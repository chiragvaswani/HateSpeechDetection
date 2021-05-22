import pipeline


text = "Explanation\r\nWhy the edits made under my username Hardcore Metallica Fan were reverted? They weren't vandalisms, just closure on some GAs after I voted at New York Dolls FAC. And please don't remove the template from the talk page since I'm retired now.89.205.38.27"
clean = pipeline.preprocess(text)
print(pipeline.text_classification(clean))
