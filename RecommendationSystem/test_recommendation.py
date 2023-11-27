import unittest

recommend_restaurants = []

class RestaurantRecommendationTest(unittest.TestCase):

    def test_valid_cuisine(self):
        recommendations = recommend_restaurants("Italian")
        self.assertEqual(recommendations, ["Restaurant A"])

    def test_invalid_cuisine(self):
        recommendations = recommend_restaurants("French")
        self.assertEqual(recommendations, [])

    def test_empty_data(self):
        restaurant_data = []
        recommendations = recommend_restaurants("Chinese")
        self.assertEqual(recommendations, [])

if __name__ == "__main__":
    unittest.main()