参考rqalpha4.7文档
https://rqalpha.readthedocs.io/zh_CN/latest/development/mod.html
创建虚拟环境的时候，出现包错误的报错
通过手动删除相关的包
conda  update --all

--------------------------------
conda create -n env_name python=3.6
conda activate env_name
conda remove -n nlp --all
conda deactivate
conda env list
conda remove --name your_env_name --all
------------------------------------
conda create -n rqalpha_mod_hello
conda activate rqalpha_mod_hello
pip install -i https://pypi.douban.com/simple rqalpha


https://rqalpha.readthedocs.io/zh_CN/latest/development/mod.html#id3

![img.png](img.png)





> 
> 经验：
> 1）建立工程的时候注意，都为下划线
> 2）上述文件建立好后，主要关注__init__.py mod.py  setup.py文件。 注意目录结构
> 3）如果感觉紊乱了最好 pip uninstall rqalpha,然后 pip install rqalpha
4) 另外在.rqalpha下面会生产一个 文件，可以删除那个记录的配置文件， 卸载rqalpha后
重新安装rqalpha。
5) rqalpha 4.7版本的 通过install -e .安装mod
6) 安装成功后通过rqalpha enable hello之后
7) 通过rqalpha mod list查看mod。
8) 通过如下命令
9) (base) D:\project\rqalpha_mod_hello>rqalpha run -f ./buy_and_hold.py -d C:\Users\liujunxx\.rqalpha\bundle -s 2016-06-01 -e 2016-12-01 --account stock 100000 --benchmark 000300.XSHG
>>> HelloWorldMod.start_up
[2016-06-01 00:00:00.000000] INFO: user_log: init
>>> HelloWorldMod.tear_down
> 
> 
> 原来有输出的命令
> rqalpha run -f ./rqalpha/examples/buy_and_hold.py -s 2016-06-01 -e 2016-12-01 --account stock 100000 --benchmark 000300.XSHG --plot
> 
> 
> end