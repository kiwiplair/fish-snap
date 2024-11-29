def get_image_url(index):
    return all_questions[index]["image_url"]
def get_answers(index):
    return all_questions[index]["answers"]


all_questions = (
    {"image_url": "beach.jpg", "answers": (("sunset",10),("ocean",10),("sand",10),("coconut tree",20),
                                           ("mountains",10),("clouds",10))},
    {"image_url": "space2.jpg", "answers": (("stars",10), ("planet", 5), ("alien", 3),("asteroids",15),
                                                                                ("saturn",10))},

    {"image_url":  "messytable.jpg", "answers":(("table", 10), ("chair", 10), ("papers", 10), ("computer", 10),

("bed", 5), ("posters", 15), ("books", 15),("shelf",15))},
    {"image_url":  "bread1.jpg", "answers":(("bread", 5), ("toaster", 10), ("jam", 15), ("egg", 5),

("tulips", 10), ("strawberries", 15), ("lettuce", 15),("ham",15),("tangerine",10),("sugar",10),("tea",10)

                                            ,("sausage",10),("tomato sauce",20),("ribbon",20),("knife",20))},


    {"image_url": "balcony.jpg","answers":(("mushroom",10),("dog",10),("tomato",15),("chilli",15),("lotus",20),
                                           ("peas",20),("flower",15),("butterfly",20),("frog",20),("broom",10))}
,  {"image_url": "Rabbit.jpg","answers":(("rabbits",10),("cake",10),("bread",15),("hat",15),("brush",20),
                                           ("mouse",20),("chicks",15),("flower",20),("bow",20),("egg",20))},
 {"image_url": "mouse.jpg","answers":(("mushroom",10),("pot",10),("clothes",15),("bucket",15),("ladder",20),
                                           ("firefly",20),("bubbles",15),("tree",20),("rope",15),("broom",10))}
,{"image_url": "christmas.jpg","answers":(("basket",15),("pot",10),("christmas tree",15),("bell",15),
                                          ("earthworm",20),
                                           ("girl",10),("rabbit",15),("snowman",20),("cat",15),("2021",10))})






