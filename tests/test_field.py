# This file is part of FiberModes.
#
# FiberModes is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FiberModes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FiberModes.  If not, see <http://www.gnu.org/licenses/>.


"""Test suite for field module"""

import unittest
import os.path

from fibermodes import FiberFactory, HE11
from fibermodes.field import Field
import numpy

_dir, _ = os.path.split(__file__)


class TestField(unittest.TestCase):

    """Test Field class.

    Current test are only to ensure code executes without errors.
    Tests that ensure fields are accurate should be written.

    """

    def setUp(self):
        f = FiberFactory(os.path.join(_dir, 'fiber/smf28.fiber'))
        fiber = f[0]
        self.field = Field(fiber, HE11, 1550e-9, 50e-6)

    def testFG(self):
        f = self.field.f(0)
        g = self.field.g(0)

        self.assertEqual(f.ndim, 2)
        self.assertEqual(g.ndim, 2)

        self.assertTrue(numpy.all(f <= 1))
        self.assertTrue(numpy.all(f >= -1))
        self.assertTrue(numpy.all(g <= 1))
        self.assertTrue(numpy.all(g >= -1))

    def testEx(self):
        ex = self.field.Ex()
        self.assertEqual(max(ex.ravel()), ex[50, 50])
        self.assertAlmostEqual(ex[0, 0], 0)

    def testEy(self):
        ey = self.field.Ey()
        self.assertTrue(numpy.all(ey < 0.01))
        self.assertTrue(numpy.all(ey < self.field.Ex()))
        self.assertAlmostEqual(ey[0, 0], 0)

    def testEz(self):
        ez = self.field.Ez()
        self.assertAlmostEqual(ez[0, 0], 0)
        self.assertTrue(numpy.all(ez < self.field.Ex()))

    def testEr(self):
        # TODO: add test
        er = self.field.Er()

    def testEphi(self):
        # TODO: add test
        ephi = self.field.Ephi()

    def testEt(self):
        ex = self.field.Ex()
        et = self.field.Et()
        self.assertTrue(numpy.all(numpy.abs(ex-et) < 1e-5))

    def testEpol(self):
        epol = self.field.Epol()
        self.assertTrue(numpy.all(numpy.abs(epol) < 1e-2))

    def testEmod(self):
        emod = self.field.Emod()
        self.assertTrue(numpy.all(emod > 0))

    def testHx(self):
        pass

    def testHy(self):
        pass

    def testHz(self):
        # TODO: add test
        hz = self.field.Hz()

    def testHr(self):
        # TODO: add test
        hr = self.field.Hr()

    def testHphi(self):
        # TODO: add test
        hphi = self.field.Hphi()

    def testHt(self):
        # TODO: add test
        ht = self.field.Ht()

    def testHpol(self):
        # TODO: add test
        hpol = self.field.Hpol()

    def testHmod(self):
        hmod = self.field.Hmod()
        self.assertTrue(numpy.all(hmod > 0))

    def testAeff(self):
        # TODO: add test
        aeff = self.field.Aeff()
        self.assertGreater(aeff, 0)

    def testBetazAcceptsUserLength(self):
        # betaz/betaz0 used to hard-code z=10e6 with no way to override it.
        default = self.field.betaz()
        custom = self.field.betaz(z=1)
        self.assertNotEqual(default, custom)
        # beta*z should scale linearly with z.
        self.assertAlmostEqual(default / custom, 10e6 / 1)

        default0 = self.field.betaz0(Neff_min=1.44)
        custom0 = self.field.betaz0(z=1, Neff_min=1.44)
        self.assertNotEqual(default0, custom0)
        self.assertAlmostEqual(default0 / custom0, 10e6 / 1)

    def testEprop2AcceptsUserLength(self):
        # eprop2 used to hard-code z=4 with no way to override it.
        default = self.field.eprop2()
        custom = self.field.eprop2(z=100)
        self.assertFalse(numpy.allclose(default, custom))
        # With z=0 there is no propagation, so the result should match
        # the un-propagated transverse field.
        zero = self.field.eprop2(z=0)
        self.assertTrue(numpy.allclose(zero, self.field.Et2()))

    def testEpropAcceptsUserLength(self):
        # eprop used to hard-code z=816508.13 with no way to override it.
        #
        # This does NOT use self.field (smf28.fiber): eprop's internal
        # _f1/_f2 helpers hard-code a core/cladding index pair of
        # 1.50/1.45 and return NaN whenever a fiber's real effective
        # index falls outside that assumed range -- which is the case
        # for smf28 (core 1.4489 / cladding 1.4444). That is a separate,
        # pre-existing bug in _f1/_f2, filed separately; using it here
        # would make this test unable to tell "z is respected" apart
        # from "the whole computation is NaN". Instead we build a fiber
        # whose indices fall inside the range _f1/_f2 assume.
        f = FiberFactory()
        f.addLayer(radius=4e-6, index=1.48)
        f.addLayer(index=1.46)
        fiber = f[0]
        field = Field(fiber, HE11, 1550e-9, 10e-6, np=11)

        default = field.eprop()
        explicit_same = field.eprop(z=816508.13)
        custom = field.eprop(z=1)

        self.assertFalse(numpy.isnan(default).any())
        self.assertTrue(numpy.allclose(default, explicit_same))
        self.assertFalse(numpy.allclose(default, custom))


if __name__ == "__main__":
    unittest.main()
