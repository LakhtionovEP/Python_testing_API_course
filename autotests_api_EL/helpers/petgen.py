import random


class PetgenHelper():
    @staticmethod
    def create_pet():
        id = random.randint(1, 100)
        category_id = random.randint(1, 100)
        category = "test"
        name = "test"
        photoUrls = "test"
        tags_id = random.randint(1, 100)
        tags = "test"
        status = "available"
        return id, category_id, category, name, photoUrls, tags_id, tags, status
