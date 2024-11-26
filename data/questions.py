def get_image_url(index):
    return all_questions[index]["image_url"]
def get_answers(index):
    return all_questions[index]["answers"]


all_questions = (
    {"image_url" : "beach.jpg", "answers":(("sunset",10),("ocean",10),("sand",10),("coconut tree",20),
                                           ("mountains",10),("clouds",10))},
    {"image_url": "space2.jpg", "answers":(("stars",10), ("planet", 5), ("alien", 3),("asteroids",15),
                                                                                ("saturn",10))},
    {"image_url":  "fruitshop.png", "answers":(("pineapples",10),("baskets",10),("white bag",10),("trees",10),
                                               ("flower pots",10), ("plants",10),("clouds", 10),
                                               ("cucumbers",10), ("apples", 10),("grapes",5),("wheels",10))}
)


