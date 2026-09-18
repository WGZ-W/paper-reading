import unittest
from pathlib import Path
import tempfile

from watch_paper_links import (
    Paper,
    extract_venue,
    find_url_only_lines,
    format_entry,
    normalize_author_name,
    parse_arxiv_xml,
    parse_paper_html,
    process_markdown_file,
    select_display_authors,
)


class WatchPaperLinksTests(unittest.TestCase):
    def test_only_standalone_urls_outside_fences_are_selected(self):
        source = "\n".join(
            (
                "https://arxiv.org/abs/2402.15852",
                "  - https://openreview.net/forum?id=abc",
                "See https://example.com/paper here.",
                "- [NaVid](https://arxiv.org/abs/2402.15852)",
                "```markdown",
                "https://arxiv.org/abs/0000.00000",
                "```",
            )
        )
        candidates = find_url_only_lines(source)
        self.assertEqual(
            [(item.indentation, item.url) for item in candidates],
            [
                ("", "https://arxiv.org/abs/2402.15852"),
                ("  ", "https://openreview.net/forum?id=abc"),
            ],
        )

    def test_arxiv_xml_produces_requested_layout(self):
        source = """
        <feed xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <title>NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation</title>
            <author><name>Jiazhao Zhang</name></author>
            <author><name>He Wang</name></author>
            <published>2024-02-24T00:00:00Z</published>
            <arxiv:comment>Accepted by RSS 2024</arxiv:comment>
          </entry>
        </feed>
        """
        url = "https://arxiv.org/abs/2402.15852"
        self.assertEqual(
            format_entry(parse_arxiv_xml(source, url)),
            "- **NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation** & Jiazhao Zhang,  He Wang & **RSS 2024** & [Arxiv](https://arxiv.org/abs/2402.15852)",
        )

    def test_citation_meta_tags_can_have_any_attribute_order(self):
        source = """
        <html><head>
          <meta content="Example Paper" name="citation_title">
          <meta name="citation_author" content="Ada Lovelace">
          <meta content="Alan Turing" name="citation_author">
          <meta name="citation_conference_title" content="Computer Vision and Pattern Recognition 2026">
        </head></html>
        """
        paper = parse_paper_html(source, "https://example.com/paper")
        self.assertEqual(paper.title, "Example Paper")
        self.assertEqual(paper.authors, ["Ada Lovelace", "Alan Turing"])
        self.assertEqual(paper.venue, "CVPR 2026")

    def test_visible_arxiv_comments_supply_the_venue(self):
        source = """
        <html><head>
          <meta name="citation_title" content="NaVid">
          <meta name="citation_author" content="Jiazhao Zhang">
          <meta name="citation_date" content="2024/02/24">
        </head><body><td class="comments">Accepted by RSS 2024</td></body></html>
        """
        paper = parse_paper_html(source, "https://arxiv.org/abs/2402.15852")
        self.assertEqual(paper.venue, "RSS 2024")
        self.assertEqual(paper.label, "Arxiv")

    def test_venue_is_not_guessed_from_abstract_text(self):
        source = """
        <html><head>
          <meta name="citation_title" content="Example Paper">
          <meta name="citation_author" content="First Author">
          <meta name="citation_date" content="2026/01/02">
        </head><body>This method evaluates a CVPR benchmark.</body></html>
        """
        paper = parse_paper_html(source, "https://arxiv.org/abs/2601.00001")
        self.assertEqual(paper.venue, "Arxiv")

    def test_two_digit_venue_year_is_normalized(self):
        self.assertEqual(extract_venue("To appear at CoRL '25"), "CoRL 2025")

    def test_only_first_and_last_authors_are_displayed(self):
        authors = ["First Author", "Second Author", "Corresponding Author"]
        self.assertEqual(
            select_display_authors(authors),
            ["First Author", "Corresponding Author"],
        )
        paper = Paper(
            "Example", authors, "CVPR 2026", "https://example.com/paper", "Paper"
        )
        self.assertEqual(
            format_entry(paper),
            "- **Example** & First Author,  Corresponding Author & **CVPR 2026** & "
            "[Paper](https://example.com/paper)",
        )

    def test_comma_separated_metadata_name_is_written_given_name_first(self):
        self.assertEqual(normalize_author_name("Zhang, Jiazhao"), "Jiazhao Zhang")
        paper = Paper(
            "Example",
            ["Zhang, Jiazhao", "Wang, He"],
            "RSS 2024",
            "https://example.com/paper",
            "Paper",
        )
        self.assertIn("Jiazhao Zhang,  He Wang", format_entry(paper))

    def test_one_or_two_authors_are_not_duplicated(self):
        self.assertEqual(select_display_authors(["Only Author"]), ["Only Author"])
        self.assertEqual(
            select_display_authors(["First Author", "Second Author"]),
            ["First Author", "Second Author"],
        )

    def test_arxiv_without_explicit_venue_is_not_given_an_invented_venue(self):
        source = """
        <feed xmlns:arxiv="http://arxiv.org/schemas/atom">
          <entry>
            <title>Example Paper</title>
            <author><name>First Author</name></author>
            <author><name>Last Author</name></author>
            <published>2026-01-02T00:00:00Z</published>
          </entry>
        </feed>
        """
        paper = parse_arxiv_xml(source, "https://arxiv.org/abs/2601.00001")
        self.assertEqual(paper.venue, "Arxiv")
        self.assertIn("First Author,  Last Author", format_entry(paper))
        self.assertNotIn("Arxiv 2026", format_entry(paper))

    def test_empty_venue_is_rendered_as_arxiv(self):
        paper = Paper(
            "Example", ["First Author"], "", "https://example.com/paper", "Paper"
        )
        self.assertIn("& **Arxiv** &", format_entry(paper))

    def test_processing_preserves_utf16_and_trailing_blank_lines(self):
        url = "https://example.com/paper"
        paper = Paper("Example", ["Ada Lovelace"], "CVPR 2026", url, "Paper")
        original = "# Papers\r\n" + url + "\r\n\r\n"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "papers.md")
            path.write_bytes(b"\xff\xfe" + original.encode("utf-16-le"))
            changed = process_markdown_file(path, {url: paper})
            payload = path.read_bytes()

        self.assertEqual(changed, 1)
        self.assertTrue(payload.startswith(b"\xff\xfe"))
        self.assertEqual(
            payload[2:].decode("utf-16-le"),
            "# Papers\r\n"
            "- **Example** & Ada Lovelace & **CVPR 2026** & "
            "[Paper](https://example.com/paper)\r\n\r\n",
        )


if __name__ == "__main__":
    unittest.main()
