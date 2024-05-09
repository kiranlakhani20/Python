import unittest

def execute_query(query):
    # Dummy implementation for testing
    if "DROP" in query:
        return "Query contains DROP statement"
    else:
        return "Query executed successfully"

class TestExecuteQuery(unittest.TestCase):
    def test_query_execution(self):
        query = "SELECT * FROM users WHERE username = 'Alice';"
        result = execute_query(query)
        self.assertEqual(result, "Query executed successfully")

    def test_query_exploitation_attempt(self):
        query = "SELECT * FROM users WHERE username = 'Alice'; DROP TABLE users;"
        result = execute_query(query)
        self.assertNotEqual(result, "Query contains DROP statement")

if __name__ == '__main__':
    unittest.main()
