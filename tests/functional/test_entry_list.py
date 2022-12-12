import pytest


@pytest.mark.django_db
class TestEntryList:

    expected_status_code = 200

    def test_entry_page(self, client, entry_page):
        _, domain, path = entry_page.get_url_parts()
        rq = client.get(f"{domain}{path}")
        assert rq.status_code == self.expected_status_code
        assert entry_page.title in str(rq.content)

    def test_entry_page_author(self, client, blog_page, entry_page):
        _, domain, blog_path = blog_page.get_url_parts()
        rq = client.get(f"{domain}{blog_path}author/{entry_page.owner.username}/")
        assert rq.status_code == self.expected_status_code
        assert "Entries for author" in str(rq.content)

    def test_entry_page_category(self, client, blog_page, category):
        _, domain, blog_path = blog_page.get_url_parts()
        rq = client.get(f"{domain}{blog_path}category/{category.slug}/")
        assert rq.status_code == self.expected_status_code
        assert "Entries for category" in str(rq.content)

    def test_entry_page_tag(self, client, blog_page, tag):
        _, domain, blog_path = blog_page.get_url_parts()
        rq = client.get(f"{domain}{blog_path}tag/{tag.slug}/")
        assert rq.status_code == self.expected_status_code
        assert "Entries for tag" in str(rq.content)

    def test_entry_page_archive_year(self, client, blog_page, entry_page):
        _, domain, blog_path = blog_page.get_url_parts()
        rq = client.get(f"{domain}{blog_path}{entry_page.slug}/")
        assert rq.status_code == self.expected_status_code
        assert "Entries for date" in str(rq.content)

#
#     def test_entry_page_archive_year(self, browser, site_url):
#         browser.visit(site_url + '/blog/2016/')
#         entries = browser.find_by_css('.page-content')
#         assert browser.status_code == self.expected_status_code
#         assert browser.is_text_present('Entries for date')
#         assert len(entries) > 0
#
#     def test_entry_page_archive_year_month(self, browser, site_url):
#         browser.visit(site_url + '/blog/2016/08/')
#         entries = browser.find_by_css('.page-content')
#         assert browser.status_code == self.expected_status_code
#         assert browser.is_text_present('Entries for date')
#         assert len(entries) > 0
