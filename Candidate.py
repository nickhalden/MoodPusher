class Candidate:
    __first_name=None
    __last_name= None
    __experience=[]


    def __init__(self,first_name,last_name, experience = []):
        self.__first_name=first_name
        self.__experience=experience
        self.__last_name=last_name

    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def experience(self):
        return self.__experience


    @first_name.setter
    def first_name(self,value):
        self.__first_name=value
    @last_name.setter
    def last_name(self,value):
        self.__last_name= value
    @experience.setter
    def experience(self,value):
        self.__experience= value

    def serialize(self):
        return {
            "firstname": self.__last_name,
            "lastname" : self.__last_name,
            "experience": [exp.serialize() for exp in self.experience]
        }
    def add_experience(self,value):
        self.experience.append(value)







