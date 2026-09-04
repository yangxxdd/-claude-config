# Skills/Plugins 统一联结操作蓝图

## 目标
- 实体存 D:\claude-projects\shared\skills\ 和 plugins\
- C:\Users\yangxd\.claude\skills\ → 联结到 D 盘
- D:\claude-projects\claude-config\skills\ → 联结到 D 盘
- 一份实体，多处可用

## 操作步骤

### 第一步：创建 D 盘共享目录
```
mkdir D:\claude-projects\shared\skills
mkdir D:\claude-projects\shared\plugins
```

### 第二步：复制内容到 D 盘（保留原件不改动）
```
robocopy C:\Users\yangxd\.claude\skills D:\claude-projects\shared\skills /E /COPYALL
robocopy C:\Users\yangxd\.claude\plugins D:\claude-projects\shared\plugins /E /COPYALL
```

### 第三步：C 盘改名 + 创建联结
```
ren C:\Users\yangxd\.claude\skills skills.bak
mklink /J C:\Users\yangxd\.claude\skills D:\claude-projects\shared\skills

ren C:\Users\yangxd\.claude\plugins plugins.bak
mklink /J C:\Users\yangxd\.claude\plugins D:\claude-projects\shared\plugins
```

### 第四步：D 盘 claude-config 改名 + 创建联结
```
ren D:\claude-projects\claude-config\skills skills.bak
mklink /J D:\claude-projects\claude-config\skills D:\claude-projects\shared\skills

ren D:\claude-projects\claude-config\plugins plugins.bak
mklink /J D:\claude-projects\claude-config\plugins D:\claude-projects\shared\plugins
```

### 第五步：验证
- dir C:\Users\yangxd\.claude\skills 应该显示 D 盘内容
- dir D:\claude-projects\claude-config\skills 应该显示 D 盘内容
- 启动 claude 正常

### 第六步：清理备份
- 验证通过后删除 skills.bak 和 plugins.bak

---

## 回滚方案

出错时按错误位置执行对应回滚：

### 回滚 C 盘（如果在第三步出错）
```cmd
rmdir C:\Users\yangxd\.claude\skills
ren C:\Users\yangxd\.claude\skills.bak skills
rmdir C:\Users\yangxd\.claude\plugins
ren C:\Users\yangxd\.claude\plugins.bak plugins
```

### 回滚 D 盘 claude-config（如果在第四步出错）
```cmd
rmdir D:\claude-projects\claude-config\skills
ren D:\claude-projects\claude-config\skills.bak skills
rmdir D:\claude-projects\claude-config\plugins
ren D:\claude-projects\claude-config\plugins.bak plugins
```

### 完全恢复原始状态
执行上面两个回滚，所有备份（.bak）重命名回来即可。

---

## 关键概念
- `mklink /J` = Windows 目录联结（Junction），类似 Linux 的硬链接
- 联结对应用程序透明，Claude Code 无感知
- 联结目标不存在时会显示为"无法访问的文件夹"
- rmdir 删除联结本身，不会删除目标内容
- ren 重命名目录不会影响联结

## 对运行中的 Claude 的影响
- 当前会话：无影响，Skills 已加载到内存
- 下次启动：通过联结读取，和直接读目录完全一样
