import unittest
from functions import fun_add,fun_minus,fun_multi,fun_div
from HtmlTestRunner import  HTMLTestRunner
import sys

class TestFun(unittest.TestCase):
    times = 0
 
    @classmethod
    def setUpClass(cls):
        print('setUpclass')
 
    # def setUp(self):
    #     # 每个测试用例执行之前都会执行该方法
    #     TestFun.times += 1
    #     print('setUp', TestFun.times)
 
    # def tearDown(self):
    #     # 每个测试用例执行之后都会执行该方法
    #     TestFun.times += 1
    #     print('tearDown', TestFun.times)
 
    def test1(self):
        # 测试用例1:fun_div
        # 使用unittest提供的断言验证functions中的函数的正误
        # 如果不相等就会失败
        self.assertEqual(2, fun_div(4))
        print('test1')

    def test2(self):
        # 测试用例2:fun_add
         self.assertNotEqual(2, 1)
         print('test2')

    def test2(self):
        # 测试用例2:fun_add
        self.assertTrue(fun_add(6) == 8)
        print('test2-1')

    def test3(self):
        # 测试用例3：fun_minus
        self.assertNotEqual(6, fun_minus(6))
        print('test3')
        # self.assertEqual(4, fun_minus(6))

    def test4(self):
        # 测试用例4：fun_multi
        self.assertIsInstance(2, int)
        print('test4')
        # self.assertEqual(8, fun_multi(4))

    # @unittest.skipIf(sys.platform.startswith('win'), 'use in window') #(条件，描述),条件为True时跳过
    # @unittest.skip('I do not wang')  #描述， 任何时候都跳过
    @unittest.skipUnless(sys.platform.startswith('win64'), 'use in window')  #条件为False跳过
    # @unittest.expectedFailure #：如果test失败了，这个test不计入失败的case数目
    def test5(self):
        assertTrue(3<4)
        print('跳过!')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        
if __name__ == '__main__':
    #直接执行
    # unittest.main()
    print(sys.platform)
    #分别加入后执行
    suit = unittest.TestSuite()
    # suit.addTest(TestFun('test1'))
    # suit.addTest(TestFun('test2'))
    # suit.addTest(TestFun('test3'))
    # suit.addTest(TestFun('test4'))
    #一起加入后执行
    # test = [TestFun('test3'), TestFun('test2'), TestFun('test1'), TestFun('test4')]
    # suit.addTests(test)

    suit.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFun))
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(output='result')  #生成html报告
    runner.run(suit)