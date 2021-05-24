import Helper as h
import cv2


# classifying image
img = cv2.imread('ViolenceDetectionTest.jpeg')
print(h.image_classification(img))


# classifying text
text = "Before you start throwing accusations and warnings at me, lets review the edit itself-making ad hominem attacks isn't going to strengthen your argument, it will merely make it look like you are abusing your power as an admin.Now, the edit itself is relevant-this is probably the single most talked about event int he news as of late. His absence is notable, since he is the only living ex-president who did not attend. That's certainly more notable than his dedicating an aircracft carrier.I intend to revert this edit, in hopes of attracting the attention of an admin that is willing to look at the issue itself, and not throw accusations around quite so liberally. Perhaps, if you achieve a level of civility where you can do this, we can have a rational discussion on the topic and resolve the matter peacefully."
cleaned = h.preprocess(text)
print(cleaned)
print(h.text_classification(cleaned))
