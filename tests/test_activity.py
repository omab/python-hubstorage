"""
Test Activty
"""
from hstestcase import HSTestCase


class ActivityTest(HSTestCase):

    def test_post_and_reverse_get(self):
        # make some sample data
        orig_data = [dict(foo=42, counter=i) for i in xrange(20)]
        data1 = orig_data[:10]
        data2 = orig_data[10:]

        # put ordered data in 2 separate posts
        self.project.activity.post(data1)
        self.project.activity.post(data2)

        # read them back - activity should be second request first (reverse chronological order)
        result = list(self.project.activity.get(count=20))
        self.assertEqual(len(result), 20)
        reconstructed = result[10:] + result[:10]
        self.assertEqual(orig_data, reconstructed)

    def test_filters(self):
        self.project.activity.post({'c': i} for i in xrange(10))
        r = list(self.project.activity.get(filter='["c", ">", [5]]', count=2))
        self.assertEqual(r, [{'c': 6}, {'c': 7}])
