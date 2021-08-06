import os
import unittest

def exec_cmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

def str_to_list(text):
    l = str(text).split()
    return list(filter(lambda x: x != '', map(lambda x: x.strip(), l)))


test_cmd = "python ./pkgsync test.json "

class TestStringMethods(unittest.TestCase):
    def test_add_and_del(self):
        exec_cmd('rm test.json')

        exec_cmd(test_cmd + 'add 1 2 3')
        ls = str_to_list(exec_cmd(test_cmd + 'list-sync'))
        self.assertTrue('1' in ls)
        self.assertTrue('2' in ls)
        self.assertTrue('3' in ls)
        self.assertTrue('' not in ls)

        exec_cmd(test_cmd + 'del 2 3 4 5 6')
        ls = str_to_list(exec_cmd(test_cmd + 'list-sync'))
        self.assertTrue('1' in ls)
        self.assertTrue('2' not in ls)
        self.assertTrue('3' not in ls)

    def test_ignore_and_del(self):
        exec_cmd('rm test.json')

        exec_cmd(test_cmd + 'ignore 1 2 3')
        ls = str_to_list(exec_cmd(test_cmd + 'list-ignore'))
        self.assertTrue('1' in ls)
        self.assertTrue('2' in ls)
        self.assertTrue('3' in ls)
        self.assertTrue('' not in ls)

        exec_cmd(test_cmd + 'del 2 3 4 5 6')
        ls = str_to_list(exec_cmd(test_cmd + 'list-ignore'))
        self.assertTrue('1' in ls)
        self.assertTrue('2' not in ls)
        self.assertTrue('3' not in ls)

    def test_pkglist_cmd_and_list_pending(self):
        exec_cmd('rm test.json')

        exec_cmd(test_cmd + "set-pkglist-cmd 'echo 123 456'")
        ls = str_to_list(exec_cmd(test_cmd + 'list-pending'))
        self.assertTrue('123' in ls)
        self.assertTrue('456' in ls)
        self.assertTrue('' not in ls)

        exec_cmd(test_cmd + 'ignore-all')
        ls = str_to_list(exec_cmd(test_cmd + 'list-pending'))
        self.assertTrue('123' not in ls)
        self.assertTrue('456' not in ls)
        ls = str_to_list(exec_cmd(test_cmd + 'list-ignore'))
        self.assertTrue('123' in ls)
        self.assertTrue('456' in ls)

if __name__ == '__main__':
    unittest.main()
