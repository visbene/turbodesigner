import unittest
import numpy as np
from turbodesigner.airfoils.DCA import DCAAirfoil


class DCAAirfoilTest(unittest.TestCase):

    def test_positive_regular_camber(self):
        c = 1
        theta = np.radians(40)
        tb = c * 0.1
        r0 = tb * 0.1
        airfoil = DCAAirfoil(c=c, theta=theta, r0=r0, tb=tb)
        actual_coords = airfoil.get_coords(5,5)

        expected_coords = np.array([
            [-4.94023275e-01,  1.28171276e-02],
            [-4.99666152e-01,  7.64638405e-03],
            [-5.00000000e-01,  1.73472348e-17],
            [-4.94829256e-01, -5.64287644e-03],
            [-4.87182872e-01, -5.97672477e-03],
            [-1.32950232e-01,  3.46691947e-02],
            [ 0.00000000e+00,  3.81634904e-02],
            [ 1.32950232e-01,  3.46691947e-02],
            [ 4.87182872e-01, -5.97672477e-03],
            [ 4.94829256e-01, -5.64287644e-03],
            [ 5.00000000e-01,  9.54097912e-18],
            [ 4.99666152e-01,  7.64638405e-03],
            [ 4.94023275e-01,  1.28171276e-02],
            [ 1.32950232e-01,  1.29606616e-01],
            [ 0.00000000e+00,  1.38163490e-01],
            [-1.32950232e-01,  1.29606616e-01],
            [-4.94023275e-01,  1.28171276e-02],
        ])
        
        equals = np.allclose(actual_coords, expected_coords)
        self.assertTrue(equals)


    def test_negative_regular_camber(self):
        c = 1
        theta = -np.radians(40)
        tb = c * 0.1
        r0 = tb * 0.1
        airfoil = DCAAirfoil(c=c, theta=theta, r0=r0, tb=tb)
        actual_coords = airfoil.get_coords(5,5)

        expected_coords = np.array([
            [-4.94023275e-01, -1.28171276e-02],
            [-4.99666152e-01, -7.64638405e-03],
            [-5.00000000e-01, -1.73472348e-17],
            [-4.94829256e-01,  5.64287644e-03],
            [-4.87182872e-01,  5.97672477e-03],
            [-1.32950232e-01, -3.46691947e-02],
            [ 0.00000000e+00, -3.81634904e-02],
            [ 1.32950232e-01, -3.46691947e-02],
            [ 4.87182872e-01,  5.97672477e-03],
            [ 4.94829256e-01,  5.64287644e-03],
            [ 5.00000000e-01, -9.54097912e-18],
            [ 4.99666152e-01, -7.64638405e-03],
            [ 4.94023275e-01, -1.28171276e-02],
            [ 1.32950232e-01, -1.29606616e-01],
            [ 0.00000000e+00, -1.38163490e-01],
            [-1.32950232e-01, -1.29606616e-01],
            [-4.94023275e-01, -1.28171276e-02]
        ])
        
        equals = np.allclose(actual_coords, expected_coords)
        self.assertTrue(equals)

    def test_positive_low_camber(self):
        c = 1
        theta = np.radians(10)
        tb = c * 0.1
        r0 = tb * 0.1
        airfoil = DCAAirfoil(c=c, theta=theta, r0=r0, tb=tb)
        actual_coords = airfoil.get_coords(5,5)

        expected_coords = np.array([
            [-4.90909610e-01,  1.08335044e-02],
            [-4.97698497e-01,  7.29943352e-03],
            [-5.00000000e-01,  2.16840434e-18],
            [-4.96465929e-01, -6.78888700e-03],
            [-4.89166496e-01, -9.09038955e-03],
            [-1.32950232e-01, -1.00000000e-02],
            [ 0.00000000e+00, -1.00000000e-02],
            [ 1.32950232e-01, -1.00000000e-02],
            [ 4.89166496e-01, -9.09038955e-03],
            [ 4.96465929e-01, -6.78888700e-03],
            [ 5.00000000e-01, -1.51788304e-18],
            [ 4.97698497e-01,  7.29943352e-03],
            [ 4.90909610e-01,  1.08335044e-02],
            [ 1.32950232e-01,  6.74290127e-02],
            [ 0.00000000e+00,  7.18304715e-02],
            [-1.32950232e-01,  6.74290127e-02],
            [-4.90909610e-01,  1.08335044e-02]
        ])
        
        equals = np.allclose(actual_coords, expected_coords)
        self.assertTrue(equals)

    def test_negative_low_camber(self):
        c = 1
        theta = -np.radians(10)
        tb = c * 0.1
        r0 = tb * 0.1
        airfoil = DCAAirfoil(c=c, theta=theta, r0=r0, tb=tb)
        actual_coords = airfoil.get_coords(5,5)

        expected_coords = np.array([
            [-4.90909610e-01, -1.08335044e-02],
            [-4.97698497e-01, -7.29943352e-03],
            [-5.00000000e-01, -2.16840434e-18],
            [-4.96465929e-01,  6.78888700e-03],
            [-4.89166496e-01,  9.09038955e-03],
            [-1.32950232e-01,  1.00000000e-02],
            [ 0.00000000e+00,  1.00000000e-02],
            [ 1.32950232e-01,  1.00000000e-02],
            [ 4.89166496e-01,  9.09038955e-03],
            [ 4.96465929e-01,  6.78888700e-03],
            [ 5.00000000e-01,  1.51788304e-18],
            [ 4.97698497e-01, -7.29943352e-03],
            [ 4.90909610e-01, -1.08335044e-02],
            [ 1.32950232e-01, -6.74290127e-02],
            [ 0.00000000e+00, -7.18304715e-02],
            [-1.32950232e-01, -6.74290127e-02],
            [-4.90909610e-01, -1.08335044e-02]
        ])
        
        equals = np.allclose(actual_coords, expected_coords)
        self.assertTrue(equals)
