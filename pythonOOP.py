import _ctypes


class Person:
    def __init__(self, surname, forename, old):
        self.__surname = surname
        self.__forename = forename
        self.__old = old

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @property
    def forename(self):
        return self.__forename

    @forename.setter
    def forename(self, forename):
        self.__forename = forename

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old



p = [Person("Ivanov", "Ivan", 19),
     Person("Marta", "Praska", 24),
     Person("Kirilov", "IVan", 20),
     Person("Pasha", "Kk", 41),
     Person("Andrii", "Fesh", 20)]


class SortKey:
    def __init__(self, listObj):
        self.__listObj = listObj

    def __call__(self, *args):
        d = {}
        for value in args:
            for obj in self.__listObj:
                d.update({id(obj): getattr(obj, value)})
            d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
            self.__listObj = []
            for obj_id in d.keys():
                self.__listObj.append(_ctypes.PyObj_FromPtr(obj_id))
        return self.__listObj


