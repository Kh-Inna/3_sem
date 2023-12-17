import tests
import unittest
suite = unittest.TestLoader().loadTestsFromModule(tests)
results = unittest.TextTestRunner(verbosity=2).run(suite)