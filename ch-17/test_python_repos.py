# Number of items in self.response returned is what is expected

# Total num of repos is greater than a certain amount
from  python_repos import *
import  unittest

class TestRequests(unittest.TestCase):
    # NOTE: Each method *must* begin with 'test' or it won't run!
    resp = get_repos('python')

    def test_status_code(self):
        """The HTTP get request should return a code of 200."""
        self.assertEqual(check_status(self.resp), 200)

    def test_check_items_length(self):
        """Check that we get at 30 repos that match our criteria."""
        self.assertEqual(check_repo_amount(self.resp), 30)

    def test_response_keys(self):
        """Check that certain keys are present in repo JSON."""
        self.assertEqual(' '.join(response_keys(self.resp)), ' '.join(['total_count', 'incomplete_results', 'items']))
    
    def test_total_repos_count(self):
        """Should return an integer of 0 or greater"""
        self.assertGreaterEqual(total_repos(self.resp), 0)
    
    def test_repo_amount(self):
        """Should return up to 30 repos and no more."""
        self.assertLessEqual(check_repo_amount(self.resp), 30)
    
    def test_repo_keys(self):
        """Should return a tuple with length and list of keys for a repo."""
        first_repo = self.resp.json()['items'][0]
        self.assertEqual(repo_keys(first_repo)[0].__class__.__name__, 'int')
        self.assertEqual(repo_keys(first_repo)[1].__class__.__name__, 'list')


if __name__ == '__main__':
    unittest.main()
