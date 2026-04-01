from django.test import TestCase
from django.urls import reverse
from common.templatetags.codex_extras import runeify

class CodexExtrasTests(TestCase):
    def test_runeify_with_normal_string(self):
        result = runeify("Silver Sword")
        self.assertEqual(result, "† Silver Sword †")

    # test if the filter handles empty strings safely
    def test_runeify_with_empty_string(self):
        result = runeify("")
        self.assertEqual(result, "")

    # tests if the filter handles none safely
    def test_runeify_with_none(self):
        result = runeify(None)
        self.assertEqual(result, "")

class CommonViewTests(TestCase):
    # tests if the home page loads successfully (200 OK)
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # tests if the home page uses the correct template
    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'common/home.html')


class MiddlewareTests(TestCase):
    def test_witcher_audit_middleware_adds_header(self):
        response = self.client.get(reverse('home'))

        # check if the custom header exists in the response
        self.assertEqual(response.get('X-Codex-Version'), '1.0-Witcher-Edition')