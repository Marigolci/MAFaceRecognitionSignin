
# 导入系统库并定义辅助函数
from pprint import pformat

# import PythonSDK
from PythonSDK.facepp import API,File
import os
import xpinyin
# 导入图片处理类
import PythonSDK.ImagePro
import cv2
import os
import tkinter
import tkinter.messagebox as mb

# 以下四项是dmeo中用到的图片资源，可根据需要替换
detech_img_url = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
faceSet_img = './imgResource/demo.jpeg'       # 用于创建faceSet
face_search_img = './imgResource/search.png'  # 用于人脸搜索
segment_img = './imgResource/segment.jpg'     # 用于人体抠像
merge_img = './imgResource/merge.jpg'         # 用于人脸融合


# 此方法专用来打印api返回的信息
def print_result(hit, result):
    print(hit)
    print('\n'.join("  " + i for i in pformat(result, width=75).split('\n')))

def printFuctionTitle(title):
    return "\n"+"-"*60+title+"-"*60;

# 初始化对象，进行api的调用工作
api = API()
# -----------------------------------------------------------人脸识别部分-------------------------------------------

# 人脸检测：https://console.faceplusplus.com.cn/documents/4888373
# res = api.detect(image_url=detech_img_url, return_attributes="gender,age,smiling,headpose,facequality,"
#                                                        "blur,eyestatus,emotion,ethnicity,beauty,"
#                                                        "mouthstatus,skinstatus")
# print_result(printFuctionTitle("人脸检测"), res)


# 人脸比对：https://console.faceplusplus.com.cn/documents/4887586
# compare_res = api.compare(image_file1=File(face_search_img), image_file2=File(face_search_img))
# print_result("compare", compare_res)

# 人脸搜索：https://console.faceplusplus.com.cn/documents/4888381
# 人脸搜索步骤
# 1,创建faceSet:用于存储人脸信息(face_token)
# 2,向faceSet中添加人脸信息(face_token)
# 3，开始搜索

# 删除无用的人脸库，这里删除了，如果在项目中请注意是否要删除

connection={'zhangfeiyu2.jpg': 'ebeba206f29d05498f1e68a012c64ab3', 'liusijia1.jpg': '96a169f0f37f229ab681603aa4fe258b', 'zhangbo1.jpg': 'a600c453d7a0c3bd45c2e47823f79cb5', 'liuguangyu2.jpg': '259f96009a2f7815273f2da9982babe0', 'chengzhonghao2.jpg': '5502af3eae4d06149dbd49ad306d49c6', 'gaozishu2.jpg': '55f606545b8d7d41124c949e225ac859', 'zhangbo3.jpg': '6257491a984165c621b97154fda65626', 'niululu1.jpg': '98508aa50e6829d2870373f60d82d4e5', 'hanyaohang3.jpg': 'c49647f1d48ef1f5f8e575bd5ec549ec', 'gaozishu1.jpg': '64f6e95643c97f326e09a186ad5aea23', 'xuxiaohan2.jpg': '6b4048cb4dab29eec97fce74ecce34df', 'mayijie1.jpg': 'a4efc29907929325ae7f97e6f42bb7fc', 'niululu2.jpg': '38fa9fddd932acedc59d09e146ac2b55', 'mayijie3.jpg': '34f2548b166dea5ba13d79055cd8146c', 'dingchaofan2.jpg': '21f834d7d3d56879d6338eaa558323fa', 'zhulingfeng1.jpg': '62d1dad11c0ed41dd370c3aea6c8b757', 'heyao2.jpg': 'cb238f4ab738435f6e6a5b8b45a48104', 'wengjun2.jpg': '983d9a1518092ba28d9c89fa92b00e5e', 'heyao3.jpg': 'e45bb4a5cc1fe44736267934d7c88db6', 'liuhao1.jpg': '6ff69f18fe103980c68982b2cb0d6d0b', 'wenxin2.jpg': '348799df12162138b46a21ded6ec2f4f', 'limeng1.jpg': 'd21a555356196cc83340d401dcc26ee9', 'zhangbo2.jpg': 'c08d84f836048f39f8789cea376c0442', 'shentianyu3.jpg': '8da4257033da9dc5e9d98778e700a601', 'wangwanyi2.jpg': '0dac01d9cebffe7a60d8619e172fe003', 'wangyifan2.jpg': '7213c9c98311e886c47e455970e0d2196a523f55d24725ec54adef6af8f29d397867bfa6d9ad4de120956d09a133abef', 'wenxin4.jpg': '4c0e7829fdaab69630d24bd2f2e9154d', 'dingchaofan1.jpg': '3921f6c76afb15efafe941a6c8b88aaa', 'chaiyajie2.jpg': 'ea4eb965bbf0411ecc83962a400579df', 'niululu3.jpg': 'ac754b86ad01279068f5945fa7af8a6a', 'wengjun1.jpg': '70f9ed7378050341aff4eef294c87211', 'chaiyajie3.jpg': '0ce0e831ce57c5bb7c62036249f42da2', 'wangzhe1.jpg': '61b56732c79ef201a3c4bf39db80b4bc', 'chengzhonghao1.jpg': 'a41e29ad40e9bb109cda87fb760754aa', 'guodebin1.jpg': '3bcbd21877f6bb79f0e21c99f39f3bd2', 'zhulingfeng2.jpg': 'f5f9a4e72ea730f8972c0eefde4fb275', 'wangzhe2.jpg': 'a65062957fcfe5fd7c2a72c721926c28', 'wenxin5.jpg': 'd3ad73a6e5588e05a52a623bda713af1', 'yangyukang1.JPG': 'e558393e74761605cbdcbf4c238a9eaf', 'liuyujing2.jpg': '2ce917cefe3f499f0d18d1f814dbadde', 'zengshen1.jpg': '2d8b528da144f78b2da727a9ea6b8ed9', 'hanyaohang1.jpg': '39b844e84b6abe7c39e5eb6ef069722a', 'xuxiaohan3.jpg': '5abb5ccf3de0ec1ce9cc32fe4b94087e', 'heyao1.jpg': 'a3f706ac44095018230f8429221c7206', 'liuguangyu3.jpg': 'f55760efc0cfb6e7f78f1d1ae3747fd8', 'wenxin1.jpg': '7edf9bb0eccec76b4cee429fddab169a', 'lishuxian2.jpg': 'b0a588fc547b7612ed5942c709093149', 'guanpeiyu2.JPG': 'e1b129a97442f4c607812d29a6766593', 'liuhao2.jpg': '001d06b32643c6ae21240fc74d1c12c2', 'zhuzhimin2.jpg': 'affdf859b6cfdea13a4f206965792c54', 'chaiyajie1.jpg': '428ddd5335b56bf165a0c1dd82b15b7e', 'liuyujing1.jpg': 'cc78a14184d17235f81ff9b6f8e7425f', 'zhengkaizhi2.jpg': '097a7f6c475d9ec633f54f619f330772', 'zhuzhimin1.jpg': '1e819c4181f076d98229f9f5fb897451', 'lilei2.jpg': '5f69f7691138bba4eddbe66c079a01ba', 'yangyukang2.jpg': '9dac16f25662bec1689ef5b0dba3abd4', 'guanpeiyu1.jpg': 'fedeb66c761949f210881e6ad25cea17', 'zhanghongrui1.jpg': '9ad5cb4eb2540b0790440d1c3bab9117', 'zhengkaizhi1.JPG': '00a5df6c4813fecfc328a390434420a7', 'ouyangming2.jpg': '759a243d67825574d06a47c545d41aec', 'shentianyu1.jpg': '2c480208ce04b01598df59e4e9b5a0cc', 'liujiawei1.jpg': 'fc8a449f4bea808e99720a0ef5027c32', 'limeng2.jpg': '425ef54297535fd433502bda9ef00a99', 'ouyangming1.jpg': '3e3314e7e8ab71dadca2b93704ea1155', 'wangyan2.jpg': '2946aec1ae80044e2ac7d7be5cbd53b8', 'lilei1.jpg': '3a4c5c7267c1e06174ef8e150014c067', 'zhangyuankai3.jpg': 'a2a31b6c8a993e5853240894c0eb7f74', 'wangyan1.jpg': '35676e420e83139816f0482521cc0436', 'lishuxian1.jpg': 'cb9ca1b23b85f558387ed82e1b1cecf3', 'guodebin3.jpg': '6c3338bd346f3bfd8141610245e05e45', 'liuying1.jpg': '9df2a007ef8b735787c74251137fd104', 'xuxiaohan1.jpg': '1f7a1bf486d3e20bb904be80771134b9', 'mayijie2.jpg': 'ed0a32aa6adaabafee330eacd73e3b73', 'chenzhaowei1.jpg': 'f8af708ec58cc25fccf7cd33112e89d6', 'zhangfeiyu1.jpg': 'f2eda4f4affae692e4abf9d1d4abb987', 'liuying2.jpg': '1100412efad5ea9ab8d2cb31dd6bf77e', 'guodebin2.jpg': 'be7fb2f75886164319e1478a5cf9c276', 'zhangzhengtao1.jpg': 'c06916214731b450cb2bfbce22d37ca5', 'chenzhaowei2.jpg': '44694f565349ea4402e8c24851ea1df6f2ba8a959ef0928ddecda26a62ea8c6f', 'lucheng2.jpg': '6b2c69670eb06bb97d63122719f45db0', 'bixueting1.jpg': '19fd11c4d298e94886fda02e747f4370', 'zhanghongrui2.jpeg': '98ca8833159860a6b8203a0edfbdba3c', 'liujiawei2.jpg': '8424033a92b37d883244c826e7e01483', 'liuhao3.jpg': '2f031b1924318d73ed6f1928cb888d32', 'liuguangyu1.jpg': '4bd30a760914816e0a72f6d5086e3c10', 'lucheng1.jpg': 'c9c4c4e3aaf2e1bdd89ede4b7df58409', 'zhangyuankai4.jpg': '8a15cf494a8068d1ba10e3876ea443ba', 'wangwanyi1.jpg': '15c3830de5b254835b788d0cbc1c6178', 'zengshen2.jpg': 'd70cde3c42e9045d01a1db5c3f04e490', 'dma.jpg': '9e4baed932b814fd44c76cbb3c5ffbcd', 'wangyifan1.jpg': '2cc11b5665bc582e5ef0805d2eb7dc5b', 'lili2.jpg': 'dd677be6f238fd483eac42b80690e9db', 'zhangzhengtao2.jpg': 'e225b1007c21d95e42308df074489176', 'bixueting2.jpg': '7737096aaed3aa131e6a2d2f26d9a34a', 'lili1.jpg': 'b84c7155de273547807e16a59fec91fc', 'liusijia2.jpg': '146de42cecf0d202219d3c0a70a1c254', 'zhangyuankai1.JPG': 'ae631aa6bd048f25729238a413b94c69', 'wenxin3.jpg': '8dc1fedd66de12ab84836ccdb9523c14', 'lishuxian3.jpg': '74e758b9f6f35f48dc830d948f8ce758'}

# 2.向faceSet中添加人脸信息(face_token)
def train(path2):
    api.faceset.delete(outer_id='STFace', check_empty=0)
    # 1.创建一个faceSet
    ret = api.faceset.create(outer_id='STFace')

    # path2="/home/marigolci/Downloads/face_recognition-master/examples/FacialSet"

    for name in os.listdir(path2):
        faceResStr=""
        res = api.detect(image_file=File(os.path.join(path2,str(name))))
        faceList = res["faces"]
        for index in range(len(faceList)):
            # if(index==0):
            faceResStr = faceResStr + faceList[index]["face_token"]
            # else:
            #     faceResStr = faceResStr + ","+faceList[index]["face_token"]

        api.faceset.addface(outer_id='STFace', face_tokens=faceResStr)
        connection[name]=faceResStr
        name = os.path.splitext(name)[0]

# train function part
# path2 = "/home/marigolci/Downloads/face_recognition-master/examples/FacialSet"
# train(path2)


    # nameList.append(name[:-1])
print(connection)
# namelist procudure
# nameList=list(set(nameList))
#form map
# nameList=dict.fromkeys(list(set(nameList)))
# print(nameList)

nameList={'guodebin': None, 'zhanghongrui': None, 'liuyujing': None, 'zengshen': None, 'liuguangyu': None, 'zhangbo': None, 'zhangfeiyu': None, 'mayijie': None, 'zhengkaizhi': None, 'zhangyuankai': None, 'liujiawei': None, 'lucheng': None, 'wangzhe': None, 'dingchaofan': None, 'yangyukang': None, 'gaozishu': None, 'wangyan': None, 'shentianyu': None, 'wangwanyi': None, 'liusijia': None, 'hanyaohang': None, 'heyao': None, 'guanpeiyu': None, 'zhuzhimin': None, 'dm': None, 'lili': None, 'wengjun': None, 'limeng': None, 'bixueting': None, 'lishuxian': None, 'zhulingfeng': None, 'niululu': None, 'zhangzhengtao': None, 'wenxin': None, 'wangyifan': None, 'xuxiaohan': None, 'chengzhonghao': None, 'liuhao': None, 'liuying': None, 'ouyangming': None, 'lilei': None, 'chaiyajie': None, 'chenzhaowei': None}
nameKey={'dm': '党铭瑷','zengshen':'曾琛','bixueting': '毕雪婷', 'yujunchi': '余俊驰', 'zhoufangxu': '周芳旭', 'mayijie': '马一杰', 'zhulingfeng': '朱凌锋', 'zhangbo': '张勃', 'limeng': '李猛', 'guodebin': '郭德斌', 'zhangyuankai': '张渊凯', 'wengjun': '翁珺', 'heyao': '何瑶', 'chengzhonghao': '程中浩', 'wangzhe': '王喆', 'liusijia': '刘思佳', 'shentianyu': '沈甜雨', 'wangwanyi': '王婉怡', 'zhangfeiyu': '张飞宇', 'dingchaofan': '丁超凡', 'niululu': '牛璐璐', 'wangyifan': '王一帆', 'yanzhanyi': '闫展熠', 'wangyan': '王炎', 'liuyujing': '刘玉婧', 'zhuzhimin': '朱志敏', 'zhengkaizhi': '郑恺之', 'xuxiaohan': '许肖汉', 'lucheng': '陆诚', 'chenzhaowei': '陈钊苇', 'yangyukang': '杨郁康', 'gaozishu': '高子舒', 'ouyangming': '欧阳明', 'xuewei': '薛玮', 'lishuxian': '李淑娴', 'hanyaohang': '韩曜航', 'liuguangyu': '刘光裕', 'liujiawei': '刘嘉炜', 'zhanghongrui': '张洪瑞', 'lilei': '李磊', 'guanpeiyu': '管培育', 'zhangzhengtao': '张正韬', 'wenxin': '温馨', 'chaiyajie': '柴亚捷', 'liuying': '刘莹', 'lili': '李黎', 'liuhao': '刘皓', 'zhaoyuan': '赵园'}
print(len(nameKey))
# 3.开始搜索相似脸人脸信息
# def Search(path1):
# # for name in os.listdir(path1):
#     ResStr=""
#     search_result = api.search(image_file=File(path1), outer_id='STFace')
#     # print("this is name")
#     # print(name)
#     # print_result('search', search_result)
#     # search_result.get("results","not exist")
#     if "results" not in search_result:
#         return "Not exist"
#     res=search_result["results"]
#     for index in range(len(res)):
#         # if (index == 0):
#             ResStr = ResStr + res[index]["face_token"]
#         # else:
#         #     ResStr = ResStr + "," + res[index]["face_token"]
#     nametmp=list(connection.keys())[list(connection.values()).index(ResStr)]
#     nametmp = os.path.splitext(nametmp)[0]
#     nameList[nametmp[:-1]] = 1
#     return nametmp[:-1]
#
# output_dir = '/home/marigolci/Downloads/lc-video'
# i = 1
# cap = cv2.VideoCapture(0)
# while 1:
#     ret, frame = cap.read()
#     cv2.imshow('cap', frame)
#     flag = cv2.waitKey(1)
#     if flag == 13: #按下回车键
#         output_path = os.path.join(output_dir, "%04d.jpg" % i)
#         cv2.imwrite(output_path, frame)
#         if output_path==None:
#             continue
#         tmp=Search(output_path)
#         if tmp==None:
#             continue
#         elif tmp=="Not exist":
#             print("抱歉，请再试一次", tmp)
#         else:
#             print("识别成功，欢迎使用ict-dma人脸签到系统1.0，祝您参观愉快",nameKey[tmp])
#         # tkinter.messagebox.showinfo('提示', '录入成功')
#         # mb.showinfo('INFO', '录入成功')
#         i += 1
#     if flag == 27: #按下ESC键
#         break
# cap.release()
# cv2.destroyAllWindows()
# pathactual='/home/marigolci/Downloads/lc-video'
# # path1=pathactual
#
# print("以下人员尚未签到")
# ans = []
# for i in nameList.items():
#     if i[1] is None:
#         ans.append(nameKey[i[0]])
# print(ans)
# -----------------------------------------------------------人体识别部分-------------------------------------------

# 人体抠像:https://console.faceplusplus.com.cn/documents/10071567
# segment_res = api.segment(image_file=File(segment_img))
# f = open('./imgResource/demo-segment.b64', 'w')
# f.write(segment_res["result"])
# f.close()
# print_result("segment", segment_res)
# # 开始抠像
# PythonSDK.ImagePro.ImageProCls.getSegmentImg("./imgResource/demo-segment.b64")

# -----------------------------------------------------------证件识别部分-------------------------------------------
# 身份证识别:https://console.faceplusplus.com.cn/documents/5671702
# ocrIDCard_res = api.ocridcard(image_url="https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/"
#                                         "c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=7a16a1be19178a82da3177f2976a18e8"
#                                         "/902397dda144ad34a1b2dcf5d7a20cf431ad85b7.jpg")
# print_result('ocrIDCard', ocrIDCard_res)

# 银行卡识别:https://console.faceplusplus.com.cn/documents/10069553
# ocrBankCard_res = api.ocrbankcard(image_url="http://pic.5tu.cn/uploads/allimg/1107/191634534200.jpg")
# print_result('ocrBankCard', ocrBankCard_res)

# -----------------------------------------------------------图像识别部分-------------------------------------------
# 人脸融合：https://console.faceplusplus.com.cn/documents/20813963
# template_rectangle参数中的数据要通过人脸检测api来获取
# mergeFace_res = api.mergeface(template_file=File(segment_img), merge_file=File(merge_img),
#                               template_rectangle="130,180,172,172")
# print_result("mergeFace", mergeFace_res)
#
# # 开始融合
# PythonSDK.ImagePro.ImageProCls.getMergeImg(mergeFace_res["result"])
