import importlib.util, tempfile, unittest, json
from pathlib import Path

class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(importlib.util.find_spec('capture'),'capture implementation absent')
        import capture
        self.c=capture
    def test_archive_roundtrip_and_mutation_refusal(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'hello.txt').write_text('deterministic fixture\n');src='a'*64
            a=self.c.make_archive(p,['hello.txt'],p/'payload.zip','test',src)
            copy=p/'roundtrip.zip';copy.write_bytes(a.read_bytes())
            receipt=self.c.make_receipt(a,copy,'libfile_deterministic_fixture')
            self.assertTrue(receipt['roundtrip_verified'])
            rp=p/'receipt.json';rp.write_text(json.dumps(receipt))
            self.c.require_receipt(rp,a,'test',src)
            copy.write_bytes(copy.read_bytes()+b'changed')
            with self.assertRaises(ValueError):self.c.make_receipt(a,copy,'libfile_deterministic_fixture')
            with self.assertRaises(FileExistsError):self.c.make_archive(p,['hello.txt'],a,'test',src)
            with self.assertRaises(ValueError):self.c.require_receipt(rp,a,'wrong',src)
            with self.assertRaises(ValueError):self.c.require_receipt(rp,a,'test','b'*64)
    def test_no_traversal_no_duplicate_no_missing_file(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'x').write_text('x')
            for files in [['../x'],['x','x'],['missing']]:
                with self.assertRaises((ValueError,FileNotFoundError)):
                    self.c.make_archive(p,files,p/'a.zip','test','a'*64)
    def test_source_review_binding_required(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'x').write_text('x')
            with self.assertRaises(ValueError):self.c.make_archive(p,['x'],p/'a.zip','source','a'*64)

if __name__=='__main__':unittest.main(verbosity=2)
