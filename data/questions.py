def get_image_url(index):
    return all_questions[index]["image_url"]
def get_answer(index):
    return all_questions[index]["answers"]

all_questions = (
    ("beach.jpg","sunset","ocean","coconut tree","sand","mountains","clouds"),
    ("space2.jpg","stars", "planet","alien","flag","asteroids","saturn"),

)

all_questions = (
    {"image_url" : "beach.jpg", "answers":(("sunset",10),("ocean",10),("sand",10),("coconut tree",10),
                                           ("mountains",10),("clouds",20))},
    {"image_url": "space2.jpg", "answers":(("stars",10), ("planet", 5), ("alien", 3),("asteroids",15),
                                           ("saturn",10))}

)


