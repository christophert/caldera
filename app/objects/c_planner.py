from app.utility.base_object import BaseObject


class Planner(BaseObject):

    @property
    def unique(self):
        return self.hash(self.name)

    @property
    def display(self):
        return dict(name=self.name, module=self.module, params=self.params, description=self.description)

    def __init__(self, name, module, params, description=None):
        super().__init__()
        self.name = name
        self.module = module
        self.params = params
        self.description = description

    def store(self, ram):
        existing = self.retrieve(ram['planners'], self.unique)
        if not existing:
            ram['planners'].append(self)
            return self.retrieve(ram['planners'], self.unique)
        return existing
