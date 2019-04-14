from app.models import Article,Source
from unittest import TestCase

class TestSource(TestCase):
    def setUp(self):
        self.source=Source("BuzzFeed","BuzzFeed is a cross-platform")

    def test_instance(self):
        self.assertIsInstance(self.source,Source)

    def test_create(self):
        self.assertEqual(self.source.name,"BuzzFeed")
        self.assertEqual(self.source.description,
        "BuzzFeed is a cross-platform"
        )

class TestArticle(TestCase):
    def setUp(self):
        self.article=Article(
            "title","urlToImage","description","url","author"
        )
    def test_instance(self):
        self.assertIsInstance(self.article,Article)
    def test_create(self):
        self.assertEqual(self.article.title,"title")
        self.assertEqual(self.article.description,
        "description"
        )

if __name__ == '__main__':
    unittest.main()