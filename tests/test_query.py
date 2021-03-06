from unittest import TestCase

from pyrestorm.query import RestQueryset

from .models import Post, Gene


class RestQuerysetTestCase(TestCase):
    def test_init(self):
        RestQueryset(Post)

    def test_getitem(self):
        queryset = RestQueryset(Post)
        self.assertEqual(queryset[0].id, 1)

    def test_len(self):
        queryset = RestQueryset(Post)
        self.assertEqual(len(queryset), 100)

    def test_repr(self):
        queryset = RestQueryset(Post)
        repr(queryset)
        self.assertTrue(True)

    def test_unicode(self):
        queryset = RestQueryset(Post)
        unicode(queryset)

    def test_iter(self):
        queryset = RestQueryset(Post)
        for item in queryset:
            self.assertTrue(True)

    def test_none(self):
        queryset = RestQueryset(Post).none()
        self.assertIsNone(queryset)


class RestPaginatedQuerysetTestCase(TestCase):
    def test_init(self):
        RestQueryset(Gene)

    def test_index(self):
        gene = RestQueryset(Gene)[40]
        self.assertTrue(isinstance(gene, Gene))

    def test_slice(self):
        genes = RestQueryset(Gene)[0:40]
        self.assertEqual(len(genes), 40)

    def test_evaluate_invalid_bounds(self):
        queryset = RestQueryset(Gene)
        self.assertRaises(ValueError, queryset.__getitem__, slice(5, 3))
        queryset._paginator.max = 10
        queryset[0:11]
