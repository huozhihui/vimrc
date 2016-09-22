#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import shutil, errno
import time
from tqdm import tqdm
import timeout_decorator
import ConfigParser


# Configurate .vimrc class
class VimRc():
    def __init__(self):
        user_home = os.environ['HOME']
        self.vimrc = '%s/.vimrc' % user_home
        self.vimrc_old = '%s/.vimrc_old' % user_home
        self.bundle = '%s/.vim/bundle' % user_home

    def set_vimrc(self):
        if os.path.exists(self.vimrc):
            self.__get_user_input()
        else:
            self.__copy_vimrc()

    def __get_user_input(self):
        print(
        'Your local system already exists .vimrc file, if you input "yes", will be backup .vimrc file for .vimrc_old, and reconfigure .vimrc; Or is not configured .vimrc.')
        while True:
            user_input = raw_input('Do you want configure .vimrc file?(yes/no):')
            if user_input.lower() in ('yes', 'y'):
                self.__rename_vimrc()
                self.__copy_vimrc()
                break
            elif user_input.lower() in ('no', 'n'):
                break
            else:
                if user_input:
                    print "Input Error, Please Input 'yes' or 'no'."
                continue

    def __copy_vimrc(self):
        print "Copy .vimrc file to %s " % os.path.dirname(self.vimrc)
        shutil.copyfile(".vimrc", self.vimrc)
        print "Configurate .vimrc Successfully."

    def __rename_vimrc(self):
        print "Backup .vimrc to .vimrc_old "
        os.rename(self.vimrc, self.vimrc_old)


# Install Vim Plugin
class InstallPlugin():
    def __init__(self):
        user_home = os.environ['HOME']
        self.bundle = '%s/.vim/bundle' % user_home
        '''
        self.plugins = {
            'html5.vim': 'https://github.com/othree/html5.vim.git',
            'ctrlp.vim': 'https://github.com/kien/ctrlp.vim.git',
            'nerdtree': 'https://github.com/scrooloose/nerdtree.git',
            'ctags.vim': 'https://github.com/vim-scripts/ctags.vim.git',
            'nginx-vim-syntax': 'https://github.com/evanmiller/nginx-vim-syntax.git',
            'rename.vim': 'git@github.com:danro/rename.vim.git',
            'snipmate.vim': 'https://github.com/msanders/snipmate.vim.git',
            'vim-endwise': 'https://github.com/tpope/vim-endwise.git',
            'vim-go': 'https://github.com/fatih/vim-go.git',
            'vim-javascript-syntax': 'https://github.com/jelera/vim-javascript-syntax.git',
            'vim-python-pep8-indent': 'https://github.com/hynek/vim-python-pep8-indent.git',
            'vim-rails': 'https://github.com/tpope/vim-rails.git',
            'vim-rake': 'https://github.com/tpope/vim-rake.git',
            'vim-rspec': 'https://github.com/thoughtbot/vim-rspec.git',
            'vim-ruby': 'https://github.com/vim-ruby/vim-ruby.git'


        }
'''
    def main(self):
        if not os.path.exists(self.bundle):
            print "Create %s directory" % self.bundle
            os.mkdir(self.bundle)
        os.chdir(self.bundle)
        print "Plugins List".center(100, '=')
        print "No".center(10) + "Name".ljust(40) + "Url"
        count = 1
        for k, v in self.plugins().iteritems():
            print str(count).center(10) + k.ljust(40) + v
            count += 1

        print '\r'
        print 'Plugins install way:'
        print '    1) Install all'
        print '    2) Select install plugins'
        print '    3) Select not install plugins'
        print '\r'

        while True:
            way = raw_input('Please install way(1/2/3):')
            if way == '1':
                print "install all"
                self.install_plugin(self.plugins())
                break
            elif way == '2':
                print "select install"
                break
            elif way == '3':
                print "select not install"
                break
            else:
                print "Input Error, Please Input '1', '2' or '3'."
                continue

    def install_plugin(self, d):
        for k, v in d.iteritems():
            plugin_path = "%s/%s" % (self.bundle, k)
            if not os.path.exists(plugin_path):
                bp_str = "Begin install %s" % k
                print bp_str.center(50, '*')
                self.git_clone(k, v)
                print 'Plugin %s Install Successfully' % k 
            else:
                print 'Plugin %s already exists' % k

    @timeout_decorator.timeout(1)
    def git_clone(self, pn, url):
        try:
            os.system('git clone %s' % url)
        except:
            print 'Plugin %s Install Timeout' % pn

    # 获取插件列表
    def plugins(self):
        return self.__setting().sections()

    # 获取插件信息
    def __plugin_info(self, pn, key):
        return self.__setting().get(pn, key)

    # 获取配置文件
    def __setting(self):
        config = ConfigParser.ConfigParser()
        config.read('setting.ini')
        return config




if __name__ == '__main__':
   # v = VimRc()
   # v.set_vimrc()
    p = InstallPlugin()
    #p.main()
    p.get_setting()
