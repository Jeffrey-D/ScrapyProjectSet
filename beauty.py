import requests
from bs4 import BeautifulSoup
from time import sleep

header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
         'cookie':'UM_distinctid=1663384985d6fd-03db9719bc459f-8383268-1fa400-1663384985f5c5; CNZZDATA1256110375=1639678596-1538460026-%7C1538460026; pgv_pvi=6300302336; pgv_si=s7801597952; yunsuo_session_verify=61e64cd8bf75fa31a03c96c3195f46f5'}

topic_count = 0
img_count = 0
err_count = 0
for i in range(1,99):
    # try:
    #根据规律遍历生成98个页面地址
    url = 'http://www.cosplaymore.com/list-30-'+str(i)+'.html'
    #使用requests的get方法访问这98个页面
    r = requests.get(url=url,headers=header,timeout=30)
    #将返回的页面内容通过beautifulsoup的网页解析器解析出来
    r_html = BeautifulSoup(r.text,'html.parser')
    #查找class名字为'con'的div
    html_board = r_html.find('div',class_='con')
    #遍历class名字为‘pic imgholder’的a标签
    for topic_link in html_board.find_all('a',class_='pic imgholder'):
        sleep(5)
        topic_count+=1
        print('访问第'+str(topic_count)+'个帖子')
        # 访问每一个帖子
        r_topic = requests.get(url=topic_link.get('href'), headers=header, timeout=30)
        # 将帖子内容解析为html网页
        topic_html = BeautifulSoup(r_topic.text, 'html.parser')
        # 找出帖子的标题
        topic_title = topic_html.find('div', class_='PiccontentTitle').find('font').text
        # 找出这个帖子中的贴图区域
        topic_board = topic_html.find('div', class_='PiccontentPart fl')
        # 从贴图区域找出所有的img标签
        title_count=0
        for img_link in topic_board.find_all('img'):
            # 从img标签中获取链接
            #print(img_link.get('src'))
            title_count += 1
            img_count += 1
            #print(topic_title+str(title_count))
            #下载图片保存到d盘的img文件夹
            img_file = requests.get(url=img_link.get('src'),headers=header,timeout=30)
            img_path = 'd:/img/'+topic_title+str(title_count)+'.jpg'
            with open(img_path,'wb') as f:
                f.write(img_file.content)
                print('图片已保存=====>'+img_path)
# except:
    #     err_count+=1
    #     print('出错，跳过'+str(err_count))

print('共爬取到'+str(topic_count)+'个帖子链接')
print('共爬取到'+str(img_count)+'张图片地址')
print('出错的帖子：'+str(err_count)+'个')