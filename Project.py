import uuid

class Project:
    __name = None
    __start_date =  None
    __end_date = None
    __id= None
    __description = None

    def __init__(self,name,start_date,end_date,description):
        self.__id=uuid.uuid1() #initiatize the the id for every project
        self.__name=name
        self.__start_date=start_date
        self.__end_date=end_date
        self.__description=description


    """ Properties
    """

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self,value):
        self.end_date=value

    @property
    def end_date(self):
        return self.__end_date
    @end_date.setter
    def end_date(self, value):
        self.end_date = value

    """
    dictionary like reperensentation of our object
    """
    def serialize(self):
        return {
            "name": self.name,
            "description":self.__start_date,
            "id": self.id,
            "start_date":self.__start_date,
            "end_date":self.end_date
        }