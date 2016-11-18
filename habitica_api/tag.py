from . import API


class Tag(object):
    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])

    @classmethod
    def new(cls, name):
        data = {'name': name}
        new_tag = API.Tag.create(data)
        if new_tag is not None:
            return cls(**new_tag)
        else:
            return None

    def delete(self):
        API.Tag.delete(self.id)

    def rename(self, new_name):
        data = {}
        data['name'] = new_name
        update = API.Tag.update(self.id, data)
        for attr in update:
            setattr(self, attr, update[attr])


class Tags(object):
    def __init__(self):
        self.tags = []
        data = API.Tag.get_all()
        for tag in data:
            self.tags.append(Tag(**tag))

    def __iter__(self):
        for t in self.tags:
            yield t

    def __len__(self):
        return len(self.tags)
