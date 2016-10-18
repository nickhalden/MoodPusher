
class Experience:
    __domain = None
    __years = None
    __projects = None

    def __init__(self,domain,years,projects):
        self.__domain = domain
        self.__projects= projects
        self.__years=years

    @property
    def domain(self):
        return self.__domain

    @property
    def years(self):
        return self.__years

    @property
    def projects(self):
        return self.__projects

    @domain.setter
    def domain(self,value):
        self.__domain=value
    @years.setter
    def years(self, value):
        self.__years = value
    @projects.setter
    def projects(self, value):
        self.__projects = value

    def serialize(self):
        return {
            "domain":self.domain,
            "years":self.years,
            "projects": [ prj.serialize() for prj in self.projects]
        }
