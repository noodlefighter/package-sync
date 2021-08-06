# package-sync

Script for sync multi environments packages ...

这个脚本适用于希望保持多台机器安装的 packages 保持同步的人。

你可以将部分部分需要加入同步列表的软件包告诉脚本，脚本会帮你存入`sync`列表，而不需要同步的软件包，存入`ignore`列表；列表被储存在指定的JSON文件中，你可以通过 github 仓库或者其他云服务同步到其他环境中调出使用。

在日后的使用，你可能会添加一些软件包，其中只有一部分是希望被同步的，此时脚本可以列出这些未被关注的包，方便你管理`sync`列表。

## usage

这是一个使用例，这里假设你是 Arch 系 Linux 发行版用户：

1. 初次使用时，先创建数据库，也就是一个`.json`文件，可以从复制模板开始

```bash
$ cp template-arch.json mypacks.json
```

2. 列出当前未决软件包列表

```bash
$ ./pkgsync mypacks.json list-pending
acpi
acpid
adapta-maia-theme
...
yay
yelp
zensu
zerotier-one
zsh
```

3. 管理需要同步的软件包

将需要同步的软件包加入`sync`列表，将余下的包加入`ignore`列表：

```bash
$ ./pkgsync mypacks.json add zsh yay
added: zsh yay
$ ./pkgsync mypacks.json list-sync
yay
zsh
$ ./pkgsync mypacks.json ignore-all
ignore: acpi acpid ...
```

4. 需要同步时，可以这样操作

```bash
$ ./pkgsync mypacks.json list-sync > pkglist.txt
$ sudo pacman -S - < pkglist.txt
```

5. 添加新软件包后

尝试安装新的软件包，未决列表中会出现它。

```bash
$ sudo pacman -S ruby
$ ./pkgsync mypacks.json list-pending
ruby
```

接下来的操作你该知道了，根据是否希望它被同步，将它应该加入`sync`或`ignore`列表。

## development

unit test:

```bash
$ python test.py
```
