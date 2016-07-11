# edx_manager_rest
RESTful API   for edx studio  and lms

# 设计
*  作为restful服务
*  实际是一个胶水层（桥接模式(Bridge Pattern)）

# 功能
### edx_lms_rest.py
*  往课程里批量添加学生
### edx_cms_rest.py
*  创建课程
*  添加课程老师

# Usage
*  mv local.yaml.template local.yaml
*  mv local_lms.yaml.template local_lms.yaml
*  登录lms和studio，填入csrftoken和sessionid
*  使用方法参考test文件

# 参考
*  [edx-rest](https://github.com/pmitros/edx-rest/)
*  [edx_siteapi](https://github.com/wwj718/edx_siteapi)
