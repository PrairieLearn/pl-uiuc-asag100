from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase, PLTestCaseWithPlot
from code_feedback import Feedback
from functools import wraps
import numpy as np

class Test(PLTestCaseWithPlot):


    @points(4)
    @name("xvec1")
    def test_0(self):

        points = 0
        if Feedback.check_numpy_array_allclose('xvec1', self.ref.xvec1, self.st.xvec1):
            points += 1
        Feedback.set_score(points)

    @points(4)
    @name("xvec2")
    def test_1(self):

        points = 0
        if Feedback.check_numpy_array_allclose('xvec2', self.ref.xvec2, self.st.xvec2):
            points += 1
        Feedback.set_score(points)

    @points(2)
    @name("get_change")
    def test_2(self):

        # xvec1 = [np.random.choice([0.0,0.2,0.3,0.5,0.7,1.0]) for i in range(self.ref.nelx*self.ref.nely)]
        # xvec1 = np.round(xvec1,2)
        # xvec2 = [np.random.choice([0.0,0.2,0.3,0.5,0.7,1.0]) for i in range(self.ref.nelx*self.ref.nely)]
        # xvec2 = np.round(xvec2,2)
        N = 4.
        points = 0
        for _ in range(int(N)):
            xvec1, xvec2 = 10*np.random.randn(40), 10*np.random.randn(40)
            st_change = Feedback.call_user(self.st.get_change,xvec1,xvec2)
            ref_change = self.ref.get_change(xvec1,xvec2)

            if Feedback.check_scalar('get_change', ref_change, st_change):
                points += 1
        Feedback.set_score( points/N )
