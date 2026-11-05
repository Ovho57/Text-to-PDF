import tempfile
import unittest
from pathlib import Path

import text_to_pdf


class TextToPDFTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "sample.txt"
        self.source.write_text(
            "Hello\n  indented text\n" + ("long line " * 100) + "\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_successful_conversion(self):
        output = self.root / "sample.pdf"
        text_to_pdf.convert(self.source, output)
        self.assertTrue(output.exists())
        self.assertGreater(output.stat().st_size, 100)
        self.assertTrue(output.read_bytes().startswith(b"%PDF"))

    def test_save_folder_created(self):
        folder = self.root / "new" / "nested"
        output = text_to_pdf.resolve_output(self.source, folder, None)
        text_to_pdf.convert(self.source, output)
        self.assertTrue(folder.is_dir())
        self.assertTrue((folder / "sample.pdf").exists())

    def test_output_path_selection(self):
        folder = self.root / "pdfs"
        result = text_to_pdf.resolve_output(self.source, folder, Path("custom.pdf"))
        self.assertEqual(result, folder / "custom.pdf")

    def test_overwrite_protection_cli(self):
        output = self.root / "sample.pdf"
        output.write_bytes(b"keep this file")
        with self.assertRaises(SystemExit) as raised:
            text_to_pdf.main([str(self.source)])
        self.assertEqual(raised.exception.code, 2)
        self.assertEqual(output.read_bytes(), b"keep this file")

    def test_overwrite_flag_allows_replacement(self):
        output = self.root / "sample.pdf"
        output.write_bytes(b"old pdf")
        result = text_to_pdf.main([str(self.source), "--overwrite"])
        self.assertEqual(result, 0)
        self.assertTrue(output.read_bytes().startswith(b"%PDF"))


if __name__ == "__main__":
    unittest.main()
