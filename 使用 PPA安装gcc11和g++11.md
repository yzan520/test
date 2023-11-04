# 使用 PPA安装gcc11和g++11

## 1.PPA是什么？

PPA 是 Ubuntu 中的一个概念，代表 Personal Package Archives，个人软件包存档。这是 Launchpad 网站为 Ubuntu 用户提供的一个服务，允许个人用户和团队上传软件包到 Launchpad 服务器上，提供一个额外的软件源

PPA 可以让个人开发者、团队或者任何人在 Ubuntu 软件中心之外，提供他们自己的软件源。这意味着用户可以使用 `add-apt-repository` 命令添加这些 PPA，并从中安装软件包

主要优势包括：

1. **访问非官方软件：** PPA 提供了一个方式，供用户获取官方软件源之外的软件

2. **获取更新和较新版本的软件：** 有时，PPA 提供了最新版本的软件，可能比 Ubuntu 官方软件源中的版本更新

使用 PPA 时，用户应该注意一些安全性和稳定性问题，因为这些软件包未经官方认证和审核。因此，添加 PPA 时应当确保选择可信的、知名的 PPA，并且了解所添加软件包的来源，以避免潜在的安全风险

例如，常见的 Ubuntu Toolchain PPA 用于提供较新的 GCC 和 G++ 版本，供开发者使用。

## 2.sudo apt update

`sudo apt update` 是 Ubuntu（或基于 Debian 的系统）中用于更新软件包列表的命令。执行这个命令会让系统重新加载软件包列表，以获取最新的软件信息，但不会安装新版本的软件

具体而言，这个命令会向 Ubuntu 软件仓库发送请求，检查软件包管理器的索引，并获取当前可用软件的最新版本和信息。软件包列表中包含了软件名称、版本、更新、依赖关系等信息

通常，在进行软件安装之前，特别是在添加新的软件源（PPA）之后，最好先执行 `sudo apt update`，以确保软件包列表是最新的，这样你就可以获取到添加的新软件源中的软件信息

需要指出的是，`sudo apt update` 不会更新软件包，它只会更新软件包列表。要实际安装更新软件包，你需要使用 `sudo apt upgrade` 或 `sudo apt dist-upgrade` 命令

## 3.如何使用使用 PPA安装gcc11和g++11

### 3.1添加 Ubuntu Toolchain PPA：

运行以下命令来添加 Ubuntu Toolchain PPA：

```sh
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt update
```

### 3.2安装GCC11和G++11

```sh
sudo apt install gcc-11 g++-11
```

这会安装 GCC 11 和 G++ 11，将它们作为可选的版本安装在系统中

### 3.3配置默认编译器版本：

 ```sh
 sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-11 90 --slave /usr/bin/g++ g++ /usr/bin/g++-11
 ```

这将设置系统中的 `gcc` 和 `g++` 命令指向 GCC 11 和 G++ 11

请注意，安装不同版本的 GCC 和 G++ 可能会在一些系统配置和编译过程中造成混淆。在使用不同版本的编译器时，请注意确保项目的兼容性，并确保正确设置默认编译器版本