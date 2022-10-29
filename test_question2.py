from question2 import hasDuplicate


class TestApp:
    def test_hasDuplicate(self):

        assert not hasDuplicate("0101101")
        assert hasDuplicate("10011001101")
        assert hasDuplicate("11")
        assert hasDuplicate("1100100011")
        assert not hasDuplicate("100101001101")
        assert hasDuplicate("10011001101")
        assert hasDuplicate("0000000000000000000011111111111111111111111111111101")


