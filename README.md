## 食用方法
1. `Fork`本项目
2. 新建/修改`link.txt`文件，按格式填写您的友链，链接于链接之间用 `,`（是半角符号哦） 分割，注意链接格式不要最后的 `/`
3. 将`workflows`配置文件的这两个注释去掉
``` yml
# schedule:
  #   - cron: "0/60 * * * *"
```
4. 如需测试请点击右上角的`Star`
5. 前往`Settings`开启`github pages`，访问`https://用户名.github.io/AutoLinklastactivetime/time.txt`即可看到最新的友链最近活跃时间
6. 建议不接收该项目的任何信息（不然邮件能吵死你）

## FAQ
1. 若某网站无法访问或无`/atom.xml`文件将抛出`ERROR`，`Actions`日志为`活跃时间未知`
