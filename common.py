import shutil
import tempfile

from torch.testing._internal.common_utils import TestCase


class PackageTestCase(TestCase):
    """Minimal base class for torch.package dependency hooks tests."""

    def setUp(self):
        super().setUp()
        self.temp_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.temp_dir, ignore_errors=True)
