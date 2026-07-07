import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        # Abre o arquivo em modo de escrita binária (wb) e joga o dicionário lá dentro
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        # Abre o arquivo em modo de leitura binária (rb) e carrega para o dicionário
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump() # Salva no arquivo sempre que adicionar algo novo

    def get(self, key):
        try:        
            return self.__cache[key]
        except KeyError:
            return None

    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() # Salva no arquivo sempre que remover
        except KeyError:
            pass

    def get_all(self):
        return list(self.__cache.values())