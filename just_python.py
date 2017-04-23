def fn_amount_to_string(amount):
    def num_to_str(num):
        d = {0: 'صفر', 1: 'واحد', 2: 'اثنين', 3: 'ثلاثه', 4: 'اربعه', 5: 'خمسه',
             6: 'ستة', 7: 'سبعة', 8: 'ثمانية', 9: 'تسعة', 10: 'عشرة',
             11: 'أحد عشر', 12: 'اثنا عشر', 13: 'ثلاثه عشر', 14: 'اربعة عشر',
             15: 'خمسة عشر', 16: 'ستة عشر', 17: 'سبعه عشر', 18: 'ثمانية عشر',
             19: 'تسعة عشر', 20: 'عشرون',
             30: 'ثلاثون', 40: 'اربعون', 50: 'خمسون', 60: 'ستون',
             70: 'سبعون', 80: 'ثمانون', 90: 'تسعون',
             100: 'مئة ', 200: 'مئتان ', 300: 'ثلثمائة ', 400: 'اربعمائة ',
             500: 'خمسمائة ', 600: 'ستمائة ', 700: 'سبعمائة ', 800: 'ثمانمائة ', 900: 'تسعمائة ',
             1000: 'الف ', 2000: 'الفان ', 3000: 'ثلاثة الاف ', 4000: 'اربعة الاف ',
             5000: 'خمسة الاف ', 6000: 'ستة الاف', 7000: 'سبعة الاف', 8000: 'ثمانية الاف ', 9000: 'تسعة الاف ',
             10000: 'عشره الاف '}
        k = 1000
        m = k * 1000
        b = m * 1000
        t = b * 1000

        assert (0 <= num)

        if (num < 20):
            return d[num]

        if (num < 100):
            if num % 10 == 0:
                return d[num]
            else:
                return d[num % 10] + ' و ' + d[num // 10 * 10]

        if (num < k):
            if num < 200 and num % 100 == 0:
                return d[100]
            elif num < 300 and num % 200 == 0:
                return d[200]
            elif num < 400 and num % 300 == 0:
                return d[300]
            elif num < 500 and num % 400 == 0:
                return d[400]
            elif num < 600 and num % 500 == 0:
                return d[500]
            elif num < 700 and num % 600 == 0:
                return d[600]
            elif num < 800 and num % 700 == 0:
                return d[700]
            elif num < 900 and num % 800 == 0:
                return d[800]
            elif num < 1000 and num % 900 == 0:
                return d[900]

            else:
                return d[num // 100 * 100] + 'و ' + num_to_str(num % 100)

        if (num < m):
            if num < 2000 and num % 1000 == 0:
                return d[1000]
            elif num < 3000 and num % 2000 == 0:
                return d[2000]
            elif num < 4000 and num % 3000 == 0:
                return d[3000]
            elif num < 5000 and num % 40000 == 0:
                return d[4000]
            elif num < 6000 and num % 5000 == 0:
                return d[500]
            elif num < 7000 and num % 6000 == 0:
                return d[6000]
            elif num < 8000 and num % 7000 == 0:
                return d[700]
            elif num < 9000 and num % 8000 == 0:
                return d[8000]
            elif num < 10000 and num % 9000 == 0:
                return d[9000]

            else:
                return d[num // 1000 * 1000] + 'و ' + num_to_str(num % 1000)


        raise AssertionError('num is too large: %s' % str(num))

    int_num = int(amount)
    dec_num = int(str(amount).split('.')[1])
    if len(str(int_num))<= 4 :
        return num_to_str(int_num) + " جنيها و " + num_to_str(dec_num) + " قرشا "
    if len(str(int_num)) == 5 :
        x1=int(str(int_num)[0:2])
        x2 = int(str(int_num)[2:])
        if x2 > 0:
            return num_to_str(x1) + ' الاف و ' + num_to_str(x2) + " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        elif x2 == 0:
            return num_to_str(x1) + ' الاف ' + " جنيها و " + num_to_str(dec_num) + " قرشا "

    if len(str(int_num)) == 6 :
        x1=int(str(int_num)[0:3])
        x2 = int(str(int_num)[3:])
        if x2>0:
            return num_to_str(x1) + ' الاف و ' + num_to_str(x2) + " جنيها و " + num_to_str(dec_num) + " قرشا "
        elif x2 == 0:
            return num_to_str(x1) + ' الاف '  + " جنيها و " + num_to_str(dec_num) + " قرشا "

    if len(str(int_num)) == 7:
        x1 = int(str(int_num)[0:1])
        x2 = int(str(int_num)[1:4])
        x3 = int(str(int_num)[4:])
        if x2>0 and x3>0:
           return num_to_str(x1) + ' مليون و ' +num_to_str(x2) + ' الاف و ' + num_to_str(x3) + " جنيها و " + num_to_str(dec_num) + " قرشا "
        elif x2==0 and x3>0:
            return num_to_str(x1) + ' مليون و '  + num_to_str(x3) + " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        elif x2 > 0 and x3 == 0:
            return num_to_str(x1) + ' مليون و ' + num_to_str(x2) + ' الاف ' +  " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        if x2 == 0 and x3 == 0:
            return num_to_str(x1) + ' مليون  ' + " جنيها و " + num_to_str(
                dec_num) + " قرشا "

    if len(str(int_num)) == 8:
        x1 = int(str(int_num)[0:2])
        x2 = int(str(int_num)[2:5])
        x3 = int(str(int_num)[5:])
        if x2>0 and x3>0:
           return num_to_str(x1) + ' مليون و ' +num_to_str(x2) + ' الاف و ' + num_to_str(x3) + " جنيها و " + num_to_str(dec_num) + " قرشا "
        elif x2==0 and x3>0:
            return num_to_str(x1) + ' مليون و '  + num_to_str(x3) + " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        elif x2 > 0 and x3 == 0:
            return num_to_str(x1) + ' مليون و ' + num_to_str(x2) + ' الاف ' +  " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        if x2 == 0 and x3 == 0:
            return num_to_str(x1) + ' مليون ' + " جنيها و " + num_to_str(
                dec_num) + " قرشا "

    if len(str(int_num)) == 9:
        x1 = int(str(int_num)[0:3])
        x2 = int(str(int_num)[3:6])
        x3 = int(str(int_num)[6:])
        if x2>0 and x3>0:
           return num_to_str(x1) + ' مليون و ' +num_to_str(x2) + ' الاف و ' + num_to_str(x3) + " جنيها و " + num_to_str(dec_num) + " قرشا "
        elif x2==0 and x3>0:
            return num_to_str(x1) + ' مليون و '  + num_to_str(x3) + " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        elif x2 > 0 and x3 == 0:
            return num_to_str(x1) + ' مليون و ' + num_to_str(x2) + ' الاف ' +  " جنيها و " + num_to_str(
                dec_num) + " قرشا "
        if x2 == 0 and x3 == 0:
            return num_to_str(x1) + ' مليون  ' + " جنيها و " + num_to_str(
                dec_num) + " قرشا "


print(fn_amount_to_string(1551.0))

print('12345678'[5:])

print 'aaaa'

