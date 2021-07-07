# Importing required libraries...
import datetime
import logging
# import pandas as pd
from logging.handlers import TimedRotatingFileHandler

# import time
l2 = datetime.datetime.now()
import easyocr
import re

# DEFINING EASY_OCR with language English...
reader = easyocr.Reader(['en'])

# LOGGER INFO FOR CODE REFERENCE... (Debug checking)
l1 = datetime.datetime.now()
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler("/home/jsw/WagonNumber_Detection/Model_Logs/CAM_1_INFO/OCR_Logs/logeer_{}.log".format(
        l1), when="m", interval=60)
logger.addHandler(handler)

code = 0
num11list = []
num4_list = []
num5list = []
num6list = []
num7_list = []
num8_list = []
num9_list = []
num10_list = []
wagonid = []
det = 0
out_dict = {}
num5_list = []
x = []
z = []
final_list = []
temp_list1 = []


# global code

def Easy_OCR(image):

    # global code

    # Reading image from model
    result = reader.readtext(image)
    # print(result)

    # with open("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Crop_Images/OCR_Result {}.txt".format(l2), "a") as f:
    #     f.write("\n")
    #     f.write(str(result))
    #     f.write("\n")
    # logger.info("Image has been rade from opencv model")

    # # Checking Result...
    if result:
        # print(result)
        # print(len(result))
        # print(result)
        # Assign empty list to append final result...
        codelist = []
        code6 = []
        code5 = []

        # Running for loop into OCR result to check special character...

        if result == "":
            print("Blank OCR Result")
            logger.info("Blank OCR Result came for EasyOCR")

        else:

            if len(result) >= 2:
                # print("code length is more then 1")

                for z in result:
                    # print(z[1])
                    code6.append(z)
                    code5.append(z)

                # Take the proper number index from the list...
                A = str(code6[0][1]) + str(code5[1][1])

                # Replace the special character to 1...
                a = A.replace('|', '1')
                b = a.replace('/', '1')
                c = b.replace('!', '1')
                d = c.replace('(', '1')
                e = d.replace(')', '1')
                f = e.replace('S', '5')
                g = f.replace('&', 'x')
                h = g.replace('%', 'x')
                i = h.replace('^', '1')
                j = i.replace('p', 'B')
                k = j.replace('$', '9')
                l = k.replace('[', '1')
                m = l.replace('@', '2')
                n = m.replace('I', '1')
                o = n.replace('i', '1')
                p = o.replace('g', '9')
                q = p.replace('e', '2')
                r = q.replace('}', '1')
                s = r.replace(']', '1')
                t = s.replace('l', '1')
                u = t.replace('o', '0')
                v = u.replace('a', '4')
                result = v.replace('?', '1')
                # print("result1-{}".format(result1+result1))

                finalcode = result1
                logger.info("All special character has been removed")

                # # Appending final code result to codelist variable...
                codelist.append(finalcode)

                # # print(codelist)

                # Converting list to string for mapping with IR data...
                code = ''.join(codelist)
                logger.info("Final Code has been taken after replaced special character-{}".format(code))
                # print(type(code))
                # print("code-{}".format(code))

                if code:
                    # print(len(str(code)))
                    # print(code)

                    # for r in code:

                        # print(code)

                    if len(str(r)) >= 11:
                        num11list.append(str(r))
                        # print(num11list)
                        # print("DETECTED-{}".format(r))
                        # wagonid.append(int(r))
                        # det=1

                    elif len(str(r)) == 10:
                        # if str(r) not in num10_list:
                        num10_list.append(str(r))

                    elif len(str(r)) == 9:
                        # if str(r) not in num9_list:
                        num9_list.append(str(r))
                        # print(num9_list)

                    elif len(str(r)) == 8:
                        # if str(r) not in num8_list:
                        num8_list.append(str(r))
                        # print(num8_list)

                    elif len(str(r)) == 7:
                        # if str(r) not in num7_list:
                        num7_list.append(str(r))

                    elif len(str(r)) == 6:
                        # if str(r) not in num6list:
                        num6list.append(str(r))
                        # print(num6list)
                        # num56_list.append(str(r))

                    elif len(str(r)) == 5:
                        # if str(r) not in num5list:
                        num5list.append(str(r))
                        # print(num5list)
                        # num56_list.append(str(r))

                    elif len(str(r)) == 4:
                        num4_list.append(str(r))

                    temp_list = []

                    # CHECK IF ANY 11 DIGIT wagonid DETECTED...IF YES..THEN WE GOT ONE
                    if len(num11list) > 0:
                        # print(num11list)
                        n11 = max(num11list, key=num11list.count)
                        temp_list.append(n11)
                        # for i in codecolumn:
                        #     if str(n11) in str(i):
                        #         # print(i)
                        #         temp_list.append(str(i))
                        #         # # print(temp_list)
                        #         # # final_list.append(re.findall(r'\d+',n11))
                        #         # # temp_list = final_list[0]
                        #         #
                        #         # db = 11
                        #         # # logger.info("DETECTED-{}".format(n11))
                        #         # # logger.info("Detected from 11 digit DB")
                        #         # wagonid.append(n11)
                        #         # # #print("DETECTED-{}".format(n11))
                        #         # # out_dict['Wagon_Number'] = str(n11)
                        #         # # out_dict['Path'] = code_img_path_list
                        # det = 1

                    # CHECK IN DB (INDIVIDUALLY FOR 7/8/9/10 DIGIT )
                    # if det != 1:
                    if len(num10_list) > 0:
                        temp10 = max(num10_list, key=num10_list.count)
                        temp_list.append(temp10)
                            # # for n in num10_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 10
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         # logger.info("Detected from DB (10 digit)-{}".format(wn))
                            #         temp_list.append(str(wn))
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]

                    # if det != 1:
                    if len(num9_list) > 0:
                        temp9 = max(num9_list, key=num9_list.count)
                        temp_list.append(temp9)
                        # for n in num9_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 9
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         # logger.info("Detected from DB (9 digit)-{}".format(wn))
                            #         temp_list.append(str(wn))
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]

                    # if det != 1:
                    if len(num8_list) > 0:
                        temp8 = max(num8_list, key=num8_list.count)
                        temp_list.append(temp8)
                            # # for n in num8_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 8
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         temp_list.append(str(wn))
                            #
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]
                            #         # logger.info("Detected from DB (8 digit)-{}".format(wn))
                            #         # break

                    # if det != 1:
                    #     if len(num8_list) > 0:
                    #         temp = max(num8_list, key=num8_list.count)
                    #         temp_5 = temp[-4:]
                    #         # for n in num8_list:
                    #         for wn in codecolumn:
                    #             if str(temp_5) in str(wn):
                    #                 # print(wn)
                    #                 det = 1
                    #                 db = 8
                    #                 wagonid.append(wn)
                    #                 # out_dict['Wagon_Number'] = str(wn)
                    #                 # out_dict['Path'] = code_img_path_list
                    #                 temp_list.append(str(wn))
                    #                 # print(temp_list)
                    #                 # final_list.append(re.findall(r'\d+', wn))
                    #                 # temp_list = final_list[0]

                    if det != 1:
                        if len(num7_list) > 0:
                            temp7 = max(num7_list, key=num7_list.count)
                            temp_list.append(temp7)
                            # # for n in num7_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 7
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         temp_list.append(str(wn))
                            #
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]
                            #         # logger.info("Detected from DB (7 digit)-{}".format(wn))
                            #         # break

                    if len(num6list) > 0:
                        # print(num5list)
                        temp6 = max(num6list, key=num5list.count)
                        temp_list.append(temp6)
                            # print(temp)
                            # for n in num7_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         # print(wn)
                            #
                            #         det = 1
                            #         db = 7
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         temp_list.append(str(wn))
                            #         # print(temp_list)
                            #
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list
                            #         # logger.info("Detected from DB (7 digit)-{}".format(wn))
                            #         # break

                    # if det != 1:
                        # print(num5list)
                        # print("22")
                    if len(num5list) > 0:
                        # print(num5list)
                        temp5 = max(num5list, key=num5list.count)
                        temp_list.append(temp5)
                            # print(temp)
                            # temp_5 = temp[-4:]
                        # temp_list1 = re.findall('\d+', temp_list)


                    # IF NO 11 DIGIT wagonid DETECTED SO FAR THEN CHECK FOR 5 & 6 DIGIT COMBINATION
                    # if det != 1:
                    #     if len(num5list) > 0 and len(num6list) > 0:
                    #         n5 = max(num5list, key=num5list.count)
                    #         n6 = max(num6list, key=num6list.count)
                    #         if str(n5) not in str(n6):
                    #             n = str(n6) + str(n5)
                    #             if len(str(n)) == 11:
                    #
                    #                 for i in codecolumn:
                    #
                    #                     if str(n) in str(i):
                    #                         db = 56
                    #                         wagonid.append(str(n))
                    #                         temp_list.append(str(n))
                    #                         det = 1
                                            # #print("DETECTED-{}".format(n))
                                            # logger.info("Detected from DB (5+6 digit combo)-{}".format(wn))
                                            # logger.info("DETECTED-{}".format(n))
                                            # out_dict['Wagon_Number'] = str(n)
                                            # out_dict['Path'] = code_img_path_list

                                            # final_list.append(re.findall(r'\d+', n))
                                            # temp_list = final_list[0]
                                            # break

                    # CHECK IF SOMETHING MAPPED SO FAR
                    # if det == 1:
                        # print(temp_list)
                        # final_list.append(re.findall(r'\d+', temp_list))
                    return temp_list[0]

                else:
                    print("Blank OCR Result")

                # return (codelist)

            else:

                for z in result:
                    # Take the proper number index from the list...
                    A = str(z[1])
                    # print(A)

                    # Replace the special character to 1...
                    a = A.replace('|', '1')
                    b = a.replace('/', '1')
                    c = b.replace('!', '1')
                    d = c.replace('(', '1')
                    e = d.replace(')', '1')
                    f = e.replace('S', '5')
                    g = f.replace('&', 'x')
                    h = g.replace('%', 'x')
                    i = h.replace('^', '1')
                    j = i.replace('p', 'B')
                    k = j.replace('$', '9')
                    l = k.replace('[', '1')
                    m = l.replace('@', '2')
                    n = m.replace('I', '1')
                    o = n.replace('i', '1')
                    p = o.replace('g', '9')
                    q = p.replace('e', '2')
                    r = q.replace('}', '1')
                    s = r.replace(']', '1')
                    t = s.replace('l', '1')
                    u = t.replace('o', '0')
                    v = u.replace('a', '4')
                    result = v.replace('?', '1')

                    finalcode = result
                    logger.info("All special character has been removed")

                    # Appending final code result to codelist variable...
                    codelist.append(finalcode)
                    # print(codelist)

                    # Converting list to string for mapping with IR data...
                    code = ''.join(codelist)
                    logger.info("Final Code has been taken after replaced special character-{}".format(code))
                    # print(code)

                    # with open("/home/vert/JSW_Project/01_WAGON_NUMBER_TRACKING_Vallari/Images_Videos/Cam_1_INFO/OCR_Result/OCR_Result {}.txt".format(l2), "a") as f:
                    #     # f.write("extract code from wagon -{}".format(Wagon_number))
                    #     # f.write("; ")
                    #     f.write(code)
                    #     f.write("; ")
                    #     # f.write("*" * 20)
                    #     print("code written")
                    if code:
                        # print(len(str(code)))
                        # print(code)

                        if len(str(r)) >= 11:
                            num11list.append(str(r))
                            # print(num11list)
                            # print("DETECTED-{}".format(r))
                            # wagonid.append(int(r))
                            # det=1

                        elif len(str(r)) == 10:
                            # if str(r) not in num10_list:
                            num10_list.append(str(r))

                        elif len(str(r)) == 9:
                            # if str(r) not in num9_list:
                            num9_list.append(str(r))
                            # print(num9_list)

                        elif len(str(r)) == 8:
                            # if str(r) not in num8_list:
                            num8_list.append(str(r))
                            # print(num8_list)

                        elif len(str(r)) == 7:
                            # if str(r) not in num7_list:
                            num7_list.append(str(r))

                        elif len(str(r)) == 6:
                            # if str(r) not in num6list:
                            num6list.append(str(r))
                            # print(num6list)
                            # num56_list.append(str(r))

                        elif len(str(r)) == 5:
                            # if str(r) not in num5list:
                            num5list.append(str(r))
                            # print(num5list)
                            # num56_list.append(str(r))

                        elif len(str(r)) == 4:
                            num4_list.append(str(r))

                        temp_list = []

                        # CHECK IF ANY 11 DIGIT wagonid DETECTED...IF YES..THEN WE GOT ONE
                        if len(num11list) > 0:
                            # print(num11list)
                            n11 = max(num11list, key=num11list.count)
                            temp_list.append(n11)
                            # print(temp_list)
                            # for i in codecolumn:
                            #     if str(n11) in str(i):
                            #         # print(i)
                            #         temp_list.append(str(i))
                            #         # # print(temp_list)
                            #         # # final_list.append(re.findall(r'\d+',n11))
                            #         # # temp_list = final_list[0]
                            #         #
                            #         # db = 11
                            #         # # logger.info("DETECTED-{}".format(n11))
                            #         # # logger.info("Detected from 11 digit DB")
                            #         # wagonid.append(n11)
                            #         # # #print("DETECTED-{}".format(n11))
                            #         # # out_dict['Wagon_Number'] = str(n11)
                            #         # # out_dict['Path'] = code_img_path_list
                            # det = 1

                        # CHECK IN DB (INDIVIDUALLY FOR 7/8/9/10 DIGIT )
                        # if det != 1:
                        if len(num10_list) > 0:
                            temp10 = max(num10_list, key=num10_list.count)
                            temp_list.append(temp10)
                            # # for n in num10_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 10
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         # logger.info("Detected from DB (10 digit)-{}".format(wn))
                            #         temp_list.append(str(wn))
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]

                        # if det != 1:
                        if len(num9_list) > 0:
                            temp9 = max(num9_list, key=num9_list.count)
                            temp_list.append(temp9)
                            # for n in num9_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 9
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         # logger.info("Detected from DB (9 digit)-{}".format(wn))
                            #         temp_list.append(str(wn))
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]

                        # if det != 1:
                        if len(num8_list) > 0:
                            temp8 = max(num8_list, key=num8_list.count)
                            temp_list.append(temp8)
                            # # for n in num8_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         det = 1
                            #         db = 8
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         temp_list.append(str(wn))
                            #
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list[0]
                            #         # logger.info("Detected from DB (8 digit)-{}".format(wn))
                            #         # break

                        # if det != 1:
                        #     if len(num8_list) > 0:
                        #         temp = max(num8_list, key=num8_list.count)
                        #         temp_5 = temp[-4:]
                        #         # for n in num8_list:
                        #         for wn in codecolumn:
                        #             if str(temp_5) in str(wn):
                        #                 # print(wn)
                        #                 det = 1
                        #                 db = 8
                        #                 wagonid.append(wn)
                        #                 # out_dict['Wagon_Number'] = str(wn)
                        #                 # out_dict['Path'] = code_img_path_list
                        #                 temp_list.append(str(wn))
                        #                 # print(temp_list)
                        #                 # final_list.append(re.findall(r'\d+', wn))
                        #                 # temp_list = final_list[0]

                        if det != 1:
                            if len(num7_list) > 0:
                                temp7 = max(num7_list, key=num7_list.count)
                                temp_list.append(temp7)
                                # # for n in num7_list:
                                # for wn in codecolumn:
                                #     if str(temp) in str(wn):
                                #         det = 1
                                #         db = 7
                                #         wagonid.append(wn)
                                #         # out_dict['Wagon_Number'] = str(wn)
                                #         # out_dict['Path'] = code_img_path_list
                                #         temp_list.append(str(wn))
                                #
                                #         # final_list.append(re.findall(r'\d+', wn))
                                #         # temp_list = final_list[0]
                                #         # logger.info("Detected from DB (7 digit)-{}".format(wn))
                                #         # break

                        if len(num6list) > 0:
                            # print(num5list)
                            temp6 = max(num6list, key=num5list.count)
                            temp_list.append(temp6)
                            # print(temp)
                            # for n in num7_list:
                            # for wn in codecolumn:
                            #     if str(temp) in str(wn):
                            #         # print(wn)
                            #
                            #         det = 1
                            #         db = 7
                            #         wagonid.append(wn)
                            #         # out_dict['Wagon_Number'] = str(wn)
                            #         # out_dict['Path'] = code_img_path_list
                            #         temp_list.append(str(wn))
                            #         # print(temp_list)
                            #
                            #         # final_list.append(re.findall(r'\d+', wn))
                            #         # temp_list = final_list
                            #         # logger.info("Detected from DB (7 digit)-{}".format(wn))
                            #         # break

                        # if det != 1:
                        # print(num5list)
                        # print("22")
                        if len(num5list) > 0:
                            # print(num5list)
                            temp5 = max(num5list, key=num5list.count)
                            temp_list.append(temp5)
                            # print(temp)
                            # temp_5 = temp[-4:]

                            # IF NO 11 DIGIT wagonid DETECTED SO FAR THEN CHECK FOR 5 & 6 DIGIT COMBINATION
                            # if det != 1:
                            #     if len(num5list) > 0 and len(num6list) > 0:
                            #         n5 = max(num5list, key=num5list.count)
                            #         n6 = max(num6list, key=num6list.count)
                            #         if str(n5) not in str(n6):
                            #             n = str(n6) + str(n5)
                            #             if len(str(n)) == 11:
                            #
                            #                 for i in codecolumn:
                            #
                            #                     if str(n) in str(i):
                            #                         db = 56
                            #                         wagonid.append(str(n))
                            #                         temp_list.append(str(n))
                            #                         det = 1
                            # #print("DETECTED-{}".format(n))
                            # logger.info("Detected from DB (5+6 digit combo)-{}".format(wn))
                            # logger.info("DETECTED-{}".format(n))
                            # out_dict['Wagon_Number'] = str(n)
                            # out_dict['Path'] = code_img_path_list

                            # final_list.append(re.findall(r'\d+', n))
                            # temp_list = final_list[0]
                            # break

                            # CHECK IF SOMETHING MAPPED SO FAR
                            # if det == 1:
                            # print(temp_list)
                            # final_list.append(re.findall(r'\d+', temp_list))
                            # temp_list1 = re.findall('\d+', temp_list)

                        return temp_list[0]

                            # return (codelist)
#
# x = Easy_OCR("/home/jsw/Desktop/image/image_128.jpg")
# print(x)