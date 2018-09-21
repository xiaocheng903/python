from config import RandyForTest

def main():
    cityChange = {'nanJin': {'cityId': 320100, 'agencyId': 101,'mainhouse':13,'prehouse':22}, 'changZhou': {'cityId': 320400, 'agencyId': 3,'mainhouse':1,'prehouse':False},'jiyuan': {'cityId': 127, 'agencyId': 251,'mainhouse':134,'prehouse':135},
                  'wuXi': {'cityId': 320200, 'agencyId': 17,'mainhouse':4,'prehouse':[15,16,17]}, 'lianYunGang': {'cityId': 320700, 'agencyId': 171,'mainhouse':80,'prehouse':81}}
    print()
    while True:
        print()
        print('*'*30)
        print('请选择以下业务(输入数字选择):')
        order_num=input('\n\n1.新建红包,\t2.新建优惠券,\t3.更改达豆,\t4.商城下单,\n\n5.猪行侠验证码,\t6.全局新建整散商品,\t7.客服系统审核,\t8.查询系统,'
                            '\n\n9.仓库运输系统走单,\t10.主仓入库,\t11.采购,\t12.猪行侠业务,\n\n13.退货入库,\t14.库位上架,\t0.退出,\n')
        if str(order_num)==str(1):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.常州,\n\n3.无锡,\n\n4.连云港,\n\n5.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['changZhou']['cityId']
                agencyId=cityChange['changZhou']['agencyId']
                server_url = 'http://192.168.1.251:31000'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(5):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            else:
                continue
            redGift_value = input('红包金额:')
            redGift_quantity = input('红包发放数量:')
            redGift_ownLimit = input('用户可领取数量:')
            redGift_useBaseLine = input('红包使用条件金额(满多少可用?):')
            redGift_instruction = '满{0}减{1}'.format(redGift_useBaseLine,redGift_value)
            print('描述为:'+redGift_instruction)
            createRedGift(cityId,agencyId,server_url,url_username,url_password,redGift_value,redGift_quantity,redGift_ownLimit,redGift_useBaseLine,redGift_instruction)
            print('请选择是否店铺领取(输入数字选择):')
            bangding_num=input('\n1.领取,\n2.不领取,\n')
            if str(bangding_num)==str(1):
                store_main_username=input('输入店铺登陆账号:')
                store_main_password=input('输入店铺登陆密码(默认123456,可回车跳过):')
                if store_main_password=='':
                    store_main_password=123456
                receiveRedGift(store_main_username,store_main_password)
            elif str(bangding_num)==str(2):
                pass

        elif str(order_num)==str(2):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.常州,\n\n3.无锡,\n\n4.连云港,\n\n5.济源,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['changZhou']['cityId']
                agencyId=cityChange['changZhou']['agencyId']
                server_url = 'http://192.168.1.251:31000'
                url_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(5):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                server_url = 'http://192.168.1.251:31010'
                url_username = '15858800000'
                url_password = '123456'
            else:
                continue
            coupon_value = input('优惠券金额:')
            coupon_quantity = input('优惠券发放数量:')
            coupon_useBaseLine = input('优惠券使用条件金额(满多少可用?):')
            coupon_instruction = '满{0}减{1}'.format(coupon_useBaseLine,coupon_value)
            print('描述为:' + coupon_instruction)
            newCoupon(cityId,agencyId,server_url,url_username,url_password,coupon_value,coupon_quantity,coupon_useBaseLine,coupon_instruction)
        elif str(order_num)==str(3):
            dd_phoneNum = input('输入店铺登陆账号:')
            dd_count = input('输入达豆数量:')
            UpdateDadou(dd_phoneNum,dd_count)
        elif str(order_num)==str(4):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.常州,\n\n3.无锡,\n\n4.连云港,\n\n5.济源,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                prehouse = cityChange['nanJin']['prehouse']
            elif str(city_num)==str(2):
                cityId=cityChange['changZhou']['cityId']
                prehouse = cityChange['changZhou']['prehouse']
            elif str(city_num)==str(3):
                cityId=cityChange['wuXi']['cityId']
                prehouse = cityChange['wuXi']['prehouse']
            elif str(city_num)==str(4):
                cityId=cityChange['lianYunGang']['cityId']
                prehouse = cityChange['lianYunGang']['prehouse']
            elif str(city_num)==str(5):
                cityId=cityChange['jiyuan']['cityId']
                prehouse = cityChange['jiyuan']['prehouse']
            else:
                continue
            checkStoreName(cityId, prehouse)
            purchase_phoneNum = input('\n输入商城店铺登陆账号:\n')
            clean_redis(purchase_phoneNum)
            store_Order(cityId,purchase_phoneNum)

        elif str(order_num)==str(5):
            zxx_loginNum = input('输入猪行侠登陆账号:')
            getZXXCode(zxx_loginNum)
        elif str(order_num)==str(6):
            img_jpg=img_content()
            if not img_jpg:
                print('\t上传图片动作失败,无法新建整散商品')
                continue
            task_ID = input('\n1.新建散装,\n\n2.新建整装,\n')
            nav_Name = input('\n输入新建商品名标签(默认跳过):\n')
            if str(task_ID)==str(1):
                count_ID = input('\n输入新建散装商品数量:\n')
                for count in range(int(count_ID)):
                    name=nav_Name+str(int(time.time()))
                    create_san_product(name,img_jpg)
            elif str(task_ID)==str(2):
                type_ID=input('\n1.自动新建散装并绑定整装,\n\n2.手动输入散装库存编号,\n')
                if str(type_ID)==str(1):
                    count_ID = input('\n输入新建整装商品数量:\n')
                    for count in range(int(count_ID)):
                        name = nav_Name+str(int(time.time()))
                        full_Id = create_san_product(name,img_jpg)
                        if full_Id:
                            create_zheng_product(name,full_Id,img_jpg)
                        else:
                            continue
                elif str(type_ID)==str(2):
                    name = nav_Name+str(int(time.time()))
                    full_Id = input('\n输入关联的散装库存编号:\n')
                    if checkGoodsExist(full_Id):
                        create_zheng_product(name,full_Id,img_jpg)
                else:
                    continue
            else:
                continue
        elif str(order_num)==str(7):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse = cityChange['nanJin']['mainhouse']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                invent_username='15858800000'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                invent_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                invent_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                server_url = 'http://192.168.1.251:3586'
                invent_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                invent_username = '15858800000'
                url_password = '123456'
            else:
                continue
            task_num = input('\n1.审核订单\t2.取消订单\t3.订单退货\n')
            if str(task_num)==str(1):
                SureOrder(cityId, agencyId, server_url, url_username, url_password)
            elif str(task_num)==str(2):
                order_Id = input('\n输入要取消的订单号\n')
                CancleOrder(cityId, agencyId, server_url, url_username, url_password, order_Id)
            elif str(task_num)==str(3):
                order_Id = input('\n输入要退货的订单号\n')
                ThOrder(cityId, agencyId, server_url, url_username, url_password, order_Id,invent_url,invent_username,mainhouse)
            else:
                continue
        elif str(order_num)==str(8):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.常州,\n\n3.无锡,\n\n4.连云港,\n\n5.济源,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                mainhouse=cityChange['nanJin']['mainhouse']
                prehouse=cityChange['nanJin']['prehouse']
            elif str(city_num)==str(2):
                cityId=cityChange['changZhou']['cityId']
                mainhouse = cityChange['changZhou']['mainhouse']
                prehouse = cityChange['changZhou']['prehouse']
            elif str(city_num)==str(3):
                cityId=cityChange['wuXi']['cityId']
                mainhouse = cityChange['wuXi']['mainhouse']
                prehouse = cityChange['wuXi']['prehouse']
            elif str(city_num)==str(4):
                cityId=cityChange['lianYunGang']['cityId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                prehouse = cityChange['lianYunGang']['prehouse']
            elif str(city_num)==str(5):
                cityId=cityChange['jiyuan']['cityId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                prehouse = cityChange['jiyuan']['prehouse']
            else:
                continue
            task_num = input('\n1.查询店铺账号,\n\n2.查询店铺是主仓或是前置仓,\n\n3.查询入库验收账号,\n\n4.退出,\n')
            if str(task_num)==str(1):
                checkStoreName(cityId,prehouse)
            elif str(task_num)==str(2):
                store_name = input('输入店铺登录账号:')
                checkStoreType(cityId, store_name, prehouse)
            elif str(task_num)==str(3):
                checkRuKuName(mainhouse)
            else:
                continue
        elif str(order_num)==str(9):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse=cityChange['nanJin']['mainhouse']
                prehouse=cityChange['nanJin']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                prehouse = cityChange['wuXi']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                prehouse = cityChange['lianYunGang']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                prehouse = cityChange['jiyuan']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
            else:
                continue
            order_Id = input('\n输入订单号\n')
            print('请选择订单类型')
            order_ty = input('\n1.订单为主仓店铺订单,\n\n2.订单为前置仓店铺订单,\n')
            if str(order_ty)==str(1):
                mainstorerun(cityId,agencyId,server_url,url_username,url_password,order_Id)
            elif str(order_ty)==str(2):
                prestorerun(cityId,agencyId,server_url,url_username,url_password,order_Id)
            else:
                continue
        elif str(order_num)==str(10):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse=cityChange['nanJin']['mainhouse']
                prehouse=cityChange['nanJin']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
                worker={"id":28,"workId":"njs001","name":"哈哈哈"}
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                prehouse = cityChange['wuXi']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '13111111111'
                url_password = '123456'
                worker={"id":2,"workId":"wxs001","name":"无锡验收员"}
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                prehouse = cityChange['lianYunGang']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
                worker={"id":32,"workId":"ZDH001","name":"连云港市"}
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                prehouse = cityChange['jiyuan']['prehouse']
                server_url = 'http://192.168.1.251:48000'
                url_username = '15858800000'
                url_password = '123456'
                worker={"id":85,"workId":"jy001","name":"济源"}
            else:
                continue
            order_Id = input('\n输入采购单号\n')
            Ruku(cityId, agencyId, worker, order_Id, server_url, url_username, url_password)
        elif str(order_num)==str(11):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse=cityChange['nanJin']['mainhouse']
                prehouse=cityChange['nanJin']['prehouse']
                server_url = 'http://192.168.1.248:31100'
                url_username = '15858800000'
                url_password = '123456'
                worker={'name':'供应商test1','providerId':'100693'}
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                prehouse = cityChange['wuXi']['prehouse']
                server_url = 'http://192.168.1.248:31100'
                url_username = '15858800000'
                url_password = '123456'
                worker={'name':'顶替','providerId':'100696'}
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                prehouse = cityChange['lianYunGang']['prehouse']
                server_url = 'http://192.168.1.248:31100'
                url_username = '15858800000'
                url_password = '123456'
                worker={'name':'A01','providerId':'100716'}
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                prehouse = cityChange['jiyuan']['prehouse']
                server_url = 'http://192.168.1.248:31100'
                url_username = '15858800000'
                url_password = '123456'
                worker={'name':'济源供应商','providerId':'1000340'}
            else:
                continue
            print('\n*****使用默认固定供应商:', worker['name'])
            checkUsedGood(cityId, worker['providerId'])
            ck_Id = input('\n输入商品库存编号\n')
            quantity = input('\n输入商品采购数量\n')
            print('\n请选择采购仓库')
            order_ty = input('\n1.主仓采购,\t2.前置仓采购,\n')
            if str(order_ty)==str(1):
                CaiGou(cityId, agencyId, server_url, mainhouse, url_username, url_password, ck_Id, quantity,worker['providerId'])
            elif str(order_ty)==str(2):
                if str(cityId)==str(320200):
                    print('无锡主要三个前置仓,请选择')
                    wuxi_pre = input('\n1.无锡前置仓1,\t2.无锡前置仓2,\t3.无锡前置仓3\n')
                    if str(wuxi_pre)==str(1):
                        prehouse=15
                    elif str(wuxi_pre)==str(2):
                        prehouse=16
                    elif str(wuxi_pre)==str(3):
                        prehouse=17
                    else:
                        continue
                CaiGou(cityId, agencyId, server_url, prehouse, url_username, url_password, ck_Id, quantity,worker['providerId'])
            else:
                continue
        elif str(order_num)==str(12):
            print('请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                server_url = 'http://192.168.1.251:50000'
                worker = {'name':'ps001', 'phone':'15575000999'}
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                server_url = 'http://192.168.1.251:50000'
                worker = {'name':'ps001', 'phone':'15575000995'}
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                server_url = 'http://192.168.1.251:50000'
                worker = {'name':'ps001', 'phone':'17621145336'}
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                server_url = 'http://192.168.1.251:50000'
                worker = {'name':'001002', 'phone':'15858800009'}
            else:
                continue
            print('\n默认主仓猪行侠手机号:',worker['phone'])
            print('\n前置仓猪行侠手机号需自己输入')
            ps_phone=input('\n输入前置仓猪行侠手机号(主仓猪行侠Enter跳过)\n')
            if ps_phone !='':
                phone=ps_phone
            else:
                phone=worker['phone']
            task_type=input('\n1.送达\n\n2.拒收\n\n3.部分送达\n\n4.退货取货中\n')
            ZZX(server_url, phone, task_type)
        elif str(order_num)==str(13):
            print('\n仓库运输系统_退货入库业务')
            print('\n请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse = cityChange['nanJin']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username='15858800000'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '15858800000'
                url_password = '123456'
            else:
                continue
            order_Id = input('\n输入退货入库订单编号\n')
            TH_RU(cityId, agencyId, invent_url, invent_username, url_password, mainhouse, order_Id)
        elif str(order_num)==str(14):
            print('\n请选择城市(输入数字选择):')
            city_num=input('\n1.南京,\n\n2.无锡,\n\n3.连云港,\n\n4.济源市,\n')
            if str(city_num)==str(1):
                cityId=cityChange['nanJin']['cityId']
                agencyId=cityChange['nanJin']['agencyId']
                mainhouse = cityChange['nanJin']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username='15858800000'
                url_password = '123456'
            elif str(city_num)==str(2):
                cityId=cityChange['wuXi']['cityId']
                agencyId=cityChange['wuXi']['agencyId']
                mainhouse = cityChange['wuXi']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '13111111111'
                url_password = '123456'
            elif str(city_num)==str(3):
                cityId=cityChange['lianYunGang']['cityId']
                agencyId=cityChange['lianYunGang']['agencyId']
                mainhouse = cityChange['lianYunGang']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '15858800000'
                url_password = '123456'
            elif str(city_num)==str(4):
                cityId=cityChange['jiyuan']['cityId']
                agencyId=cityChange['jiyuan']['agencyId']
                mainhouse = cityChange['jiyuan']['mainhouse']
                invent_url = 'http://192.168.1.251:48000'
                invent_username = '15858800000'
                url_password = '123456'
            else:
                continue
            order_Id = input('\n输入采购入库单号\n')
            SJ(cityId, agencyId, invent_url, invent_username, url_password, mainhouse, order_Id)
        elif str(order_num)==str(0):
            break
main()