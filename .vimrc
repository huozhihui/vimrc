"filetype off                  " required
"colorscheme rails             " 适合ruby
"colorscheme peachpuff        " 适合Ruby开发的蓝色主题
"colorscheme railscasts        " 适合Ruby开发的蓝色主题
"colorscheme github           " 适合Ruby开发的蓝色主题
"colorscheme guardian         " 适合Ruby开发的蓝色主题

"colorscheme solarized          " 适合Ruby开发的蓝色主题
"colorscheme molokai
"set background=dark
"set nobackup                  " 不产生临时文件（备份文件）
"set noswapfile                " 不产生临时文件（交换文件）
"set ruler                     " 打开状态标尺
"set cursorline                " 突出显示当前行

" 设置自动保存
imap <F9> <Esc>:up<cr>
let g:ctrlp_map = ',,'
set guifont=Monaco:h10       " 适合Ruby开发的字体 && 字号
set tabstop=4                " 设置tab键的宽度
set shiftwidth=4             " 换行时行间交错使用4个空格
set expandtab
set autoindent               " 自动对齐
set backspace=2              " 设置退格键可用
set cindent shiftwidth=2     " 自动缩进4空格
set smartindent              " 智能自动缩进
set ai!                      " 设置自动缩进
set nu!                      " 显示行号
"set ruler                    " 右下角显示光标位置的状态行
set hlsearch                 " 开启高亮显示结果
set incsearch                " 开启实时搜索功能
set nowrapscan               " 搜索到文件两端时不重新搜索
set nocompatible             " 关闭兼容模式
set vb t_vb=                 " 关闭提示音
set hidden                   " 允许在有未保存的修改时切换缓冲区
set mouse=a
set clipboard=unnamed
set list                     " 显示Tab符，使用一高亮竖线代替
set listchars=tab:\|\ ,
"set statusline+=%F           " 显示当前文件路径
"set laststatus=2             " 显示当前文件路径    
set wrapscan
"syntax enable                " 打开语法高亮
syntax on                    " 开启文件类型侦测
filetype indent on           " 针对不同的文件类型采用不同的缩进格式
filetype plugin on           " 针对不同的文件类型加载对应的插件
filetype plugin indent on    " 启用自动补全
execute pathogen#infect()
autocmd BufNewFile,BufRead *.erb set filetype=html

