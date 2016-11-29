import unittest
from mongo_persist import MongoPersist
import test_memory_persist

class TestMongoPersist(test_memory_persist.TestMemoryPersist):
    def get_persist(self):
        return MongoPersist(dbname='test_loyalty', clear_old = True)
