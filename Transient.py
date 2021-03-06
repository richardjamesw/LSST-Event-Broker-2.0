from Observation import Observation


class Transient:
    # variables

    def __init__(self, loc, cat):
        self.__location = loc
        self.__category = cat
        self.__observations = []

    def get_loc(self):
        return self.__location

    def get_cat(self):
        return self.__category

    def add_observation(self, time, loc, mag):
        obs = Observation(time, loc, mag)
        self.__observations.append(obs)

    def add_observation2(self, observation):
        self.__observations.append(observation)

    def get_observation(self):
        return self.__observations
