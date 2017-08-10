### WEB接口文档

##### 1.添加发布会接口

> 名称  添加发布会

> 描述   添加发布会

> URL http://127.0.0.1:8000/api/add_event/

> 调用方法  post

> 传入参数   
>
>  eid     #发布会id
>
> name   #发布会标题
>
> limit    #限制人数
>
> status #状态
>
> address #地址
>
> start_time #发布会时间（格式：2017-08-10 12：00：00）

> 返回值
>
> ｛‘status’:200,'message':"add event success"｝

> 状态码：
>
> 10021:parameter  error   
>
> 10022:event id already exists   
>
> 10023:event name already exists
>
> 10024:start_time format error.It must be in YYYY-MM-DD HH:MM:SS format
>
> 200:    add event success

> 说明：发布会接口测试说明

##### 2.查询发布会接口

> 名称  查询发布会

> 描述   查询发布会

> URL http://127.0.0.1:8000/api/get_event_list/

> 调用方法  GET

> 传入参数   
>
>  eid     #发布会id
>
> name   #发布会名称

> 返回值
>
> ｛‘data’:{'start_time':"2016-12-10T14:00:00",‘name’:'小米手机发布会','limit':2000,'address':'背景水立方','status':true｝,"message":"successs","status":200}

> 状态码：
>
> 10021:parameter  error   
>
> 10022:query result is empty 
>
> 200:    add event success

> 说明：eid 或 name 两个参数二选一

##### 3.添加嘉宾接口

> 名称  添加嘉宾接口

> 描述     添加嘉宾接口

> URL http://127.0.0.1:8000/api/add_guest/

> 调用方法  post

> 传入参数   
>
>  eid     #关联发布会id
>
> realname   #姓名
>
> phone    #手机号码
>
> email     #邮箱

> 返回值
>
> ｛‘status’:200,'message':"add event success"｝

> 状态码：
>
> 10021:parameter  error   
>
> 10022:event id null    
>
> 10023:event status is not available
>
> 10024:event number is full 
>
> 10025:event has started
>
> 10026:the event guest phone number pepeat 
>
> 200:    add guest success

> 说明：

##### 4.查询嘉宾接口

> 名称  查询嘉宾接口

> 描述   查询嘉宾接口

> URL http://127.0.0.1:8000/api/get_guest_list/

> 调用方法  GET

> 传入参数   
>
>  eid     #关联发布会id
>
> phone   #嘉宾手机号

> 返回值
>
> {‘data’:[{'email':"123456@mail.com",‘phone’:'123456','realname':'david','sign':false},{'email':"123456@mail.com",‘phone’:'123456','realname':'david','sign':false},{'email':"123456@mail.com",‘phone’:'123456','realname':'david','sign':false}],"message":"successs","status":200}

> 状态码：
>
> 10021:eid can not be empty
>
> 10022:query result is empty 
>
> 200:  success

> 说明：

##### 5.发布会签到接口

> 名称  发布会签到接口

> 描述   发布会签到接口

> URL http://127.0.0.1:8000/api/user_sign/

> 调用方法  GET

> 传入参数   
>
>  eid     #发布会id
>
> phone   #嘉宾手机号

> 返回值
>
> {"status":200,"message":"successs"}

> 状态码：
>
> 10021：parameter error
>
> 10022:  event id null 
>
> 10023：event status is not avaliable 
>
> 10024：event has started
>
> 10025：user phone null
>
> 10026：user did not participate in the conference
>
> 10027：user has sign in
>
> 200:  sign success

> 说明：