import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", text_type_bold)
		node2 = TextNode("This is a text node", text_type_bold)

		self.assertEqual(node, node2)

	def test_no_url(self):
		node = TextNode("This is a text node", text_type_italic, "www.website.com")
		node2 = TextNode("This is a text node", text_type_italic)

		self.assertNotEqual(node, node2)
	
	def test_neq(self):
		node = TextNode("This is not a text node", text_type_text)
		node2 = TextNode("This is a text node", text_type_text)

		self.assertNotEqual(node, node2)

if __name__ == "__main__":
	unittest.main()